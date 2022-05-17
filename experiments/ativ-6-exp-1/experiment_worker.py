import subprocess
from tqdm import tqdm
from pathlib import Path
import sys
import json
import re

def run_command(cmd, **popen_kwargs):
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,stderr=subprocess.PIPE, bufsize=1, universal_newlines=True, **popen_kwargs) as p:
        for line in p.stdout:
            print(line, end='') # process line here

    if p.returncode != 0:
        raise CalledProcessError(p.returncode, p.args)

    return

def build_experimnt():
    COMMAND = "mkdir cifar10 && cd cifar10 ;" + \
        "wget --no-check-certificate https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz ;" + \
        "tar -xvf cifar-10-python.tar.gz ;" + \
        "cd .."
    
    run_command(COMMAND)
    return
    
def run_experiment():
    
    ip = input('Type the Private IP address of the Master node:')
    COMMAND = rf'cd ../..; sudo docker run --env OMP_NUM_THREADS=1 --rm --network=host -v=$(pwd):/root dist_dcgan:latest python -m torch.distributed.launch --nproc_per_node=##NPROCS## --nnodes=2 --node_rank=1 --master_addr="{ip}" --master_port=1234 dist_dcgan.py --dataset cifar10 --dataroot ./cifar10 --num_epochs=1 --batch_size=16'
    
    nprocs = [1,2,4,8]
    n_repeats = 3
    result_dict = {i:[] for i in nprocs}
    #setup
    proc = subprocess.run(COMMAND.replace('##NPROCS##', str(4)), capture_output=False, shell=True)            
    for i in tqdm(nprocs[::-1]):
        for _ in range(n_repeats):
            proc = subprocess.run(COMMAND.replace('##NPROCS##', str(i)), capture_output=False, shell=True)            
   
    return
	
if __name__ == '__main__':
	run_experiment()	
	



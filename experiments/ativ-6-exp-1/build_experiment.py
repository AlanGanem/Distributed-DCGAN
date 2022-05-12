import subprocess

if __name__ == "__main__":
    COMMAND = [
        "sudo apt install python3-pip ;",
        "pip3 install -r exp_requirements.txt ;",
        "sudo apt update ;",
        "sudo apt install -y docker.io ; ",
        "cd ../.. ; mkdir cifar10 && cd cifar10 ; ",
        "wget --no-check-certificate https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz ; ",
        "tar -xvf cifar-10-python.tar.gz ; ",
        "sudo docker build -t dist_dcgan .",
    ]
    
    COMMAND = ''.join(COMMAND)
    subprocess.run(COMMAND, shell = True)

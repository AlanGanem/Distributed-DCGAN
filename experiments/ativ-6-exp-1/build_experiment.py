import subprocess

if __name__ == "__main__":
    COMMAND = "cd ../.. ; mkdir cifar10 && cd cifar10 ; " + \
        "wget --no-check-certificate https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz ; " + \
        "tar -xvf cifar-10-python.tar.gz ; " + \
        "cd .. ; " + \
        "sudo apt install docker.io ; " +\
        "docker build -t dist_dcgan ."
    subprocess.run(COMMAND, shell = True)

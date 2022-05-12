import subprocess

if __name__ == "__main__":
    COMMAND = "sudo apt install -y docker.io ; " +\
        "cd ../.. ; mkdir cifar10 && cd cifar10 ; " + \
        "wget --no-check-certificate https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz ; " + \
        "tar -xvf cifar-10-python.tar.gz ; " + \
        "docker build -t dist_dcgan ."
    subprocess.run(COMMAND, shell = True)

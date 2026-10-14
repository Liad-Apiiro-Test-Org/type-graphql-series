import subprocess


def deploy(target):
    subprocess.call("bash -c 'deploy " + target + "'", shell=True)

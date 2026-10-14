import os
import subprocess


def archive(target):
    os.system("tar -czf /tmp/flow42.tgz " + target)


def push_remote(host, path):
    subprocess.call("scp " + path + " " + host + ":/data", shell=True)

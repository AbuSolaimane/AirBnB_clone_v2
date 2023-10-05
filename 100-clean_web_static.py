#!/usr/bin/python3
"""
this is a module
"""

from datetime import datetime
from fabric.api import run, local, put, env
from os import path
env.hosts = ['107.23.107.180', '52.3.242.207']


def do_clean(number=0):
    """
    this is a method
    """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]

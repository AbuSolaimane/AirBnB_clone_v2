#!/usr/bin/python3
"""
this is a module
"""

from datetime import datetime
from fabric.api import run, local, put, env
from os import path
env.hosts = ['107.23.107.180', '52.3.242.207']


def do_deploy(archive_path):
    """
    this is a method
    """
    if path.exists(archive_path) is False:
        return False

    try:
        upload = put(archive_path, "/tmp/")
        name = archive_path[9:-4]
        rmt_path = "/data/web_static/releases/" + name
        run("mkdir {}".format(rmt_path))
        run("tar -xvzf /tmp/{}.tgz --directory {}/".format(name, rmt_path))
        run("rm /tmp/{}.tgz".format(name))
        run("rm /data/web_static/current")
        run("ln -nsf /data/web_static/releases/{} /data/web_static/current"
            .format(name))
        run("mv {}/web_static/* {}".format(rmt_path, rmt_path))
        run("rm -d {}/web_static/".format(rmt_path))
        return True
    except Exception:
        return False
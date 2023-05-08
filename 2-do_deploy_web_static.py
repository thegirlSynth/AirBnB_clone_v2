#!/usr/bin/python3
"""This module contians a function do_deploy."""
from fabric.api import *
import os.path


env.user = "ubuntu"
env.hosts = ["52.86.108.58", "100.25.205.85"]


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        filename_with_ext = archive_path.split('/')[-1]
        filename = filename_with_ext.split('.')[0]
        run("mkdir -p /data/web_static/releases/{}".format(filename))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(filename_with_ext, filename))
        run("rm /tmp/{}".format(filename_with_ext))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}".format(filename, filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(filename))
        return True
    except BaseException:
        return False

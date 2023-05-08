#!/usr/bin/python3
"""This module contians a function do_pack."""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Generates a .tgz archive from the contents of the web_static folder
    on my AirBnB clone repo"""

    try:
        if not os.path.exists("./versions"):
            local("mkdir versions")
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        newfile = "web_static_" + time + ".tgz"
        local("tar -czvf versions/{} web_static".format(newfile))
        return os.path.abspath("./versions/{}".format(filename))
    except BaseException:
        return None

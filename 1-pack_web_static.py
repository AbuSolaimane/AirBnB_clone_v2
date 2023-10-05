#!/usr/bin/python3
"""
this is a module
"""

from datetime import datetime
from fabric.api import run, local, put


def do_pack():
    """
    this is a class
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    if local('tar -cvzf versions/{} web_static'.format(archive)) is not None:
        return archive
    else:
        return None

# coding: utf-8

from fabric.api import *

import sys

sys.path.append('.')


def dev():
    from curlbin import app
    app.run()

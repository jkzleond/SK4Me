#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time      : 2017-09-24 14:53
# @Author    : modm
'''
you can start the server by uwsgi
like gunicorn -w 4 SK4Me.uwsgi:app
'''
from SK4Me.app import app, initialize

initialize()

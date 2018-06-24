#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mocker import app

@app.route('/')
def hello_world():
    return 'Hello, World!'

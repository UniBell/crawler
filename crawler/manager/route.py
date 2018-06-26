#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crawler.manager import app

@app.route('/')
def hello_world():
    return 'Hello, World 123!'

@app.route('/api/project')
def get_data():
    return {
        'name': '123'
    }

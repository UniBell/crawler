#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crawler.manager import app
from flask import jsonify

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/list')
def summary():
    array = (
        {
            'name': 'a'
        },
        {
            'name': 'b'
        },
        {
            'name': 'c'
        }
    )
    return jsonify({
        'data': array
    })

# @app.route('/add', method=POST)
# def add():


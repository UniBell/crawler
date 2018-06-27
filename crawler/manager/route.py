#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crawler.manager import app
from crawler.manager import db
from flask import jsonify
from crawler.manager.model import Project

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/list')
def summary():
    cursor = db.cursor()
    data = cursor.fetchone()
    return jsonify({
        'data': data
    })
    

@app.route('/add', methods=['POST'])
def add():
    print('aaa')
    a = Project(
        '1', 
        'abc', 
        1, 
        {
            'base_url': 'https://club.jd.com/comment/productPageComments.action',
            'interval': 3600
        },
        'test'
    )
    db.session.add(a)
    db.session.commit()
    print('bbb')

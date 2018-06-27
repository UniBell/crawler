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
    

@app.route('/add/<Project:project>', methods=['POST'])
def add(project):
    print('aaa')
    db.session.add(project)
    db.session.commit()
    print('bbb')

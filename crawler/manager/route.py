#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crawler.manager import app
from crawler.manager import db
from flask import jsonify
from crawler.manager import utils
from crawler.manager.model import Project
from flask import request
from flask import make_response,Response

def Response_headers(content):  
    resp = Response(content)  
    resp.headers['Access-Control-Allow-Origin'] = '*'  
    return resp

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/list')
def summary():
    rows = Project.query.all()
    l = []
    for row in rows:
        l.append(utils.object_as_dict(row))
    return jsonify({
        'data': l
    })
    

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        dic = {
            'id': request.form.get('id'),
            'name': request.form.get('name'),
            'behavior': request.form.get('behavior'),
            'config': request.form.get('config'),
            'desc': request.form.get('desc')
        }
        project = Project(**dic)
        db.session.add(project)
        db.session.commit()
        resp = Response_headers(dic)  
        return jsonify({
            "message": "success",
            "code": 200,
            "data": resp
        })

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        return ''

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        projectId = request.form.get('id')
        dic = {
            'id': request.form.get('id'),
            'name': request.form.get('name'),
            'behavior': request.form.get('behavior'),
            'config': request.form.get('config'),
            'desc': request.form.get('desc')
        }
        project = Project(**dic)
        db.session.add(project)
        db.session.query(Project).filter(Project.id == projectId).update({Project: dic})

        db.session.commit()
        return {
            "message": 'success'
        }

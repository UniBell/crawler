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
        return jsonify({
            "message": "success",
        })

@app.route('/delete', methods=['POST'])
def delete():
    if request.method == 'POST':
        project = Project.query.filter_by(id = request.form.get('id')).first()
        db.session.delete(project)
        db.session.commit()
        return jsonify({
            "message": "success",
        })

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST':
        projectId = request.form.get('id')
        dic = {
            'name': request.form.get('name'),
            'behavior': request.form.get('behavior'),
            'config': request.form.get('config'),
            'desc': request.form.get('desc')
        }
        project = Project.query.filter_by(id = projectId).first()
        project.name = dic['name']
        project.behavior = dic['behavior']
        project.config = dic['config']
        project.desc = dic['desc']
        db.session.commit()
        return jsonify({
            "message": 'success'
        })

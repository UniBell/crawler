#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crawler.manager import app
from crawler.manager import db
from flask import jsonify
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
    # list = project.query.all()
    sql = 'select * from project;'
    data = db.session.execute(sql)
    return jsonify({
        'data': Project.dump(data)
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
        return resp

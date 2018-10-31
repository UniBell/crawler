#!/usr/bin/env python
# -*- coding: utf-8 -*-

from crawler.manager import db

class Project(db.Model):
    #自增id
    id = db.Column(db.Integer, primary_key = True)
    #项目名字
    name = db.Column(db.String(20), unique = True, nullable = False)
    #项目行为，整型，比如0表示定时get url类型的项目
    behavior = db.Column(db.Integer(), unique = False, nullable = False)
    #项目配置，是一个json字符串，后续由对应的逻辑来处理
    config = db.Column(db.String(2000), unique = False, nullable = False)
    #项目描述，可选
    desc = db.Column(db.String(120), unique = False, nullable = True)

class OrderBook(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    table = db.Column(db.String(20), unique = True, nullable = False)
    action = db.Column(db.String(20), unique = True, nullable = False)
    data = db.Column(db.String(20), unique = True, nullable = False)


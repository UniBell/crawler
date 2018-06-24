#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mocker import db

class Service(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), unique = True, nullable = False)
    port = db.Column(db.Integer(), unique = True, nullable = False)
    desc = db.Column(db.String(120), unique = False, nullable = True)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:xxxxxx@localhost/crawler'
db = SQLAlchemy(app)

import crawler.manager.route
import crawler.manager.model
import crawler.Test.websocket_scrapy

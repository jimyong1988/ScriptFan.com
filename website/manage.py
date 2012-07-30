#!/usr/bin/env python
#-*-coding:utf-8-*-
import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask
from flaskext.script import Manager
from scriptfan import config_app, dispatch_handlers, dispatch_apps
from scriptfan.extensions import *

manager = Manager(app)

@manager.option('-c', '--config', dest='config', help='Configuration file name', default='scriptfan.cfg')
def test(config):
    config_app(app, config)
    dispatch_handlers(app)
    dispatch_apps(app)
    app.run(host='0.0.0.0')

@manager.option('-c', '--config', dest='config', help='Configuration file name', default='scriptfan.cfg')
def initdb(config='scriptfan.cfg'):
    config_app(app, config)
    from scriptfan.models import db

    try:
        db.drop_all()
        db.create_all()
        print 'Create tables success'
    except Exception as e:
        print 'Create tables fail:', e
        sys.exit(0)

if __name__ == '__main__':
    manager.run()


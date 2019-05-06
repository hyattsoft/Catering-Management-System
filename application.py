# _*_ coding:utf-8 _*_
# author: hyatt
# CreateDateTime: 2019/5/1 16:22
# FileName: application.py
# Email: kinagod@sina.com
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
import os


class Application(Flask):
    def __init__(self, import_name, template_folder=None, root_path=None):
        super(Application, self).__init__(import_name=import_name, template_folder=template_folder, root_path=root_path,
                                          static_folder=None)
        db.init_app(self)


db = SQLAlchemy()
app = Application(__name__, template_folder=os.getcwd()+"/website/templates", root_path=os.getcwd())
manager = Manager(app)


import route_blue

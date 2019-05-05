# _*_ coding:utf-8 _*_
# author: hyatt
# CreateDateTime: 2019-05-06 5:50
# FileName: table.py
# Email: kinagod@sina.com
from application import db

"""
餐桌定义
"""


class Table(db.Model):
    code = db.Column(db.String(6), primary_key=True, comment="")
    nickName = db.Column(db.String(20), nullable=False, comment="")
    content = db.Column(db.String(200), nullable=False, comment="")
    number = db.Column(db.Integer, nullable=False, comment="")
    max_number = db.Column(db.Integer, nullable=False, comment="")

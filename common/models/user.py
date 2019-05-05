# _*_ coding:utf-8 _*_
# author: hyatt
# CreateDateTime: 2019-05-06 5:08
# FileName: user.py
# Email: kinagod@sina.com
from application import db

"""
用户
"""


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment="")
    loginName = db.Column(db.String(50), unique=True, nullable=False, comment="")
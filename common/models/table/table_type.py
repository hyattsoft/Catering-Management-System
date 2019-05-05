# _*_ coding:utf-8 _*_
# author: hyatt
# CreateDateTime: 2019-05-06 6:02
# FileName: table_type.py
# Email: kinagod@sina.com
from application import db
"""
餐桌类型定义
"""


class TableType(db.Model):
    code = db.Column(db.String(6), primary_key=True, comment="类型编码")
    typeName = db.Column(db.String(20), nullable=False, unique=True, comment="类型名称")
    content = db.Column(db.String(200), comment="类型描述")
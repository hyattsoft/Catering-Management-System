# _*_ coding:utf-8 _*_
# author: hyatt
# CreateDateTime: 2019-05-06 5:57
# FileName: table_region.py
# Email: kinagod@sina.com
from application import db
"""
餐桌区域定义
"""


class TableRegion(db.Model):
    code = db.Column(db.String(6), primary_key=True, comment="区域编码")
    regionName = db.Column(db.String(20), nullable=False, unique=True, comment="区域名称")
    content = db.Column(db.String(200), comment="区域描述")

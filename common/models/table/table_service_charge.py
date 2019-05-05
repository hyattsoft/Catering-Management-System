# _*_ coding:utf-8 _*_
# author: hyatt
# CreateDateTime: 2019-05-06 6:07
# FileName: table_service_charge.py
# Email: kinagod@sina.com
from application import db
"""
餐桌服务费定义
"""


class TableServiceCharge(db.Model):
    code = db.Column(db.String(6), primary_key=True, comment="")
    chargeName = db.Column(db.String(20), nullable=False, comment="")

# _*_ coding:utf-8 _*_
# author: hyatt
# CreateDateTime: 2019/5/1 16:27
# FileName: route_blue.py
# Email: kinagod@sina.com

from website.api import api_blue
from application import app


app.register_blueprint(api_blue, url_prefix="/api")


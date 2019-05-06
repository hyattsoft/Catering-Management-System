# _*_ coding:utf-8 _*_
# author: hyatt
# CreateDateTime: 2019/5/5 9:33
# FileName: __init__.py.py
# Email: kinagod@sina.com

from flask import Blueprint

api_blue = Blueprint("api_blue", __name__)


@api_blue.route("/")
def index():
    return "API Doc"

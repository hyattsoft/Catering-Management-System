#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# author: hyatt
# CreateDateTime: 2019/5/1 16:22
# FileName: manager.py
# Email: kinagod@sina.com
from application import app, manager
from flask_script import Server
"""
程序启动管理器，工厂函数创建APP
"""

manager.add_command("runserver", Server(host="0.0.0.0", port=8999, use_debugger=True, use_reloader=True))


def main():
    manager.run()


if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())
    except Exception as e:
        import traceback
        traceback.print_exc()

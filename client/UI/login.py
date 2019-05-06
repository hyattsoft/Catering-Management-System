# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(341, 186)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 321, 131))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 30, 54, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 54, 12))
        self.label_2.setObjectName("label_2")
        self.txt_login = QtWidgets.QLineEdit(self.groupBox)
        self.txt_login.setGeometry(QtCore.QRect(120, 30, 113, 20))
        self.txt_login.setObjectName("txt_login")
        self.txt_pass = QtWidgets.QLineEdit(self.groupBox)
        self.txt_pass.setGeometry(QtCore.QRect(120, 90, 113, 20))
        self.txt_pass.setInputMask("")
        self.txt_pass.setText("")
        self.txt_pass.setObjectName("txt_pass")
        self.btn_login = QtWidgets.QPushButton(self.centralwidget)
        self.btn_login.setGeometry(QtCore.QRect(60, 150, 75, 23))
        self.btn_login.setObjectName("btn_login")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.btn_cancel.setObjectName("btn_cancel")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "凯悦云餐饮-前台登陆"))
        self.label.setText(_translate("MainWindow", "登陆名称："))
        self.label_2.setText(_translate("MainWindow", "登陆密码："))
        self.btn_login.setText(_translate("MainWindow", "登陆"))
        self.btn_cancel.setText(_translate("MainWindow", "取消"))



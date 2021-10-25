# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainpage1234.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# import pymysql
import datetime
import cv2
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import QTimer, QTime


### mysql 연결 ###

# conn = pymysql.connect(
#     user='smart-mirror',
#     passwd='1234',
#     host='localhost',
#     db='mirrordb',
#     charset='utf8'
# # )
# cursor = conn.cursor()



class Ui_Form_main(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")



        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 110, 64, 15))
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 160, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.pushButton2 = QtWidgets.QPushButton(Form)
        self.pushButton2.setGeometry(QtCore.QRect(220, 220, 93, 28))
        self.pushButton2.setObjectName("pushButton2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "main"))
        self.pushButton.setText(_translate("Form", "next"))
        self.pushButton2.setText(_translate("Form", "videoPage"))

class Ui_Form_next(object):
    def setupUi(self, Form, faceid):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 110, 200, 15))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 220, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form, faceid)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form, faceid):
        print(faceid)
        days = ['mon', 'tue', 'wen', 'thu', 'fri', 'sat', 'sun']
        today = datetime.datetime.today().weekday()
        faceid = str(faceid)
        sql = 'select name from medicine where userID=' + faceid +' && ' + days[today]+'=1'
        sql2 = 'select name from user where id=1'
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.execute(sql2)
        result2 = cursor.fetchall()
        i = 0
        today_medi=[]
        while(i<len(result)):
            medicine = result[i][0]
            print(medicine)
            today_medi.append(medicine)
            print(today_medi)
            if(medicine == pymysql.NULL):
                break
            i = i+1
        print(today_medi)

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", result2[0][0]+"님"+today_medi[0]+"드셨나요"))
        self.pushButton.setText(_translate("Form", "back"))

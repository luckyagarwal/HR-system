# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shortlisted.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import numpy as  np
from schedule_interview import Ui_MainWindow
class Ui_shortlisted_candidate(object):
    def __init__(self,table_,shor_ui):
        self.table_=table_
        self.shor_ui=shor_ui
        
        
    def showdata(self):
        for row_number,row_data in enumerate(self.table_):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
    
                   
    def setupUi(self, shortlisted_candidate):
        shortlisted_candidate.setObjectName("shortlisted_candidate")
        shortlisted_candidate.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(shortlisted_candidate)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(('Username,Email,Job_name,Date, Time').split(','))
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.showdata)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.send_email)
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        shortlisted_candidate.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(shortlisted_candidate)
        self.statusbar.setObjectName("statusbar")
        shortlisted_candidate.setStatusBar(self.statusbar)

        self.retranslateUi(shortlisted_candidate)
        QtCore.QMetaObject.connectSlotsByName(shortlisted_candidate)
    
    def send_email(self):
        self.sch= QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow(self.sch,self.shor_ui)
        self.ui.setupUi(self.sch)
        self.sch.show()
    
    def retranslateUi(self, shortlisted_candidate):
        _translate = QtCore.QCoreApplication.translate
        shortlisted_candidate.setWindowTitle(_translate("shortlisted_candidate", "Shortlisted candidate"))
        self.pushButton.setText(_translate("shortlisted_candidate", "Show"))
        self.pushButton_2.setText(_translate("shortlisted_candidate", "Schedule Interview"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Interview_results.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from thank import Ui_Dialog
class Ui_Interview_results(object):
    def __init__(self,table_,close_win):
        self.table_=table_
        self.close_win=close_win
        
    def showdata(self):
        for row_number,row_data in enumerate(self.table_):
            self.tableWidget.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.tableWidget.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
                
    def setupUi(self, Interview_results):
        Interview_results.setObjectName("Interview_results")
        Interview_results.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Interview_results)
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
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(50)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(('Username,Email,Job_name,Date, Time').split(','))
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.show = QtWidgets.QPushButton(self.frame)
        self.show.setObjectName("show")
        self.show.clicked.connect(self.showdata)
        self.horizontalLayout.addWidget(self.show)
        self.send_email = QtWidgets.QPushButton(self.frame)
        self.send_email.setObjectName("send_email")
        self.send_email.clicked.connect(self.close_wind)
        self.horizontalLayout.addWidget(self.send_email)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)
        Interview_results.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Interview_results)
        self.statusbar.setObjectName("statusbar")
        Interview_results.setStatusBar(self.statusbar)

        self.retranslateUi(Interview_results)
        QtCore.QMetaObject.connectSlotsByName(Interview_results)
        

        
    def close_wind(self):
        self.close_win.hide()
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        
    def retranslateUi(self, Interview_results):
        _translate = QtCore.QCoreApplication.translate
        Interview_results.setWindowTitle(_translate("Interview_results", "Interview_results"))
        self.show.setText(_translate("Interview_results", "Show"))
        self.send_email.setText(_translate("Interview_results", " Close"))


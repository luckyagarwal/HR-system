# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'creatd_vacant.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_vacant(object):
    def setupUi(self, vacant):
        vacant.setObjectName("vacant")
        vacant.resize(509, 246)
        self.gridLayout = QtWidgets.QGridLayout(vacant)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(vacant)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(130, 50, 221, 121))
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(vacant)
        QtCore.QMetaObject.connectSlotsByName(vacant)

    def retranslateUi(self, vacant):
        _translate = QtCore.QCoreApplication.translate
        vacant.setWindowTitle(_translate("vacant", "Dialog"))
        self.textEdit.setHtml(_translate("vacant", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt; font-weight:600; color:#00ffff;\">Created Vacancies</span></p></body></html>"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'h_r_portal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from abc import ABC ,abstractmethod
import database
#for randomly selecting participants from the first round..
import random
import sys
from welcome import Ui_Window_1
from error import Ui_Dialog

class Main_portal(ABC):
    pass
#We will provide unique access to the portal only to the HR using username and password
#we are creating a class for this purpose
class login(Main_portal):
    
    def __init__(self,username,password):
        #this is our constructor.
        print("add something here")
        self.username=username
        self.password=password
      
    #we need to check whether that username and password for the authentication
    
    def authenticate(self):
        #we need to search the Username in the database and match both of them..
        table_list=database.login_table()
        #authnticate logic
        auth=False
        for det in table_list:
            if(self.username.lower()==det[0].lower() and self.password==det[1]):
                auth=True
                break
            
        #return auth
        if(auth==True):
            return True
        else:
            return False

class job_categories(login):
    def __init__(self,vacant,job_name):
        #this is our constructor.
        print("add something here")
        self.vacant=vacant
        self.job_name=job_name
        
    
    def create_vacancies(self):
        database.update_job_catgories_table(self.job_name,self.vacant)
    
class Interview(Main_portal):
    pass

class Approval_shortlisting(Interview):
    def __init__(self,n_c):
        #this is our constructor.
        print("add something here")
        self.n_c=n_c
    
    def shortlist(self):
        table_list=database.Applicant_table()
        select_r_1=[] 
        for i in range(self.n_c):
            random.shuffle(table_list)
            select_r_1.append(table_list.pop())
        #now we need to update the table in which we have selected candidate..
        for ent in select_r_1:
            database.update_Applicant_table(ent[0],ent[1],1,1)
        #we need to create a separate table that contains shortlisted candidate from round 1
        for ent in select_r_1:
            database.insert_shortlisted_candidate(ent[0],ent[1],ent[4])
        
#ap=Approval_shortlisting(7)
#ap.shortlist()
        
class Scheduling_interview:
    def __init__(self,r_c):
        #this is our constructor.
        print("add something here")
        self.r_c=r_c 
        
    def shortlist_final(self):
        table_list=database.Applicant_table()
        intermed_list=[]
        for ent in table_list:
            if(ent[5]==1):
                intermed_list.append(ent)
        select_r_1=[]
        for i in range(self.r_c):
            random.shuffle(intermed_list)
            select_r_1.append(intermed_list.pop())
        #now we need to update the table in which we have selected candidate..
        for ent in select_r_1:
            database.update_Applicant_table(ent[0],ent[1],2,1)
        #we need to create a separate table that contains shortlisted candidate from round 1
        for ent in select_r_1:
            database.insert_final_candidate(ent[0],ent[1],ent[4])
    
#Sd=Scheduling_interview(3)
#Sd.shortlist_final()

class Interview_results(Interview):
    def __init__(self,r_c):
        #this is our constructor.
        print("add something here")
        self.r_n         
    def do_something(self):
        print("Do something")    
        
class Ui_H_r_portal(object):
    

        
    def setupUi(self, H_r_portal):
        H_r_portal.setObjectName("H_r_portal")
        H_r_portal.resize(640, 532)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI/icon_final.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        H_r_portal.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(H_r_portal)
        self.centralwidget.setMinimumSize(QtCore.QSize(640, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Tech = QtWidgets.QFrame(self.centralwidget)
        self.Tech.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.Tech.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Tech.setObjectName("Tech")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Tech)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.icon = QtWidgets.QLabel(self.Tech)
        self.icon.setText("")
        self.icon.setPixmap(QtGui.QPixmap("UI/imgonline-com-ua-resize-CTsWWNaYCcTcOI.png"))
        self.icon.setObjectName("icon")
        self.horizontalLayout.addWidget(self.icon)
        self.label_2 = QtWidgets.QLabel(self.Tech)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Avestan")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addWidget(self.Tech)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.login_icon = QtWidgets.QLabel(self.frame)
        self.login_icon.setText("")
        self.login_icon.setPixmap(QtGui.QPixmap("UI/rsz_kisspng-india-login-computer-icons-emoticon-medicine-user-login-icon-5ab05c8c27d4c14591099815215074681632.png"))
        self.login_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.login_icon.setObjectName("login_icon")
        self.verticalLayout_3.addWidget(self.login_icon)
        self.u_name = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.u_name.setFont(font)
        self.u_name.setObjectName("u_name")
        self.verticalLayout_3.addWidget(self.u_name)
        self.u_name_l = QtWidgets.QLineEdit(self.frame)
        self.u_name_l.setObjectName("u_name_l")
        self.verticalLayout_3.addWidget(self.u_name_l)
        self.password = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setObjectName("password")
        self.verticalLayout_3.addWidget(self.password)
        self.pass_l = QtWidgets.QLineEdit(self.frame)
        self.pass_l.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_l.setObjectName("pass_l")
        self.verticalLayout_3.addWidget(self.pass_l)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.enter)
        self.verticalLayout_3.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_3.addWidget(self.frame)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Noto Sans Armenian")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 305, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.frame_2)
        H_r_portal.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(H_r_portal)
        self.statusbar.setObjectName("statusbar")
        H_r_portal.setStatusBar(self.statusbar)
        self.retranslateUi(H_r_portal)
        QtCore.QMetaObject.connectSlotsByName(H_r_portal)
    
    
       
    def open_welcome(self):
        
        self.Window_1 = QtWidgets.QMainWindow()
        self.ui = Ui_Window_1()
        
        self.ui.setupUi(self.Window_1)
        self.Window_1.show()
        self.ui.create_vacancies()
        
    
        
    def enter(self):
        username=self.u_name_l.text()
        password=self.pass_l.text()
        log=login(username,password)
        authn=log.authenticate()
        if(authn==True):
            Ui_H_r.hide()
            self.open_welcome()
        else:
            print("error")
            self.error_win()
            
    def error_win(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()        
        
    def retranslateUi(self, H_r_portal):
        _translate = QtCore.QCoreApplication.translate
        H_r_portal.setWindowTitle(_translate("H_r_portal", "H R Portal"))
        self.label_2.setText(_translate("H_r_portal", "Tech Consultancy"))
        self.u_name.setText(_translate("H_r_portal", "Username"))
        self.password.setText(_translate("H_r_portal", "Password"))
        self.pushButton.setText(_translate("H_r_portal", "Login"))
        self.label.setText(_translate("H_r_portal", "ABOUT US:"))
        self.plainTextEdit.setPlainText(_translate("H_r_portal", "A human resource portal, or HR portal, is an internal gateway for a company’s employees to access HR-related and other information about their workplace. It is also an access point for outside job applicants and potential applicants. HR portals are usually dynamic and interactive and should not function only as repositories for benefits and other workplace information.\n"
"\n"
"The goal of an HR portal is to streamline and centralize information so that it is easy for employees to find what they need. For example, if handbooks, benefits enrollment details, and other information are on a portal, a company can save money by reducing printing costs and staff hours in distribution. (HR portals are frequently secure, so existing employees usually must have login credentials to access company information.)\n"
"\n"
"HR portals can also help connect human resource staff to employees (and vice versa) as well as reduce calls and emails between the two. If employees can find the information they need on their own, they do not need to involve HR staff."))
        

if (__name__=="__main__"):
    
    app = QtWidgets.QApplication(sys.argv)
    Ui_H_r= QtWidgets.QMainWindow()
    ui = Ui_H_r_portal( )
    ui.setupUi(Ui_H_r)
    Ui_H_r.show()
    sys.exit(app.exec_())

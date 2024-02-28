# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginpfxycx.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(535, 597)
        Login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logi_container = QFrame(self.centralwidget)
        self.logi_container.setObjectName(u"logi_container")
        self.logi_container.setGeometry(QRect(-10, -10, 551, 611))
        self.logi_container.setStyleSheet(u"")
        self.logi_container.setFrameShape(QFrame.StyledPanel)
        self.logi_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.logi_container)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.logi_container)
        self.logo.setObjectName(u"logo")
        self.logo.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.logo)

        self.frame = QFrame(self.logi_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.username = QLineEdit(self.frame_2)
        self.username.setObjectName(u"username")
        self.username.setMinimumSize(QSize(0, 40))
        font = QFont()
        font.setFamily(u"Nimbus Sans L")
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setStyleSheet(u"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,255);\n"
"color: rgb(120, 120, 120);")

        self.horizontalLayout_2.addWidget(self.username)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.password = QLineEdit(self.frame_3)
        self.password.setObjectName(u"password")
        self.password.setMinimumSize(QSize(0, 40))
        self.password.setFont(font)
        self.password.setStyleSheet(u"border: 1px solid rgba(0,0,0,0);\n"
"border-bottom-color: rgba(46,82,101,255);\n"
"color: rgb(120, 120, 120);\n"
"")

        self.horizontalLayout_3.addWidget(self.password)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"color: rgb(255, 3, 62);")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 0, 68);")

        self.verticalLayout_3.addWidget(self.label)

        self.loginBtn = QPushButton(self.frame_4)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setFamily(u"Nimbus Sans L")
        font1.setPointSize(18)
        font1.setBold(False)
        font1.setWeight(50)
        self.loginBtn.setFont(font1)
        self.loginBtn.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(24, 66, 255);")

        self.verticalLayout_3.addWidget(self.loginBtn)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.logo.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("Login", u"Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("Login", u"Password", None))
        self.label.setText("")
        self.loginBtn.setText(QCoreApplication.translate("Login", u"LOGIN", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacezAQMSo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 639)
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #ffffff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #040f13;\n"
"}\n"
"#header{\n"
"background-color: #040f13;\n"
"}\n"
"#side_menu{\n"
"	background-color: #071e26;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"QComboBox{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"\n"
"}\n"
"#main_body{\n"
"	background-color: #071e26;\n"
"	border-radius: 10px;\n"
"}\n"
"#pushButton_view{\n"
"	text-align: left;\n"
"}\n"
"#pushButton_contact{\n"
"	text-align: left;\n"
"}\n"
"#pushButton_config{\n"
"	text-align: left;\n"
"}\n"
"#comboBox{\n"
"	text-align: left;\n"
"}\n"
"#pushButton_xmdt{\n"
"	text-align: left;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1021, 639))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.header.sizePolicy().hasHeightForWidth())
        self.header.setSizePolicy(sizePolicy)
        self.header.setMinimumSize(QSize(0, 60))
        self.header.setMaximumSize(QSize(16777215, 60))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.frame_3)
        self.menuButton.setObjectName(u"menuButton")
        self.menuButton.setMinimumSize(QSize(0, 30))
        self.menuButton.setMaximumSize(QSize(16777215, 50))
        self.menuButton.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Ubuntu Condensed\";")
        self.menuButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.menuButton)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_5 = QFrame(self.header)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 10, 71, 21))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 10, 121, 21))

        self.horizontalLayout_2.addWidget(self.frame_5)


        self.verticalLayout.addWidget(self.header)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.main_body = QFrame(self.frame_2)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.main_body)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.side_menu = QCustomSlideMenu(self.main_body)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setMinimumSize(QSize(200, 0))
        self.side_menu.setLayoutDirection(Qt.LeftToRight)
        self.vboxLayout = QVBoxLayout(self.side_menu)
        self.vboxLayout.setSpacing(6)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.side_menu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_9 = QFrame(self.frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.toolBox_3 = QToolBox(self.frame_9)
        self.toolBox_3.setObjectName(u"toolBox_3")
        sizePolicy.setHeightForWidth(self.toolBox_3.sizePolicy().hasHeightForWidth())
        self.toolBox_3.setSizePolicy(sizePolicy)
        self.toolBox_3.setMinimumSize(QSize(200, 40))
        self.toolBox_3.setMaximumSize(QSize(200, 16777215))
        self.toolBox_3.setStyleSheet(u"QToolBox{\n"
"icon-size: 32px;\n"
"border-top:5px;\n"
"background-color: #071e26;\n"
"border-top:15px;\n"
"}\n"
"QToolBox::tab{\n"
"icon-size: 32px;\n"
"border-top:15px;\n"
"background-color: #040f13;\n"
"}")
        self.menu_view_2 = QWidget()
        self.menu_view_2.setObjectName(u"menu_view_2")
        self.menu_view_2.setGeometry(QRect(0, 0, 200, 68))
        icon = QIcon()
        icon.addFile(u":/icons/icons/analysis.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_3.addItem(self.menu_view_2, icon, u"Hi\u1ec3n th\u1ecb")
        self.menu_function_2 = QWidget()
        self.menu_function_2.setObjectName(u"menu_function_2")
        self.menu_function_2.setGeometry(QRect(0, 0, 200, 68))
        self.verticalLayout_7 = QVBoxLayout(self.menu_function_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.button_function = QPushButton(self.menu_function_2)
        self.button_function.setObjectName(u"button_function")
        self.button_function.setMaximumSize(QSize(16777215, 40))
        self.button_function.setStyleSheet(u"text-align: left;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/otp.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_function.setIcon(icon1)
        self.button_function.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.button_function)

        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/project-management.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_3.addItem(self.menu_function_2, icon2, u"Ch\u1ee9c n\u0103ng ch\u00ednh")
        self.menu_config_2 = QWidget()
        self.menu_config_2.setObjectName(u"menu_config_2")
        self.menu_config_2.setGeometry(QRect(0, 0, 200, 68))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/testing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_3.addItem(self.menu_config_2, icon3, u"C\u1ea5u h\u00ecnh h\u1ec7 th\u1ed1ng")
        self.menu_contact = QWidget()
        self.menu_contact.setObjectName(u"menu_contact")
        self.menu_contact.setGeometry(QRect(0, 0, 200, 68))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/contacts.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox_3.addItem(self.menu_contact, icon4, u"Li\u00ean h\u1ec7")

        self.verticalLayout_5.addWidget(self.toolBox_3, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame_9)


        self.vboxLayout.addWidget(self.frame, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.side_menu, 0, Qt.AlignLeft|Qt.AlignTop)

        self.content = QFrame(self.main_body)
        self.content.setObjectName(u"content")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy1)
        self.content.setStyleSheet(u"")
        self.content.setFrameShape(QFrame.StyledPanel)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.content)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.frame_4 = QFrame(self.content)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"\n"
"background-color: rgb(4, 15, 19);")
        self.page_view = QWidget()
        self.page_view.setObjectName(u"page_view")
        self.verticalLayout_4 = QVBoxLayout(self.page_view)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_11 = QFrame(self.page_view)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 200))
        self.frame_11.setMaximumSize(QSize(16777215, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.start_button = QPushButton(self.frame_11)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(30, 70, 201, 40))
        self.start_button.setMinimumSize(QSize(0, 40))
        self.start_button.setStyleSheet(u"background-color: rgb(85, 0, 255);\n"
"\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.start_button.setIcon(icon5)
        self.start_button.setIconSize(QSize(24, 24))
        self.stop_button = QPushButton(self.frame_11)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(240, 70, 201, 40))
        self.stop_button.setMinimumSize(QSize(0, 40))
        self.stop_button.setStyleSheet(u"background-color: rgb(255, 99, 102);\n"
"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_button.setIcon(icon6)
        self.stop_button.setIconSize(QSize(24, 24))
        self.pushButton_3 = QPushButton(self.frame_11)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 20, 131, 41))
        self.pushButton_3.setStyleSheet(u"text-align: left;")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/calendar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon7)
        self.pushButton_3.setIconSize(QSize(24, 24))
        self.pushButton_4 = QPushButton(self.frame_11)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(230, 20, 91, 41))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/clock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon8)
        self.pushButton_4.setIconSize(QSize(24, 24))
        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(590, 0, 130, 62))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_12)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon9)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.pushButton_5)

        self.label_3 = QLabel(self.frame_12)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.frame_13 = QFrame(self.frame_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(590, 60, 130, 62))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, -1, 0)
        self.pushButton_6 = QPushButton(self.frame_13)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon10)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.pushButton_6)

        self.label_8 = QLabel(self.frame_13)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.num_threads = QSpinBox(self.frame_11)
        self.num_threads.setObjectName(u"num_threads")
        self.num_threads.setGeometry(QRect(150, 20, 81, 40))
        self.num_threads.setMinimumSize(QSize(20, 40))
        self.num_threads.setMaximumSize(QSize(150, 16777215))
        self.num_threads.setSizeIncrement(QSize(0, 40))
        self.num_threads.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.num_threads.setMaximum(999)
        self.num_threads.setValue(2)
        self.delay_time = QSpinBox(self.frame_11)
        self.delay_time.setObjectName(u"delay_time")
        self.delay_time.setGeometry(QRect(360, 20, 81, 40))
        self.delay_time.setMinimumSize(QSize(20, 40))
        self.delay_time.setMaximumSize(QSize(150, 16777215))
        self.delay_time.setSizeIncrement(QSize(0, 40))
        self.delay_time.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.delay_time.setMaximum(999999999)
        self.delay_time.setValue(200)

        self.verticalLayout_4.addWidget(self.frame_11)

        self.tableWidget = QTableWidget(self.page_view)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.tableWidget.rowCount() < 3):
            self.tableWidget.setRowCount(3)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setMinimumSize(QSize(0, 300))
        self.tableWidget.setStyleSheet(u"background-color: rgb(46, 52, 54);")

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.stackedWidget.addWidget(self.page_view)
        self.page_config = QWidget()
        self.page_config.setObjectName(u"page_config")
        self.frame_7 = QFrame(self.page_config)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 10, 751, 511))
        self.frame_7.setStyleSheet(u"background-color: rgb(4, 15, 19);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.comboBox_20 = QComboBox(self.frame_7)
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.addItem("")
        self.comboBox_20.setObjectName(u"comboBox_20")
        self.comboBox_20.setGeometry(QRect(432, 16, 301, 40))
        self.comboBox_20.setMinimumSize(QSize(0, 40))
        self.comboBox_20.setMaximumSize(QSize(16777215, 40))
        self.comboBox_20.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.label_24 = QLabel(self.frame_7)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(392, 10, 50, 53))
        self.label_24.setMinimumSize(QSize(40, 0))
        self.label_24.setMaximumSize(QSize(50, 16777215))
        self.comboBox_19 = QComboBox(self.frame_7)
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.addItem("")
        self.comboBox_19.setObjectName(u"comboBox_19")
        self.comboBox_19.setGeometry(QRect(36, 16, 350, 40))
        self.comboBox_19.setMinimumSize(QSize(350, 40))
        self.comboBox_19.setMaximumSize(QSize(350, 40))
        self.comboBox_19.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.label_23 = QLabel(self.frame_7)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(10, 10, 20, 53))
        self.label_23.setMinimumSize(QSize(20, 0))
        self.label_23.setMaximumSize(QSize(20, 16777215))
        self.stackedWidget.addWidget(self.page_config)
        self.page_function = QWidget()
        self.page_function.setObjectName(u"page_function")
        self.page_function.setStyleSheet(u"background-color: rgb(4, 15, 19);")
        self.frame_6 = QFrame(self.page_function)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 751, 521))
        self.frame_6.setMinimumSize(QSize(0, 30))
        self.frame_6.setSizeIncrement(QSize(30, 0))
        self.frame_6.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 180, 67, 17))
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 230, 67, 17))
        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 280, 81, 17))
        self.comboBox_8 = QComboBox(self.frame_6)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setGeometry(QRect(110, 170, 381, 40))
        self.comboBox_8.setMinimumSize(QSize(0, 40))
        self.comboBox_8.setMaximumSize(QSize(16777215, 40))
        self.comboBox_8.setSizeIncrement(QSize(0, 0))
        self.comboBox_8.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.comboBox_9 = QComboBox(self.frame_6)
        self.comboBox_9.addItem("")
        self.comboBox_9.setObjectName(u"comboBox_9")
        self.comboBox_9.setGeometry(QRect(110, 220, 131, 40))
        self.comboBox_9.setMinimumSize(QSize(0, 40))
        self.comboBox_9.setMaximumSize(QSize(16777215, 40))
        self.comboBox_9.setSizeIncrement(QSize(0, 0))
        self.comboBox_9.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.radioButton_7 = QRadioButton(self.frame_6)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setGeometry(QRect(90, 280, 151, 16))
        self.radioButton_7.setStyleSheet(u"selection-color: rgb(138, 226, 52);")
        self.comboBox_14 = QComboBox(self.frame_6)
        self.comboBox_14.addItem("")
        self.comboBox_14.addItem("")
        self.comboBox_14.setObjectName(u"comboBox_14")
        self.comboBox_14.setGeometry(QRect(500, 170, 241, 40))
        self.comboBox_14.setMinimumSize(QSize(0, 40))
        self.comboBox_14.setMaximumSize(QSize(16777215, 40))
        self.comboBox_14.setSizeIncrement(QSize(0, 0))
        self.comboBox_14.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(10, 330, 81, 17))
        self.comboBox_15 = QComboBox(self.frame_6)
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.setObjectName(u"comboBox_15")
        self.comboBox_15.setGeometry(QRect(110, 320, 631, 40))
        self.comboBox_15.setMinimumSize(QSize(0, 40))
        self.comboBox_15.setMaximumSize(QSize(16777215, 40))
        self.comboBox_15.setSizeIncrement(QSize(30, 0))
        self.comboBox_15.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.label_16 = QLabel(self.frame_6)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(250, 230, 31, 17))
        self.label_17 = QLabel(self.frame_6)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 380, 81, 17))
        self.radioButton_8 = QRadioButton(self.frame_6)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setGeometry(QRect(240, 280, 101, 23))
        self.radioButton_9 = QRadioButton(self.frame_6)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setGeometry(QRect(340, 280, 81, 23))
        self.radioButton_10 = QRadioButton(self.frame_6)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setGeometry(QRect(420, 280, 121, 23))
        self.radioButton_10.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.radioButton_11 = QRadioButton(self.frame_6)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setGeometry(QRect(540, 280, 121, 23))
        self.radioButton_12 = QRadioButton(self.frame_6)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setGeometry(QRect(660, 280, 91, 23))
        self.label_18 = QLabel(self.frame_6)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 430, 81, 17))
        self.label_19 = QLabel(self.frame_6)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(10, 480, 81, 17))
        self.comboBox_16 = QComboBox(self.frame_6)
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.addItem("")
        self.comboBox_16.setObjectName(u"comboBox_16")
        self.comboBox_16.setGeometry(QRect(110, 470, 631, 40))
        self.comboBox_16.setMinimumSize(QSize(0, 40))
        self.comboBox_16.setMaximumSize(QSize(16777215, 40))
        self.comboBox_16.setSizeIncrement(QSize(0, 0))
        self.comboBox_16.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.textEdit_4 = QTextEdit(self.frame_6)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(110, 260, 0, 30))
        self.textEdit_4.setMinimumSize(QSize(0, 30))
        self.textEdit_4.setMaximumSize(QSize(16777215, 30))
        self.textEdit_4.setSizeIncrement(QSize(0, 0))
        self.textEdit_7 = QTextEdit(self.frame_6)
        self.textEdit_7.setObjectName(u"textEdit_7")
        self.textEdit_7.setEnabled(False)
        self.textEdit_7.setGeometry(QRect(110, 370, 631, 40))
        self.textEdit_7.setMinimumSize(QSize(0, 40))
        self.textEdit_7.setMaximumSize(QSize(16777215, 40))
        self.textEdit_7.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.textEdit_8 = QTextEdit(self.frame_6)
        self.textEdit_8.setObjectName(u"textEdit_8")
        self.textEdit_8.setEnabled(False)
        self.textEdit_8.setGeometry(QRect(290, 220, 451, 40))
        self.textEdit_8.setMinimumSize(QSize(0, 40))
        self.textEdit_8.setMaximumSize(QSize(16777215, 40))
        self.textEdit_8.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"")
        self.comboBox_6 = QComboBox(self.frame_6)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setGeometry(QRect(500, 70, 241, 40))
        self.comboBox_6.setMinimumSize(QSize(0, 40))
        self.comboBox_6.setMaximumSize(QSize(16777215, 40))
        self.comboBox_6.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.comboBox_11 = QComboBox(self.frame_6)
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.setObjectName(u"comboBox_11")
        self.comboBox_11.setGeometry(QRect(110, 120, 381, 40))
        self.comboBox_11.setMinimumSize(QSize(0, 40))
        self.comboBox_11.setMaximumSize(QSize(16777215, 40))
        self.comboBox_11.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.label_21 = QLabel(self.frame_6)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(10, 130, 91, 17))
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 80, 81, 17))
        self.comboBox_7 = QComboBox(self.frame_6)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setGeometry(QRect(110, 20, 631, 40))
        self.comboBox_7.setMinimumSize(QSize(0, 40))
        self.comboBox_7.setMaximumSize(QSize(16777215, 40))
        self.comboBox_7.setStyleSheet(u"\n"
"background-color: rgb(46, 52, 54);\n"
"")
        self.comboBox_12 = QComboBox(self.frame_6)
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.setObjectName(u"comboBox_12")
        self.comboBox_12.setGeometry(QRect(110, 70, 381, 40))
        self.comboBox_12.setMinimumSize(QSize(0, 40))
        self.comboBox_12.setMaximumSize(QSize(16777215, 40))
        self.comboBox_12.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 30, 81, 17))
        self.comboBox_13 = QComboBox(self.frame_6)
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.setObjectName(u"comboBox_13")
        self.comboBox_13.setGeometry(QRect(500, 120, 241, 40))
        self.comboBox_13.setMinimumSize(QSize(0, 40))
        self.comboBox_13.setMaximumSize(QSize(16777215, 40))
        self.comboBox_13.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.BtnListMail = QPushButton(self.frame_6)
        self.BtnListMail.setObjectName(u"BtnListMail")
        self.BtnListMail.setGeometry(QRect(109, 420, 631, 40))
        self.BtnListMail.setMinimumSize(QSize(0, 40))
        self.BtnListMail.setMaximumSize(QSize(16777215, 40))
        self.BtnListMail.setStyleSheet(u"background-color: rgb(46, 52, 54);\n"
"text-align: left;")
        self.stackedWidget.addWidget(self.page_function)
        self.page_contact = QWidget()
        self.page_contact.setObjectName(u"page_contact")
        self.frame_8 = QFrame(self.page_contact)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(0, 0, 761, 521))
        self.frame_8.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(4, 15, 19);\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_10 = QFrame(self.frame_8)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.page_contact)

        self.verticalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout_5.addWidget(self.frame_4)


        self.horizontalLayout_3.addWidget(self.content)


        self.horizontalLayout.addWidget(self.main_body)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox_3.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HSD: V\u0129nh vi\u1ec5n", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.menu_view_2), QCoreApplication.translate("MainWindow", u"Hi\u1ec3n th\u1ecb", None))
        self.button_function.setText(QCoreApplication.translate("MainWindow", u"G\u1eedi XMDT", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.menu_function_2), QCoreApplication.translate("MainWindow", u"Ch\u1ee9c n\u0103ng ch\u00ednh", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.menu_config_2), QCoreApplication.translate("MainWindow", u"C\u1ea5u h\u00ecnh h\u1ec7 th\u1ed1ng", None))
        self.toolBox_3.setItemText(self.toolBox_3.indexOf(self.menu_contact), QCoreApplication.translate("MainWindow", u"Li\u00ean h\u1ec7", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"B\u1eaft \u0111\u1ea7u", None))
        self.stop_button.setText(QCoreApplication.translate("MainWindow", u"T\u1ea1m d\u1eebng", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Lu\u1ed3ng ch\u1ea1y", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Delay", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"T\u1ea5t c\u1ea3:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"62", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0110\u00e3 ch\u1ecdn", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"2", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"@T\u00e0i kho\u1ea3n[Id|Pw|2Fa ho\u1eb7c Cookie]", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"@Ip", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"@Limit", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"@Tr\u1ea1ng th\u00e1i", None));
        self.comboBox_20.setItemText(0, QCoreApplication.translate("MainWindow", u"https://m.facebook.com/", None))
        self.comboBox_20.setItemText(1, QCoreApplication.translate("MainWindow", u"https://mbasic.facebook.com/", None))
        self.comboBox_20.setItemText(2, QCoreApplication.translate("MainWindow", u"https://www.facebook.com/", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.comboBox_19.setItemText(0, QCoreApplication.translate("MainWindow", u"911", None))
        self.comboBox_19.setItemText(1, QCoreApplication.translate("MainWindow", u"Http", None))
        self.comboBox_19.setItemText(2, QCoreApplication.translate("MainWindow", u"Sock4", None))
        self.comboBox_19.setItemText(3, QCoreApplication.translate("MainWindow", u"Sock5", None))
        self.comboBox_19.setItemText(4, QCoreApplication.translate("MainWindow", u"None", None))
        self.comboBox_19.setItemText(5, QCoreApplication.translate("MainWindow", u"Proxy-Tinsoft", None))
        self.comboBox_19.setItemText(6, QCoreApplication.translate("MainWindow", u"Proxy-Tm", None))
        self.comboBox_19.setItemText(7, QCoreApplication.translate("MainWindow", u"Proxy-Minproxy", None))
        self.comboBox_19.setItemText(8, QCoreApplication.translate("MainWindow", u"Dcom", None))
        self.comboBox_19.setItemText(9, QCoreApplication.translate("MainWindow", u"Proxy-Shoplike", None))

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"IP:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Up Avatar:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Capcha:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"OTP Phone:", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"C\u00f3", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"Kh\u00f4ng", None))

        self.comboBox_9.setItemText(0, QCoreApplication.translate("MainWindow", u"Anycapcha", None))

        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Chothuesimcode", None))
        self.comboBox_14.setItemText(0, QCoreApplication.translate("MainWindow", u"2Captcha", None))
        self.comboBox_14.setItemText(1, QCoreApplication.translate("MainWindow", u"Anycaptcha", None))

        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nh\u00e0 m\u1ea1ng:", None))
        self.comboBox_15.setItemText(0, QCoreApplication.translate("MainWindow", u"Mobi", None))
        self.comboBox_15.setItemText(1, QCoreApplication.translate("MainWindow", u"Vina", None))
        self.comboBox_15.setItemText(2, QCoreApplication.translate("MainWindow", u"Viettel", None))
        self.comboBox_15.setItemText(3, QCoreApplication.translate("MainWindow", u"VNMB", None))
        self.comboBox_15.setItemText(4, QCoreApplication.translate("MainWindow", u"Itelecom", None))
        self.comboBox_15.setItemText(5, QCoreApplication.translate("MainWindow", u"T\u1ea5t c\u1ea3", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Key:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Key OTP:", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Viotp.com", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"Otpmm", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"Codetextnow", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"Tempsms.com", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"Primeotp", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"List mail:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Get s\u1ed1, mail:", None))
        self.comboBox_16.setItemText(0, QCoreApplication.translate("MainWindow", u"1 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_16.setItemText(1, QCoreApplication.translate("MainWindow", u"2 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_16.setItemText(2, QCoreApplication.translate("MainWindow", u"3 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_16.setItemText(3, QCoreApplication.translate("MainWindow", u"4 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))
        self.comboBox_16.setItemText(4, QCoreApplication.translate("MainWindow", u"5 l\u1ea7n khi Code OTP kh\u00f4ng v\u1ec1", None))

        self.textEdit_7.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; font-size:11pt;\"><br /></p></body></html>", None))
        self.textEdit_8.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; font-size:11pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Ubuntu'; font-size:11pt;\"><br /></p></body></html>", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"G\u1eedi 902 up ph\u00f4i", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"G\u1eedi 902 ch\u1ecdn d\u00f2ng(b\u1ecf qua b\u01b0\u1edbc up ph\u00f4i)", None))

        self.comboBox_11.setItemText(0, QCoreApplication.translate("MainWindow", u"T\u1ea3i online", None))
        self.comboBox_11.setItemText(1, QCoreApplication.translate("MainWindow", u"D\u00f9ng \u1ea3nh c\u00f3 s\u1eb5n", None))

        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u1ea2nh \u1edf ph\u00f4i", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn ph\u00f4i", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainWindow", u"XMDT th\u1eb3ng & 902", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"XMDT share 273", None))

        self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", u"L\u1ea5y ph\u00f4i \u1edf tool(C\u00f3 fake th\u00f4ng tin theo Via)", None))
        self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", u"T\u1ea3i l\u00ean ph\u00f4i(Ch\u1ec9nh s\u1eeda ph\u00f4i t\u1ef1 \u0111\u1ed9ng)", None))

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ki\u1ec3u XMDT", None))
        self.comboBox_13.setItemText(0, QCoreApplication.translate("MainWindow", u"1. Ph\u00f4i US", None))
        self.comboBox_13.setItemText(1, QCoreApplication.translate("MainWindow", u"2. Ph\u00f4i UK", None))
        self.comboBox_13.setItemText(2, QCoreApplication.translate("MainWindow", u"3. Ph\u00f4i Vi\u1ec7t Nam - CMND", None))
        self.comboBox_13.setItemText(3, QCoreApplication.translate("MainWindow", u"4. Ph\u00f4i Philippines", None))
        self.comboBox_13.setItemText(4, QCoreApplication.translate("MainWindow", u"5. Ph\u00f4i Thailand", None))
        self.comboBox_13.setItemText(5, QCoreApplication.translate("MainWindow", u"6. Ph\u00f4i Vi\u1ec7t Nam - B\u1eb1ng l\u00e1i A1", None))

        self.BtnListMail.setText(QCoreApplication.translate("MainWindow", u"Nh\u1eadp mail list", None))
    # retranslateUi


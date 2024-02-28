/********************************************************************************
** Form generated from reading UI file 'appHBvqHQ.ui'
**
** Created by: Qt User Interface Compiler version 5.12.8
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef APPHBVQHQ_H
#define APPHBVQHQ_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QWidget *header;
    QFrame *frame;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *pushButton;
    QLabel *label_14;
    QWidget *widget_2;
    QWidget *right_side;
    QFrame *frame_2;
    QTableWidget *tableWidget;
    QFrame *frame_5;
    QLabel *label_4;
    QLabel *label_5;
    QLabel *label_8;
    QComboBox *comboBox_6;
    QComboBox *comboBox_7;
    QRadioButton *radioButton;
    QComboBox *comboBox_11;
    QLabel *label_9;
    QComboBox *comboBox_12;
    QLabel *label_10;
    QLabel *label_11;
    QRadioButton *radioButton_2;
    QRadioButton *radioButton_3;
    QRadioButton *radioButton_4;
    QRadioButton *radioButton_5;
    QRadioButton *radioButton_6;
    QLabel *label_12;
    QLabel *label_13;
    QComboBox *comboBox_13;
    QTextEdit *textEdit;
    QTextEdit *textEdit_2;
    QTextEdit *textEdit_3;
    QFrame *frame_3;
    QLabel *label;
    QLabel *label_2;
    QLabel *label_3;
    QComboBox *comboBox;
    QComboBox *comboBox_2;
    QComboBox *comboBox_3;
    QComboBox *comboBox_4;
    QComboBox *comboBox_5;
    QFrame *frame_4;
    QHBoxLayout *horizontalLayout;
    QLabel *label_6;
    QComboBox *comboBox_8;
    QSpacerItem *horizontalSpacer;
    QLabel *label_7;
    QComboBox *comboBox_10;
    QWidget *left_side;
    QVBoxLayout *verticalLayout_3;
    QFrame *frame_left;
    QVBoxLayout *verticalLayout;
    QPushButton *btn_view;
    QPushButton *btn_func;
    QPushButton *btn_conf;
    QPushButton *btn_cont;
    QSpacerItem *verticalSpacer;
    QPushButton *btn_quit;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QString::fromUtf8("MainWindow"));
        MainWindow->resize(1115, 757);
        MainWindow->setAutoFillBackground(false);
        MainWindow->setStyleSheet(QString::fromUtf8("#MainWindow{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"#btn_conf {\n"
"	text-align: left;\n"
"}\n"
"#btn_view {\n"
"	text-align: left;\n"
"}\n"
"#btn_func {\n"
"	text-align: left;\n"
"}\n"
"#btn_cont {\n"
"	text-align: left;\n"
"}\n"
"#btn_quit {\n"
"	text-align: left;\n"
"}\n"
""));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QString::fromUtf8("centralwidget"));
        header = new QWidget(centralwidget);
        header->setObjectName(QString::fromUtf8("header"));
        header->setGeometry(QRect(0, 0, 1081, 61));
        header->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);\n"
"background-color: rgb(46, 52, 54);"));
        frame = new QFrame(header);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setGeometry(QRect(0, 0, 251, 58));
        frame->setStyleSheet(QString::fromUtf8("background-color: rgb(46, 52, 54);"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        horizontalLayout_2 = new QHBoxLayout(frame);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        pushButton = new QPushButton(frame);
        pushButton->setObjectName(QString::fromUtf8("pushButton"));
        pushButton->setStyleSheet(QString::fromUtf8("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);"));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/icons/icons/align-justify.svg"), QSize(), QIcon::Normal, QIcon::Off);
        pushButton->setIcon(icon);
        pushButton->setIconSize(QSize(32, 32));

        horizontalLayout_2->addWidget(pushButton);

        label_14 = new QLabel(frame);
        label_14->setObjectName(QString::fromUtf8("label_14"));

        horizontalLayout_2->addWidget(label_14);

        widget_2 = new QWidget(centralwidget);
        widget_2->setObjectName(QString::fromUtf8("widget_2"));
        widget_2->setGeometry(QRect(0, 60, 1101, 621));
        widget_2->setStyleSheet(QString::fromUtf8("background-color: rgb(52, 101, 164);"));
        right_side = new QWidget(widget_2);
        right_side->setObjectName(QString::fromUtf8("right_side"));
        right_side->setGeometry(QRect(250, 0, 831, 601));
        right_side->setStyleSheet(QString::fromUtf8("background-color: rgb(173, 127, 168);"));
        frame_2 = new QFrame(right_side);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        frame_2->setGeometry(QRect(-1, -1, 831, 601));
        frame_2->setStyleSheet(QString::fromUtf8("background-color: rgb(0, 0, 0);"));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        tableWidget = new QTableWidget(frame_2);
        if (tableWidget->columnCount() < 5)
            tableWidget->setColumnCount(5);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(3, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        tableWidget->setHorizontalHeaderItem(4, __qtablewidgetitem4);
        if (tableWidget->rowCount() < 3)
            tableWidget->setRowCount(3);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        tableWidget->setVerticalHeaderItem(0, __qtablewidgetitem5);
        QTableWidgetItem *__qtablewidgetitem6 = new QTableWidgetItem();
        tableWidget->setVerticalHeaderItem(1, __qtablewidgetitem6);
        QTableWidgetItem *__qtablewidgetitem7 = new QTableWidgetItem();
        tableWidget->setVerticalHeaderItem(2, __qtablewidgetitem7);
        tableWidget->setObjectName(QString::fromUtf8("tableWidget"));
        tableWidget->setGeometry(QRect(20, 20, 771, 121));
        tableWidget->setStyleSheet(QString::fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);"));
        tableWidget->setFrameShape(QFrame::StyledPanel);
        tableWidget->setFrameShadow(QFrame::Sunken);
        tableWidget->setLineWidth(0);
        tableWidget->setSizeAdjustPolicy(QAbstractScrollArea::AdjustIgnored);
        tableWidget->setSelectionBehavior(QAbstractItemView::SelectItems);
        tableWidget->horizontalHeader()->setVisible(true);
        tableWidget->horizontalHeader()->setCascadingSectionResizes(false);
        tableWidget->horizontalHeader()->setMinimumSectionSize(50);
        tableWidget->horizontalHeader()->setDefaultSectionSize(81);
        tableWidget->horizontalHeader()->setHighlightSections(false);
        tableWidget->horizontalHeader()->setStretchLastSection(false);
        tableWidget->verticalHeader()->setVisible(true);
        tableWidget->verticalHeader()->setStretchLastSection(false);
        frame_5 = new QFrame(frame_2);
        frame_5->setObjectName(QString::fromUtf8("frame_5"));
        frame_5->setGeometry(QRect(20, 150, 771, 231));
        frame_5->setStyleSheet(QString::fromUtf8("\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);"));
        frame_5->setFrameShape(QFrame::StyledPanel);
        frame_5->setFrameShadow(QFrame::Raised);
        label_4 = new QLabel(frame_5);
        label_4->setObjectName(QString::fromUtf8("label_4"));
        label_4->setGeometry(QRect(10, 20, 67, 17));
        label_5 = new QLabel(frame_5);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setGeometry(QRect(10, 50, 67, 17));
        label_8 = new QLabel(frame_5);
        label_8->setObjectName(QString::fromUtf8("label_8"));
        label_8->setGeometry(QRect(10, 80, 81, 17));
        comboBox_6 = new QComboBox(frame_5);
        comboBox_6->addItem(QString());
        comboBox_6->setObjectName(QString::fromUtf8("comboBox_6"));
        comboBox_6->setGeometry(QRect(110, 20, 441, 25));
        comboBox_7 = new QComboBox(frame_5);
        comboBox_7->addItem(QString());
        comboBox_7->setObjectName(QString::fromUtf8("comboBox_7"));
        comboBox_7->setGeometry(QRect(110, 50, 131, 25));
        radioButton = new QRadioButton(frame_5);
        radioButton->setObjectName(QString::fromUtf8("radioButton"));
        radioButton->setGeometry(QRect(110, 80, 151, 23));
        radioButton->setStyleSheet(QString::fromUtf8("selection-color: rgb(138, 226, 52);"));
        comboBox_11 = new QComboBox(frame_5);
        comboBox_11->addItem(QString());
        comboBox_11->setObjectName(QString::fromUtf8("comboBox_11"));
        comboBox_11->setGeometry(QRect(560, 20, 191, 25));
        label_9 = new QLabel(frame_5);
        label_9->setObjectName(QString::fromUtf8("label_9"));
        label_9->setGeometry(QRect(10, 110, 81, 17));
        comboBox_12 = new QComboBox(frame_5);
        comboBox_12->addItem(QString());
        comboBox_12->setObjectName(QString::fromUtf8("comboBox_12"));
        comboBox_12->setGeometry(QRect(110, 110, 641, 25));
        label_10 = new QLabel(frame_5);
        label_10->setObjectName(QString::fromUtf8("label_10"));
        label_10->setGeometry(QRect(260, 50, 67, 17));
        label_11 = new QLabel(frame_5);
        label_11->setObjectName(QString::fromUtf8("label_11"));
        label_11->setGeometry(QRect(10, 140, 81, 17));
        radioButton_2 = new QRadioButton(frame_5);
        radioButton_2->setObjectName(QString::fromUtf8("radioButton_2"));
        radioButton_2->setGeometry(QRect(260, 80, 101, 23));
        radioButton_3 = new QRadioButton(frame_5);
        radioButton_3->setObjectName(QString::fromUtf8("radioButton_3"));
        radioButton_3->setGeometry(QRect(360, 80, 81, 23));
        radioButton_4 = new QRadioButton(frame_5);
        radioButton_4->setObjectName(QString::fromUtf8("radioButton_4"));
        radioButton_4->setGeometry(QRect(440, 80, 121, 23));
        radioButton_5 = new QRadioButton(frame_5);
        radioButton_5->setObjectName(QString::fromUtf8("radioButton_5"));
        radioButton_5->setGeometry(QRect(560, 80, 121, 23));
        radioButton_6 = new QRadioButton(frame_5);
        radioButton_6->setObjectName(QString::fromUtf8("radioButton_6"));
        radioButton_6->setGeometry(QRect(680, 80, 121, 23));
        label_12 = new QLabel(frame_5);
        label_12->setObjectName(QString::fromUtf8("label_12"));
        label_12->setGeometry(QRect(10, 170, 81, 17));
        label_13 = new QLabel(frame_5);
        label_13->setObjectName(QString::fromUtf8("label_13"));
        label_13->setGeometry(QRect(10, 200, 81, 17));
        comboBox_13 = new QComboBox(frame_5);
        comboBox_13->addItem(QString());
        comboBox_13->setObjectName(QString::fromUtf8("comboBox_13"));
        comboBox_13->setGeometry(QRect(110, 200, 641, 25));
        textEdit = new QTextEdit(frame_5);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));
        textEdit->setGeometry(QRect(110, 140, 641, 21));
        textEdit_2 = new QTextEdit(frame_5);
        textEdit_2->setObjectName(QString::fromUtf8("textEdit_2"));
        textEdit_2->setEnabled(false);
        textEdit_2->setGeometry(QRect(110, 170, 641, 21));
        textEdit_3 = new QTextEdit(frame_5);
        textEdit_3->setObjectName(QString::fromUtf8("textEdit_3"));
        textEdit_3->setGeometry(QRect(300, 50, 451, 21));
        frame_3 = new QFrame(frame_2);
        frame_3->setObjectName(QString::fromUtf8("frame_3"));
        frame_3->setGeometry(QRect(20, 390, 771, 121));
        frame_3->setStyleSheet(QString::fromUtf8("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);"));
        frame_3->setFrameShape(QFrame::StyledPanel);
        frame_3->setFrameShadow(QFrame::Raised);
        label = new QLabel(frame_3);
        label->setObjectName(QString::fromUtf8("label"));
        label->setGeometry(QRect(10, 20, 81, 17));
        label_2 = new QLabel(frame_3);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setGeometry(QRect(10, 50, 81, 17));
        label_3 = new QLabel(frame_3);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setGeometry(QRect(10, 80, 91, 17));
        comboBox = new QComboBox(frame_3);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));
        comboBox->setGeometry(QRect(100, 10, 431, 25));
        comboBox_2 = new QComboBox(frame_3);
        comboBox_2->setObjectName(QString::fromUtf8("comboBox_2"));
        comboBox_2->setGeometry(QRect(100, 40, 431, 25));
        comboBox_3 = new QComboBox(frame_3);
        comboBox_3->setObjectName(QString::fromUtf8("comboBox_3"));
        comboBox_3->setGeometry(QRect(100, 70, 431, 25));
        comboBox_4 = new QComboBox(frame_3);
        comboBox_4->addItem(QString());
        comboBox_4->setObjectName(QString::fromUtf8("comboBox_4"));
        comboBox_4->setGeometry(QRect(540, 40, 211, 25));
        comboBox_5 = new QComboBox(frame_3);
        comboBox_5->addItem(QString());
        comboBox_5->setObjectName(QString::fromUtf8("comboBox_5"));
        comboBox_5->setGeometry(QRect(540, 70, 211, 25));
        frame_4 = new QFrame(frame_2);
        frame_4->setObjectName(QString::fromUtf8("frame_4"));
        frame_4->setGeometry(QRect(20, 520, 771, 45));
        frame_4->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(46, 52, 54);"));
        frame_4->setFrameShape(QFrame::StyledPanel);
        frame_4->setFrameShadow(QFrame::Raised);
        horizontalLayout = new QHBoxLayout(frame_4);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        label_6 = new QLabel(frame_4);
        label_6->setObjectName(QString::fromUtf8("label_6"));

        horizontalLayout->addWidget(label_6);

        comboBox_8 = new QComboBox(frame_4);
        comboBox_8->addItem(QString());
        comboBox_8->setObjectName(QString::fromUtf8("comboBox_8"));
        comboBox_8->setMinimumSize(QSize(66, 25));
        comboBox_8->setMaximumSize(QSize(66, 25));

        horizontalLayout->addWidget(comboBox_8);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        label_7 = new QLabel(frame_4);
        label_7->setObjectName(QString::fromUtf8("label_7"));

        horizontalLayout->addWidget(label_7);

        comboBox_10 = new QComboBox(frame_4);
        comboBox_10->addItem(QString());
        comboBox_10->setObjectName(QString::fromUtf8("comboBox_10"));

        horizontalLayout->addWidget(comboBox_10);

        left_side = new QWidget(widget_2);
        left_side->setObjectName(QString::fromUtf8("left_side"));
        left_side->setGeometry(QRect(0, 0, 251, 601));
        left_side->setStyleSheet(QString::fromUtf8("background-color: rgb(173, 127, 168);"));
        verticalLayout_3 = new QVBoxLayout(left_side);
        verticalLayout_3->setSpacing(9);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(0, 0, 0, 0);
        frame_left = new QFrame(left_side);
        frame_left->setObjectName(QString::fromUtf8("frame_left"));
        frame_left->setAutoFillBackground(false);
        frame_left->setStyleSheet(QString::fromUtf8("background-color: rgb(46, 52, 54);\n"
"color: rgb(255, 255, 255);"));
        frame_left->setFrameShape(QFrame::StyledPanel);
        frame_left->setFrameShadow(QFrame::Raised);
        verticalLayout = new QVBoxLayout(frame_left);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        btn_view = new QPushButton(frame_left);
        btn_view->setObjectName(QString::fromUtf8("btn_view"));
        QSizePolicy sizePolicy(QSizePolicy::Minimum, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(btn_view->sizePolicy().hasHeightForWidth());
        btn_view->setSizePolicy(sizePolicy);
        btn_view->setBaseSize(QSize(0, 0));
        QFont font;
        font.setFamily(QString::fromUtf8("Waree"));
        font.setBold(false);
        font.setItalic(false);
        font.setWeight(50);
        font.setStrikeOut(false);
        btn_view->setFont(font);
        btn_view->setStyleSheet(QString::fromUtf8("selection-color: rgb(85, 87, 83);\n"
"background-color: rgb(46, 52, 54);"));
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/icons/icons/analysis.png"), QSize(), QIcon::Normal, QIcon::Off);
        btn_view->setIcon(icon1);
        btn_view->setIconSize(QSize(32, 32));

        verticalLayout->addWidget(btn_view);

        btn_func = new QPushButton(frame_left);
        btn_func->setObjectName(QString::fromUtf8("btn_func"));
        QFont font1;
        font1.setFamily(QString::fromUtf8("Waree"));
        font1.setPointSize(11);
        btn_func->setFont(font1);
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/icons/icons/project-management.png"), QSize(), QIcon::Normal, QIcon::Off);
        btn_func->setIcon(icon2);
        btn_func->setIconSize(QSize(32, 32));

        verticalLayout->addWidget(btn_func);

        btn_conf = new QPushButton(frame_left);
        btn_conf->setObjectName(QString::fromUtf8("btn_conf"));
        QFont font2;
        font2.setFamily(QString::fromUtf8("Waree"));
        btn_conf->setFont(font2);
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/icons/icons/testing.png"), QSize(), QIcon::Normal, QIcon::Off);
        btn_conf->setIcon(icon3);
        btn_conf->setIconSize(QSize(32, 32));

        verticalLayout->addWidget(btn_conf);

        btn_cont = new QPushButton(frame_left);
        btn_cont->setObjectName(QString::fromUtf8("btn_cont"));
        btn_cont->setFont(font2);
        btn_cont->setLayoutDirection(Qt::LeftToRight);
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/icons/icons/contacts.png"), QSize(), QIcon::Normal, QIcon::Off);
        btn_cont->setIcon(icon4);
        btn_cont->setIconSize(QSize(32, 32));

        verticalLayout->addWidget(btn_cont);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(verticalSpacer);

        btn_quit = new QPushButton(frame_left);
        btn_quit->setObjectName(QString::fromUtf8("btn_quit"));
        btn_quit->setFont(font2);
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/icons/icons/logout.png"), QSize(), QIcon::Normal, QIcon::Off);
        btn_quit->setIcon(icon5);
        btn_quit->setIconSize(QSize(32, 32));

        verticalLayout->addWidget(btn_quit);


        verticalLayout_3->addWidget(frame_left);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", nullptr));
        pushButton->setText(QString());
        label_14->setText(QApplication::translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">MyLogoApp</span></p></body></html>", nullptr));
        QTableWidgetItem *___qtablewidgetitem = tableWidget->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("MainWindow", "#", nullptr));
        QTableWidgetItem *___qtablewidgetitem1 = tableWidget->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("MainWindow", "@T\303\240i kho\341\272\243n[Id|Pw|2Fa ho\341\272\267c Cookie]", nullptr));
        QTableWidgetItem *___qtablewidgetitem2 = tableWidget->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QApplication::translate("MainWindow", "@IP", nullptr));
        QTableWidgetItem *___qtablewidgetitem3 = tableWidget->horizontalHeaderItem(3);
        ___qtablewidgetitem3->setText(QApplication::translate("MainWindow", "@Limit", nullptr));
        QTableWidgetItem *___qtablewidgetitem4 = tableWidget->horizontalHeaderItem(4);
        ___qtablewidgetitem4->setText(QApplication::translate("MainWindow", "@Tr\341\272\241ng th\303\241i", nullptr));
        QTableWidgetItem *___qtablewidgetitem5 = tableWidget->verticalHeaderItem(0);
        ___qtablewidgetitem5->setText(QApplication::translate("MainWindow", "1", nullptr));
        QTableWidgetItem *___qtablewidgetitem6 = tableWidget->verticalHeaderItem(1);
        ___qtablewidgetitem6->setText(QApplication::translate("MainWindow", "2", nullptr));
        QTableWidgetItem *___qtablewidgetitem7 = tableWidget->verticalHeaderItem(2);
        ___qtablewidgetitem7->setText(QApplication::translate("MainWindow", "3", nullptr));
        label_4->setText(QApplication::translate("MainWindow", "Up Avatar:", nullptr));
        label_5->setText(QApplication::translate("MainWindow", "Capcha:", nullptr));
        label_8->setText(QApplication::translate("MainWindow", "OTP Phone:", nullptr));
        comboBox_6->setItemText(0, QApplication::translate("MainWindow", "C\303\263", nullptr));

        comboBox_7->setItemText(0, QApplication::translate("MainWindow", "Anycapcha", nullptr));

        radioButton->setText(QApplication::translate("MainWindow", "Chothuesimcode", nullptr));
        comboBox_11->setItemText(0, QApplication::translate("MainWindow", "Capcha Text", nullptr));

        label_9->setText(QApplication::translate("MainWindow", "Nh\303\240 m\341\272\241ng:", nullptr));
        comboBox_12->setItemText(0, QApplication::translate("MainWindow", "T\341\272\245t c\341\272\243", nullptr));

        label_10->setText(QApplication::translate("MainWindow", "Key:", nullptr));
        label_11->setText(QApplication::translate("MainWindow", "Key OTP:", nullptr));
        radioButton_2->setText(QApplication::translate("MainWindow", "Viotp.com", nullptr));
        radioButton_3->setText(QApplication::translate("MainWindow", "Otpmm", nullptr));
        radioButton_4->setText(QApplication::translate("MainWindow", "Codetextnow", nullptr));
        radioButton_5->setText(QApplication::translate("MainWindow", "Tempsms.com", nullptr));
        radioButton_6->setText(QApplication::translate("MainWindow", "Primeotp", nullptr));
        label_12->setText(QApplication::translate("MainWindow", "List mail:", nullptr));
        label_13->setText(QApplication::translate("MainWindow", "Get s\341\273\221, mail:", nullptr));
        comboBox_13->setItemText(0, QApplication::translate("MainWindow", "3 l\341\272\247n khi Code OTP kh\303\264ng v\341\273\201", nullptr));

        textEdit_2->setHtml(QApplication::translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">M\341\273\237 list hotmail 1</p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", nullptr));
        label->setText(QApplication::translate("MainWindow", "Ki\341\273\203u XMDT", nullptr));
        label_2->setText(QApplication::translate("MainWindow", "Ch\341\273\215n ph\303\264i", nullptr));
        label_3->setText(QApplication::translate("MainWindow", "\341\272\242nh \341\273\237 ph\303\264i", nullptr));
        comboBox_4->setItemText(0, QApplication::translate("MainWindow", "G\341\273\255i 902 up ph\303\264i", nullptr));

        comboBox_5->setItemText(0, QApplication::translate("MainWindow", "6 [Ph\303\264i Vi\341\273\207t Nam, B\341\272\261ng l\303\241i A1]", nullptr));

        label_6->setText(QApplication::translate("MainWindow", "ID:", nullptr));
        comboBox_8->setItemText(0, QApplication::translate("MainWindow", "None", nullptr));

        label_7->setText(QApplication::translate("MainWindow", "Login", nullptr));
        comboBox_10->setItemText(0, QApplication::translate("MainWindow", "https://m.facebook.com/", nullptr));

#ifndef QT_NO_TOOLTIP
        btn_view->setToolTip(QApplication::translate("MainWindow", "btn_view", nullptr));
#endif // QT_NO_TOOLTIP
        btn_view->setText(QApplication::translate("MainWindow", "Hi\341\273\203n th\341\273\213", nullptr));
#ifndef QT_NO_TOOLTIP
        btn_func->setToolTip(QApplication::translate("MainWindow", "btn_func", nullptr));
#endif // QT_NO_TOOLTIP
        btn_func->setText(QApplication::translate("MainWindow", "Ch\341\273\251c n\304\203ng ch\303\255nh", nullptr));
#ifndef QT_NO_TOOLTIP
        btn_conf->setToolTip(QApplication::translate("MainWindow", "btn_conf", nullptr));
#endif // QT_NO_TOOLTIP
        btn_conf->setText(QApplication::translate("MainWindow", "C\341\272\245u h\303\254nh h\341\273\207 th\341\273\221ng", nullptr));
#ifndef QT_NO_TOOLTIP
        btn_cont->setToolTip(QApplication::translate("MainWindow", "btn_cont", nullptr));
#endif // QT_NO_TOOLTIP
        btn_cont->setText(QApplication::translate("MainWindow", "Li\303\252n h\341\273\207", nullptr));
#ifndef QT_NO_TOOLTIP
        btn_quit->setToolTip(QApplication::translate("MainWindow", "btn_quit", nullptr));
#endif // QT_NO_TOOLTIP
        btn_quit->setText(QApplication::translate("MainWindow", "Logout", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // APPHBVQHQ_H

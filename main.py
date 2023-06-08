from ui_interface import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
                            QInputDialog, QLineEdit,\
                            QFileDialog, QTableWidget, \
                            QTableWidgetItem, QMessageBox, \
                            QHeaderView, QStyle, QStyleOptionButton,QAction,  \
                            QCheckBox, QVBoxLayout, QMenu

from PyQt5.QtGui import QPainter, QPixmap, QFont, QFontDatabase, QTransform, QDesktopServices, QClipboard
from PyQt5.QtCore import Qt, QRect, QUrl
from Custom_Widgets.Widgets import *
from PyQt5 import QtWidgets
from functions import * 
from ui_upPhoiWindow import *
from upPhoiWindow import UpPhoiWindow
class MyHeader(QHeaderView):
    def __init__(self, orientation, parent=None):
        super().__init__(orientation, parent)
        self.isOn = False

    def setTableWidget(self, tableWidget):
        self.tableWidget = tableWidget

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super().paintSection(painter, rect, logicalIndex)
        painter.restore()
        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(5, 5, 15, 15)
            option.state = QStyle.State_On if self.isOn else QStyle.State_Off
            self.style().drawPrimitive(QStyle.PE_IndicatorCheckBox, option, painter)

    def mousePressEvent(self, event):
        if self.logicalIndexAt(event.pos()) == 0:
            self.isOn = not self.isOn
            self.update()
            super().mousePressEvent(event)

        if self.tableWidget and self.logicalIndexAt(event.pos()) == 0:
            for row in range(self.tableWidget.rowCount()):
                item = self.tableWidget.item(row, 0)
                if item:
                    item.setCheckState(Qt.Checked if self.isOn else Qt.Unchecked)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################
        # self.ui.pushButton_view.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_view))
        # self.ui.pushButton_config.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_config))
        # self.ui.pushButton_contact.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_contact))
        # self.ui.comboBox.currentIndexChanged.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_function))
        # self.ui.comboBox.activated.connect(self.activated)
        self.ui.toolBox_3.currentChanged.connect(self.menuChanged)
        self.ui.BtnListMail.clicked.connect(self.openFileDialog)
        self.data = []
        myHeader = MyHeader(Qt.Horizontal, self.ui.tableWidget)
        myHeader.setTableWidget(self.ui.tableWidget)
        self.ui.tableWidget.setHorizontalHeader(myHeader)
        self.ui.tableWidget.setColumnWidth(0, 30)
        self.ui.tableWidget.setColumnWidth(1, 300)
        self.ui.tableWidget.setColumnWidth(2, 100)
        self.ui.tableWidget.setColumnWidth(3, 100)
        self.ui.tableWidget.setColumnWidth(4, 150)
        # Add checkboxes to the table
        for row in range(self.ui.tableWidget.rowCount()):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            item2 = QTableWidgetItem(str(row + 1))
            self.ui.tableWidget.setVerticalHeaderItem(row, item2)
            self.ui.tableWidget.setItem(row, 0, item)

        self.ui.start_button.clicked.connect(self.start_generation)
        self.ui.stop_button.clicked.connect(self.stop_generation)
        self.ui.stop_button.setEnabled(False)
        self.generator_threads = []
        self.ui.comboBox_12.currentIndexChanged.connect(self.openUpPhoiWindow)
        self.show()

    def menuChanged(self):
        if self.ui.toolBox_3.currentIndex() == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_view)
        elif self.ui.toolBox_3.currentIndex() == 1:
            if self.ui.button_function.clicked:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_function)
        elif self.ui.toolBox_3.currentIndex() == 2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_config)
        elif self.ui.toolBox_3.currentIndex() == 3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_contact)

    def openFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, "Open File", "", "Text files (*.txt)")
        if fname:
            self.ui.BtnListMail.setText(str(fname).replace("Text files (*.txt)", "")[2:-6])
        return 0

    def openUpPhoiWindow(self):
        # self.window= QtWidgets.QMainWindow()
        self.window2 = UpPhoiWindow()
        # self.ui.setupUi(self.window)
        self.window2.show()
    def contextMenuEvent(self, event):
        menu = QMenu(self)

        paste_delete_action = QAction("Paste tài khoản [Xóa tài khoản cũ]", self)
        paste_delete_action.triggered.connect(self.pasteDeleteAccount)
        menu.addAction(paste_delete_action)

        paste_no_delete_action = QAction("Paste tài khoản [Không xóa tài khoản cũ]", self)
        paste_no_delete_action.triggered.connect(self.pasteNoDeleteAccount)
        menu.addAction(paste_no_delete_action)

        click_selected_account_action = QAction("Click vào tài khoản đã bôi đen", self)
        click_selected_account_action.triggered.connect(self.clickSelectedAccount)
        menu.addAction(click_selected_account_action)

        menu.setStyleSheet("QMenu { background-color: rgb(46, 52, 54); }"
                           "QMenu::item {   background-color: rgb(46, 52, 54); color: white; \
                                            padding: 4px solid rgb(46, 52, 54);\
                                            padding-left: 2px solid rgb(46, 52, 54);\
                                            border: 1px solid rgb(46, 52, 54); }"
                           "QMenu::item:selected { background-color: blue; }")

        menu.exec_(event.globalPos())
        event.accept()

    def pasteDeleteAccount(self):
        if self.ui.tableWidget.rowCount() > 0:
            # print(self.ui.tableWidget.rowCount())
            self.ui.tableWidget.clearContents()

        clipboard = QApplication.clipboard()
        clipboard_texts = clipboard.text().split("\n")
        self.ui.tableWidget.setRowCount(len(clipboard_texts))
        for item in clipboard_texts:
            self.data.append(item)
        if len(self.data) > 0:
            for row, item in enumerate(self.data):
                table_item = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, 1, table_item)


    def pasteNoDeleteAccount(self):
        if self.ui.tableWidget.rowCount() > 0:
            start_row = self.ui.tableWidget.rowCount()  
        clipboard = QApplication.clipboard()
        clipboard_texts = clipboard.text().split("\n")
        self.ui.tableWidget.setRowCount(start_row + len(clipboard_texts))
        for item in clipboard_texts:
            self.data.append(item)
        if len(self.data) > 0:
            for row, item in enumerate(self.data):
                table_item = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(start_row, 1, table_item)

    def clickSelectedAccount(self):
        # QMessageBox.information(self, "Custom Action", "Click vào tài khoản đã bôi đen clicked!")
        pass
    def start_generation(self):

        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setEnabled(True)
        self.num_threads = self.ui.num_threads.value()
        if self.num_threads > self.ui.tableWidget.rowCount():
            self.num_threads = self.ui.tableWidget.rowCount()
        for i in range(0, self.num_threads):
            self.ui.tableWidget.setItem(i, 4,  QTableWidgetItem(""))
        print(self.num_threads)
        for i in range(0, self.num_threads): 
            generator_thread = NumberGeneratorThread(i, i * 10 + 1, self.ui.delay_time.value())
            generator_thread.number_generated.connect(self.handle_number_generated)
            self.generator_threads.append(generator_thread)
            generator_thread.start()

    def stop_generation(self):
        self.ui.start_button.setEnabled(True)
        for generator_thread in self.generator_threads:
            generator_thread.requestInterruption()

    def handle_number_generated(self, number, thread_id):
        item = QTableWidgetItem()
        item.setText(str(number))
        self.ui.tableWidget.setItem(thread_id, 4, item)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # window = UpPhoiWindow()
    window.show()
    sys.exit(app.exec_())

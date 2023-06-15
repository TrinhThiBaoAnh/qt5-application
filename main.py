from ui_interface import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
                            QInputDialog, QLineEdit,\
                            QFileDialog, QTableWidget, \
                            QTableWidgetItem, QMessageBox, \
                            QHeaderView, QStyle, QStyleOptionButton,QAction,  \
                            QCheckBox, QVBoxLayout, QMenu,QDesktopWidget

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
        self.centerWindow()
        # Disable moving the window out of the screen boundaries
        self.setFixedSize(self.size())
        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        # loadJsonStyle(self, self.ui)
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
        self.count = 0
        self.ui.comboBox_12.currentIndexChanged.connect(self.openUpPhoiWindow)
        self.show()
    def centerWindow(self):
        # Get the screen's geometry
        screen = QDesktopWidget().screenGeometry()

        # Calculate the center point of the screen
        center_x = screen.width() // 2
        center_y = screen.height() // 2

        # Calculate the top-left position of the window
        window_x = center_x - self.width() // 2
        window_y = center_y - self.height() // 2

        # Set the window's position
        self.move(window_x, window_y)
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
        if  self.ui.comboBox_12.currentIndex() == 1:
            # self.window= QtWidgets.QMainWindow()
            self.window2 = UpPhoiWindow()
            # self.ui.setupUi(self.window)
            self.window2.show()
    def contextMenuEvent(self, event):
        # print("Coordinate",event.x(), event.y())
        if (event.y() >305 and event.y() <602 and event.x() >  260 and event.x() < 987):
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
    def get_checked_rows(self):
        # Retrieve checked rows
        checked_rows = []
        for row in range(self.ui.tableWidget.rowCount()):
            check_item = self.ui.tableWidget.item(row, 0)
            if check_item.checkState() == Qt.Checked:
                checked_rows.append(row)
        return checked_rows
    def pasteDeleteAccount(self):
        if self.ui.tableWidget.rowCount() > 0:
            # print(self.ui.tableWidget.rowCount())
            self.ui.tableWidget.clearContents()
            # Add checkboxes to the table
        clipboard = QApplication.clipboard()
        clipboard_texts = clipboard.text().split("\n")
        self.ui.tableWidget.setRowCount(len(clipboard_texts))
        for item in clipboard_texts:
            self.data.append(item)
        if len(self.data) > 0:
            for row, item in enumerate(self.data):
                table_item = QTableWidgetItem(item)
                self.ui.tableWidget.setItem(row, 1, table_item)
        for row in range(self.ui.tableWidget.rowCount()):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            item2 = QTableWidgetItem(str(row + 1))
            self.ui.tableWidget.setVerticalHeaderItem(row, item2)
            self.ui.tableWidget.setItem(row, 0, item)

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
        for row in range(self.ui.tableWidget.rowCount()):
            item = QTableWidgetItem()
            item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            item.setCheckState(Qt.Unchecked)
            item2 = QTableWidgetItem(str(row + 1))
            self.ui.tableWidget.setVerticalHeaderItem(row, item2)
            self.ui.tableWidget.setItem(row, 0, item)
    def clickSelectedAccount(self):
        # QMessageBox.information(self, "Custom Action", "Click vào tài khoản đã bôi đen clicked!")
        pass
    def start_generation(self):
        self.ui.start_button.setEnabled(False)
        self.ui.stop_button.setEnabled(True)
        self.clearRow()
        self.num_threads = self.ui.num_threads.value()
        self.delay_time = self.ui.delay_time.value()
        self.checked_rows = self.get_checked_rows()
        self.num_threads = min(len(self.checked_rows), self.num_threads)
        # Create threads
        for i in range(0, self.ui.tableWidget.rowCount()):  # Create 4 generator threads
            if i in self.checked_rows:
                generator_thread = NumberGeneratorThread(i, i * 10 + 1, self.delay_time)
                generator_thread.number_generated.connect(self.handle_number_generated)
                generator_thread.thread_finished.connect(self.handle_thread_finished)
                self.generator_threads.append(generator_thread)
        # print( "len(self.generator_threads): " , len(self.generator_threads))
        self.current_thread_index = 0
        self.run_next_threads()

    def run_next_threads(self):
        num_threads_to_run = min(len(self.generator_threads) - self.current_thread_index, self.num_threads)
        # import ipdb; ipdb.set_trace();
        if num_threads_to_run > 0:
            for i in range(num_threads_to_run):
                generator_thread = self.generator_threads[self.current_thread_index]
                generator_thread.start()
                # if i == num_threads_to_run-1:
                self.current_thread_index += 1

    def stop_generation(self):
        self.ui.start_button.setEnabled(True)
        for generator_thread in self.generator_threads:
            generator_thread.requestInterruption()

    def handle_number_generated(self, number, thread_id):
        # print(f"Thread {thread_id}: {number}")
        item = QTableWidgetItem()
        item.setText(str(number))
        self.ui.tableWidget.setItem(thread_id, 4, item)

    def handle_thread_finished(self, thread_id):
        print(f"Thread {thread_id} finished")
        # print('current_thread_index: ', self.current_thread_index)
        # import ipdb; ipdb.set_trace();
        if self.current_thread_index < len(self.generator_threads):
            if thread_id % self.num_threads==0:
                self.run_next_threads() 
        else:
            self.finish_generation()

    def finish_generation(self):
        self.ui.stop_button.setEnabled(False)
        self.ui.start_button.setEnabled(True)
        self.current_thread_index = 0

        for generator_thread in self.generator_threads:
            generator_thread.requestInterruption()
            generator_thread.quit()
            generator_thread.wait()
        self.generator_threads = []
        
        # self.start_generation()
        print("All threads finished")
    def clearRow(self):
        for row in range(self.ui.tableWidget.rowCount()):
            item = QTableWidgetItem("")
            self.ui.tableWidget.setItem(row, 4, item)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # window = UpPhoiWindow()
    window.show()
    sys.exit(app.exec_())

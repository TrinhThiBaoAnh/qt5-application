from ui_interface import *
import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
                            QInputDialog, QLineEdit,\
                            QFileDialog, QTableWidget, \
                            QTableWidgetItem, QMessageBox, \
                            QHeaderView, QStyle, QStyleOptionButton, \
                            QCheckBox, QVBoxLayout
from PyQt5.QtGui import QPainter, QPixmap, QFont, QFontDatabase, QTransform, QDesktopServices
from PyQt5.QtCore import Qt, QRect, QUrl
from Custom_Widgets.Widgets import *
from PyQt5 import QtWidgets

from ui_upPhoiWindow import *
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

# class ImageLabel(QLabel):
#     def __init__(self, image_path, parent=None):
#         super().__init__(parent)
#         original_image = QPixmap(image_path)
#         width = 591  # desired width
#         height = 361  # desired height
#         resized_image = original_image.scaled(width, height)
#         self.setPixmap(resized_image)
        
#     def mousePressEvent(self, event):
#         if event.buttons() == Qt.LeftButton:
#             x = event.x()
#             y = event.y()
#             print("Clicked coordinates: ({}, {})".format(x, y))
#             return x, y

class UpPhoiWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui  = Ui_UpPhoiWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.browser_images)
        # Get the list of available font families
        font_families = QFontDatabase().families()
        # Set the font families as items in the QComboBox
        self.ui.comboBox_3.addItems(font_families)
        for num in range(6, 96):
            self.ui.comboBox_2.addItem(str(num))
        self.ui.spinBox_11.setValue(170)
        self.ui.spinBox_12.setValue(480)

        self.ui.spinBox_17.setValue(150)
        self.ui.spinBox_18.setValue(210)

        self.ui.spinBox_14.setValue(70)
        self.ui.spinBox_15.setValue(210)

        self.ui.spinBox_20.setValue(120)
        self.ui.spinBox_21.setValue(210)

        self.ui.spinBox_23.setValue(210)
        self.ui.spinBox_25.setValue(100)
        self.ui.label_36.setText('<a href="https://www.youtube.com">Video hướng dẫn</a>')
        self.ui.label_36.setOpenExternalLinks(True)  # Allow opening the link in an external browser

        # Connect the link clicked signal to a slot
        self.ui.label_36.linkActivated.connect(lambda url: QDesktopServices.openUrl(QUrl(url)))

        self.show()
    def paint_images(self, background_image, foreground_image, 
                     givenname,surname,birthday,gender,address, 
                     img_x, img_y, img_width, img_height,
                     givenname_x, givenname_y, surname_x, surname_y,birthday_x, birthday_y,gender_x, gender_y, address_x, address_y,
                     font_family, is_bold, 
                     text_color, font_size):
        
        font = QFont()
        font.setFamily(font_family)
        font.setPointSize(font_size)
        font.setBold(is_bold)
        
        text_color = Qt.red

        self.ui.spinBox_3.setValue(img_x)
        self.ui.spinBox_4.setValue(img_y)

        width = 591  # desired width
        height = 361  # desired height
        background_image = background_image.scaled(width, height)
        foreground_image = foreground_image.scaled(img_width, img_height)
        self.ui.image_label.setPixmap(background_image)

        self.ui.spinBox.setValue(img_width)
        self.ui.spinBox_2.setValue(img_height)
        combined_image = QPixmap(background_image.size())
        combined_image.fill(Qt.transparent)

        # Draw the background image on the combined image
        painter = QPainter(combined_image)
        painter.drawPixmap(0, 0, background_image)
        painter.drawPixmap(img_x, img_y, foreground_image)
        painter.setFont(font)
        painter.setPen(text_color)
        # Set the rotation angles for the texts
        angle_givenname = self.ui.spinBox_24.value()
        angle_surname = self.ui.spinBox_16.value()
        angle_birthday = self.ui.spinBox_19.value()
        angle_gender = self.ui.spinBox_13.value()
        angle_address = self.ui.spinBox_22.value()

        # Create a transformation matrix for each rotation angle
        transform_1 = QTransform()
        transform_1.rotate(angle_givenname)

        transform_2 = QTransform()
        transform_2.rotate(angle_surname)

        transform_3 = QTransform()
        transform_3.rotate(angle_birthday)

        transform_4 = QTransform()
        transform_4.rotate(angle_gender)

        transform_5 = QTransform()
        transform_5.rotate(angle_address)

        # Apply the transformations to the painter for each text
        painter.setTransform(transform_1)
        painter.drawText(givenname_x, givenname_y, givenname)

        painter.setTransform(transform_2)
        painter.drawText(surname_x, surname_y, surname)

        painter.setTransform(transform_3)
        painter.drawText(birthday_x, birthday_y, birthday)

        painter.setTransform(transform_4)
        painter.drawText(gender_x, gender_y, gender)

        painter.setTransform(transform_5)
        painter.drawText(address_x, address_y, address)

        # painter.drawText(givenname_x, givenname_y, givenname)
        # painter.drawText(surname_x, surname_y, surname)
        # painter.drawText(birthday_x, birthday_y, birthday)
        # painter.drawText(gender_x, gender_y, gender)
        # painter.drawText(address_x, address_y, address)
        painter.end()

        self.ui.label_img.setPixmap(combined_image)
        self.ui.label_img.show()

    def browser_images(self):
        fname = QFileDialog.getOpenFileName(self, "Open Image","", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fname:
            img_path = str(fname).replace("Image Files (*.png *.jpg *.jpeg *.bmp)","")[2:-6]
            self.ui.textEdit.setText(img_path)
            self.background_image = QPixmap(img_path)
            self.foreground_image = QPixmap("demo/a.png")
            w = self.foreground_image.width()
            h = self.foreground_image.height()

            # current_index = self.ui.comboBox_2.currentIndex()
            font_size = self.ui.comboBox_2.currentText()

            # current_index = self.ui.comboBox_3.currentIndex()
            font_family = self.ui.comboBox_3.currentText()


            # current_index = self.ui.comboBox_4.currentIndex()

            is_bold = self.ui.comboBox_4.currentText()=="Bold"
            # current_index = self.ui.comboBox_4.currentIndex()
            text_color = self.ui.comboBox_4.currentText()
            self.givenname = "First Name"
            self.surname = "Last Name"
            self.birthday = "dd/mm/yyyy"
            self.gender = "Sex"
            self.address = "Address"
            givenname_x = self.ui.spinBox_23.value()
            givenname_y = self.ui.spinBox_25.value()

            surname_x = self.ui.spinBox_15.value()
            surname_y = self.ui.spinBox_14.value()

            birthday_x = self.ui.spinBox_18.value()
            birthday_y = self.ui.spinBox_17.value()

            gender_x = self.ui.spinBox_12.value()
            gender_y = self.ui.spinBox_11.value()

            address_x = self.ui.spinBox_21.value()
            address_y = self.ui.spinBox_20.value()

            self.paint_images(self.background_image, self.foreground_image, 
                              self.givenname,self.surname,self.birthday,self.gender,self.address,
                                img_x=100, img_y=100, 
                                img_width =w , img_height = h,
                                givenname_x = givenname_x, givenname_y= givenname_y, surname_x= surname_x, surname_y=surname_y,
                                birthday_x= birthday_x, birthday_y= birthday_y,gender_x= gender_x, gender_y= gender_y,
                                address_x=address_x, address_y= address_y,font_family=font_family, is_bold=True, 
                                text_color ="Black", font_size = int(font_size))
            self.ui.spinBox.valueChanged.connect(self.update)
            self.ui.spinBox_2.valueChanged.connect(self.update)
            self.ui.spinBox_3.valueChanged.connect(self.update)
            self.ui.spinBox_4.valueChanged.connect(self.update)

            self.ui.spinBox_23.valueChanged.connect(self.update)
            self.ui.spinBox_25.valueChanged.connect(self.update)

            self.ui.spinBox_15.valueChanged.connect(self.update)
            self.ui.spinBox_14.valueChanged.connect(self.update)
            
            self.ui.spinBox_18.valueChanged.connect(self.update)
            self.ui.spinBox_17.valueChanged.connect(self.update)

            self.ui.spinBox_12.valueChanged.connect(self.update)
            self.ui.spinBox_11.valueChanged.connect(self.update)

            self.ui.spinBox_21.valueChanged.connect(self.update)
            self.ui.spinBox_20.valueChanged.connect(self.update)

            self.ui.comboBox_2.currentIndexChanged.connect(self.update)
            self.ui.comboBox_3.currentIndexChanged.connect(self.update)

            self.ui.spinBox_24.valueChanged.connect(self.update)
            self.ui.spinBox_16.valueChanged.connect(self.update)
            self.ui.spinBox_19.valueChanged.connect(self.update)
            self.ui.spinBox_13.valueChanged.connect(self.update)
            self.ui.spinBox_22.valueChanged.connect(self.update)

        return 0
    def update(self):
        font_family = self.ui.comboBox_3.currentText()
        font_size = self.ui.comboBox_2.currentText()
        givenname_x = self.ui.spinBox_23.value()
        givenname_y = self.ui.spinBox_25.value()

        surname_x = self.ui.spinBox_15.value()
        surname_y = self.ui.spinBox_14.value()

        birthday_x = self.ui.spinBox_18.value()
        birthday_y = self.ui.spinBox_17.value()

        gender_x = self.ui.spinBox_12.value()
        gender_y = self.ui.spinBox_11.value()

        address_x = self.ui.spinBox_21.value()
        address_y = self.ui.spinBox_20.value()
        w = self.ui.spinBox.value()
        h = self.ui.spinBox_2.value()
        x = self.ui.spinBox_3.value()
        y = self.ui.spinBox_4.value()
        self.paint_images(self.background_image, self.foreground_image,
                          self.givenname,self.surname,self.birthday,self.gender,self.address,
                                img_x=x, img_y=y, 
                                img_width =w , img_height = h,
                                givenname_x = givenname_x, givenname_y= givenname_y, surname_x= surname_x, surname_y=surname_y,
                                birthday_x= birthday_x, birthday_y= birthday_y,gender_x= gender_x, gender_y= gender_y, 
                                address_x=address_x, address_y= address_y,font_family=font_family, is_bold=True, 
                                text_color ="Black", font_size = int(font_size))
        return 0

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui  = Ui_MainWindow()
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

        self.ui.comboBox_12.currentIndexChanged.connect(self.openUpPhoiWindow)
        self.show()
    def menuChanged(self):
        if self.ui.toolBox_3.currentIndex() ==0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_view)
        elif self.ui.toolBox_3.currentIndex() ==1:
            if self.ui.button_function.clicked:
                self.ui.stackedWidget.setCurrentWidget(self.ui.page_function)
        elif self.ui.toolBox_3.currentIndex() ==2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_config)
        elif self.ui.toolBox_3.currentIndex() ==3:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_contact)
    def openFileDialog(self):
        fname = QFileDialog.getOpenFileName(self, "Open File","", "Text files (*.txt)")
        if fname:
            self.ui.BtnListMail.setText(str(fname).replace("Text files (*.txt)","")[2:-6])
        return 0
    def openUpPhoiWindow(self):
        # self.window= QtWidgets.QMainWindow()
        self.window2 = UpPhoiWindow()
        # self.ui.setupUi(self.window)
        self.window2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    # window = UpPhoiWindow()
    window.show()
    sys.exit(app.exec_())
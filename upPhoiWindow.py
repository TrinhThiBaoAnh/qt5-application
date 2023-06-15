import sys
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget

from PyQt5.QtGui import QPainter, QPixmap, QFont, QFontDatabase, QTransform, QDesktopServices, QClipboard, QPdfWriter
from PyQt5.QtCore import Qt, QUrl,  QSettings
from Custom_Widgets.Widgets import *

from ui_upPhoiWindow import *

class UpPhoiWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui  = Ui_UpPhoiWindow()
        self.ui.setupUi(self)
        self.centerWindow()
        # Disable moving the window out of the screen boundaries
        self.setFixedSize(self.size())
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
        self.ui.btn_preview.clicked.connect(self.show_preview)
        # Connect the link clicked signal to a slot
        self.ui.label_36.linkActivated.connect(lambda url: QDesktopServices.openUrl(QUrl(url)))

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
    def paint_images(self, background_image, foreground_image, 
                     givenname,surname,birthday,gender,address, 
                     img_x, img_y, rotation_angle, img_width, img_height,
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
        transform = QTransform()
        transform.rotate(rotation_angle)
        rotated_image = foreground_image.transformed(transform)
        self.ui.image_label.setPixmap(background_image)

        self.ui.spinBox.setValue(img_width)
        self.ui.spinBox_2.setValue(img_height)
        combined_image = QPixmap(background_image.size())
        combined_image.fill(Qt.transparent)

        # Draw the background image on the combined image
        painter = QPainter(combined_image)
        painter.drawPixmap(0, 0, background_image)
        painter.drawPixmap(img_x, img_y, rotated_image)
        painter.setFont(font)
        painter.setPen(text_color)
        # Set the rotation angles for the texts
        angle_givenname = self.ui.spinBox_24.value()
        angle_surname = self.ui.spinBox_16.value()
        angle_birthday = self.ui.spinBox_19.value()
        angle_gender = self.ui.spinBox_13.value()
        angle_address = self.ui.spinBox_22.value()

        # Create a transformation matrix for the rotation angle around the center
        transform_1 = QTransform()
        transform_1.translate(givenname_x, givenname_y)
        transform_1.rotate(angle_givenname)
        transform_1.translate(-givenname_x, -givenname_y)
          # Create a transformation matrix for the rotation angle around the center
        transform_2 = QTransform()
        transform_2.translate(surname_x, surname_y)
        transform_2.rotate(angle_surname)
        transform_2.translate(-surname_x, -surname_y)
          # Create a transformation matrix for the rotation angle around the center
        transform_3 = QTransform()
        transform_3.translate(birthday_x, birthday_y)
        transform_3.rotate(angle_birthday)
        transform_3.translate(-birthday_x, -birthday_y)
          # Create a transformation matrix for the rotation angle around the center
        transform_4 = QTransform()
        transform_4.translate(gender_x, gender_y)
        transform_4.rotate(angle_gender)
        transform_4.translate(-gender_x, -gender_y)
          # Create a transformation matrix for the rotation angle around the center
        transform_5 = QTransform()
        transform_5.translate(address_x, address_y)
        transform_5.rotate(angle_address)
        transform_5.translate(-address_x, -address_y)

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

        self.combined_image = combined_image
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
                                img_x=100, img_y=100, rotation_angle = 0,
                                img_width =w , img_height = h,
                                givenname_x = givenname_x, givenname_y= givenname_y, surname_x= surname_x, surname_y=surname_y,
                                birthday_x= birthday_x, birthday_y= birthday_y,gender_x= gender_x, gender_y= gender_y,
                                address_x=address_x, address_y= address_y,font_family=font_family, is_bold=True, 
                                text_color ="Black", font_size = int(font_size))
            self.ui.spinBox.valueChanged.connect(self.update)
            self.ui.spinBox_2.valueChanged.connect(self.update)
            self.ui.spinBox_3.valueChanged.connect(self.update)
            self.ui.spinBox_4.valueChanged.connect(self.update)
            self.ui.spinBox_5.valueChanged.connect(self.update)

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
        img_angle  = self.ui.spinBox_5.value()
        x = self.ui.spinBox_3.value()
        y = self.ui.spinBox_4.value()
        self.paint_images(self.background_image, self.foreground_image,
                          self.givenname,self.surname,self.birthday,self.gender,self.address,
                                img_x=x, img_y=y, rotation_angle = img_angle,
                                img_width =w , img_height = h,
                                givenname_x = givenname_x, givenname_y= givenname_y, surname_x= surname_x, surname_y=surname_y,
                                birthday_x= birthday_x, birthday_y= birthday_y,gender_x= gender_x, gender_y= gender_y, 
                                address_x=address_x, address_y= address_y,font_family=font_family, is_bold=True, 
                                text_color ="Black", font_size = int(font_size))
        return 0
    def show_preview(self):
        self.preview_window = QMainWindow()
        self.preview_window.setWindowTitle("Image Preview")

        # # Create a label and set the pixmap
        label = QLabel()
        label.setPixmap(self.combined_image)
        self.preview_window.setCentralWidget(label)
        # Show the new window
        self.preview_window.show()
        # Save the combined_image as PDF
        self.save_as_png(self.combined_image)
        self.save_value()
        # self.load_value("/home/baoanh/Desktop/qt5_application/app_v1/output/config.ini")
    def save_as_png(self,   image):
        image.save("output/preview.png", "PNG")
    
    def load_value(self, filepath):
        settings = QSettings(filepath, QSettings.IniFormat)
        defaultValue = 0
        # Load values from the configuration file and set them to spin box widgets
        self.ui.spinBox.setValue(int(settings.value("Foreground_Width", defaultValue)))
        self.ui.spinBox_2.setValue(int(settings.value("Foreground_Height", defaultValue)))
        self.ui.spinBox_3.setValue(int(settings.value("Foreground_x", defaultValue)))
        self.ui.spinBox_4.setValue(int(settings.value("Foreground_y", defaultValue)))
        self.ui.spinBox_5.setValue(int(settings.value("Foreground_Angle", defaultValue)))
        self.ui.comboBox_2.setCurrentText(settings.value("Font_Size", defaultValue))
        self.ui.comboBox_3.setCurrentText(settings.value("Font_Family", defaultValue))
        self.ui.spinBox_23.setValue(int(settings.value("GivenName_x", defaultValue)))
        self.ui.spinBox_25.setValue(int(settings.value("GivenName_y", defaultValue)))
        self.ui.spinBox_24.setValue(int(settings.value("GivenName_Angle", defaultValue)))
        self.ui.spinBox_15.setValue(int(settings.value("FirstName_x", defaultValue)))
        self.ui.spinBox_14.setValue(int(settings.value("FirstName_y", defaultValue)))
        self.ui.spinBox_16.setValue(int(settings.value("FirstName_Angle", defaultValue)))
        self.ui.spinBox_18.setValue(int(settings.value("Birthday_x", defaultValue)))
        self.ui.spinBox_17.setValue(int(settings.value("Birthday_y", defaultValue)))
        self.ui.spinBox_19.setValue(int(settings.value("Birthday_Angle", defaultValue)))
        self.ui.spinBox_12.setValue(int(settings.value("Gender_x", defaultValue)))
        self.ui.spinBox_11.setValue(int(settings.value("Gender_y", defaultValue)))
        self.ui.spinBox_13.setValue(int(settings.value("Gender_Angle", defaultValue)))
        self.ui.spinBox_22.setValue(int(settings.value("Address_x", defaultValue)))
        self.ui.spinBox_20.setValue(int(settings.value("Address_y", defaultValue)))
        self.ui.spinBox_21.setValue(int(settings.value("Address_Angle", defaultValue)))
        print("Loading successfully!")
    def save_value(self):
        import datetime

        # Get the current date and time
        current_datetime = datetime.datetime.now()

        # Format the datetime as a string
        datetime_string = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        settings = QSettings(f"output/config_{datetime_string}.ini", QSettings.IniFormat)
        # Clear the content of the config file
        settings.clear()
        settings.setValue("Background_Width", 591)
        settings.setValue("Backgroun_Height",361)

        settings.setValue("Foreground_Width", self.ui.spinBox.value())
        settings.setValue("Foreground_Height",  self.ui.spinBox_2.value())
        settings.setValue("Foreground_x",  self.ui.spinBox_3.value())
        settings.setValue("Foreground_y",  self.ui.spinBox_4.value())
        settings.setValue("Foreground_Angle", self.ui.spinBox_5.value())

        settings.setValue("Font_Size", self.ui.comboBox_2.currentText())
        settings.setValue("Font_Family", self.ui.comboBox_3.currentText())

        
        settings.setValue("GivenName_x", self.ui.spinBox_23.value())
        settings.setValue("GivenName_y", self.ui.spinBox_25.value())
        settings.setValue("GivenName_Angle",self.ui.spinBox_24.value())

        settings.setValue("FirstName_x", self.ui.spinBox_15.value())
        settings.setValue("FirstName_y", self.ui.spinBox_14.value())
        settings.setValue("FirstName_Angle", self.ui.spinBox_16.value())

        settings.setValue("Birthday_x", self.ui.spinBox_18.value())
        settings.setValue("Birthday_y", self.ui.spinBox_17.value())
        settings.setValue("Birthday_Angle", self.ui.spinBox_19.value())

        settings.setValue("Gender_x", self.ui.spinBox_12.value())
        settings.setValue("Gender_y",self.ui.spinBox_11.value())
        settings.setValue("Gender_Angle", self.ui.spinBox_13.value())

        settings.setValue("Address_x", self.ui.spinBox_22.value())
        settings.setValue("Address_y",  self.ui.spinBox_20.value())
        settings.setValue("Address_Angle", self.ui.spinBox_22.value())

        settings.sync()
        print(f"All configuration is saved in output/config_{datetime_string}.ini")


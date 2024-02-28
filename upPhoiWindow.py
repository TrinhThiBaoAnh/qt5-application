import sys
from PyQt5.QtWidgets import QFileDialog, QDesktopWidget, QMessageBox
import os
from PyQt5.QtGui import QPainter, QPixmap, QFont, QFontDatabase, QTransform
from PyQt5.QtCore import Qt, QSettings
from Custom_Widgets.Widgets import *
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from ui_upPhoiWindow import *
class UpPhoiWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui  = Ui_UpPhoiWindow()
        self.ui.setupUi(self)
        screen = QDesktopWidget().screenGeometry()
        # Calculate the center point of the screen
        center_x = screen.width() // 2
        center_y = screen.height() // 2

        
        # self.setFixedSize(self.size())
        # self.centerWindow()
        # Get the screen geometry
        screen_rect = QDesktopWidget().screenGeometry()

        # Set the window size based on the screen size
        window_width = screen_rect.width() * 0.8  # Set the desired width (e.g., 80% of the screen width)
        window_height = screen_rect.height() * 0.8  # Set the desired height (e.g., 80% of the screen height)
        self.resize(window_width, window_height)
        self.move(center_x -window_width//2, center_y - window_height//2)
        # Disable moving the window out of the screen boundaries
        # self.setFixedSize(self.size())
        self.ui.pushButton.clicked.connect(self.browser_images)
        # Get the list of available font families
        # font_families = QFontDatabase().families()
        font_file_1 = [file for file in os.listdir("./font passport") if file.endswith(".ttf")]
        # font_file_2 = [file for file in os.listdir("./font passport/static/OpenSans") if file.endswith(".ttf")]
        # font_file_3 = [file for file in os.listdir("./font passport/static/OpenSans_Condensed") if file.endswith(".ttf")]
        # font_file_4 = [file for file in os.listdir("./font passport/static/OpenSans_SemiCondensed") if file.endswith(".ttf")]
        # Set the font families as items in the QComboBox
        # font_files = font_file_1 + font_file_2 + font_file_3 + font_file_4
        # print(font_file_1)
        self.ui.comboBox_3.addItems(font_file_1)
        for num in range(6, 96):
            self.ui.comboBox_2.addItem(str(num))
        self.ui.btn_preview.clicked.connect(self.show_preview)
        self.load_value('output/config.ini')
        self.ui.label_img.setScaledContents(True)
        self.enable_spinbox()
        self.ui.checkBox_birthday.clicked.connect(self.enable_spinbox)
        self.ui.checkBox_fullname.clicked.connect(self.enable_spinbox)
        self.ui.checkBox_givenname.clicked.connect(self.enable_spinbox)
        self.ui.checkBox_surname.clicked.connect(self.enable_spinbox)
        self.ui.checkBox_code.clicked.connect(self.enable_spinbox)
        self.ui.checkBox_gender.clicked.connect(self.enable_spinbox)
        self.ui.checkBox_code.setStyleSheet('''


            QCheckBox::indicator:checked {
                image: url(icons/icons8-toggle-on-40.png);  /* Replace with your toggle-on image */
            }

            QCheckBox::indicator:unchecked {
                image: url(icons/icons8-toggle-off-40.png);  /* Replace with your toggle-off image */
            }
        ''')
        self.ui.checkBox_surname.setStyleSheet('''


            QCheckBox::indicator:checked {
                image: url(icons/icons8-toggle-on-40.png);  /* Replace with your toggle-on image */
            }

            QCheckBox::indicator:unchecked {
                image: url(icons/icons8-toggle-off-40.png);  /* Replace with your toggle-off image */
            }
        ''')
        self.ui.checkBox_givenname.setStyleSheet('''


            QCheckBox::indicator:checked {
                image: url(icons/icons8-toggle-on-40.png);  /* Replace with your toggle-on image */
            }

            QCheckBox::indicator:unchecked {
                image: url(icons/icons8-toggle-off-40.png);  /* Replace with your toggle-off image */
            }
        ''')
        self.ui.checkBox_fullname.setStyleSheet('''


            QCheckBox::indicator:checked {
                image: url(icons/icons8-toggle-on-40.png);  /* Replace with your toggle-on image */
            }

            QCheckBox::indicator:unchecked {
                image: url(icons/icons8-toggle-off-40.png);  /* Replace with your toggle-off image */
            }
        ''')
        self.ui.checkBox_birthday.setStyleSheet('''


            QCheckBox::indicator:checked {
                image: url(icons/icons8-toggle-on-40.png);  /* Replace with your toggle-on image */
            }

            QCheckBox::indicator:unchecked {
                image: url(icons/icons8-toggle-off-40.png);  /* Replace with your toggle-off image */
            }
        ''')
        self.ui.checkBox_gender.setStyleSheet('''


            QCheckBox::indicator:checked {
                image: url(icons/icons8-toggle-on-40.png);  /* Replace with your toggle-on image */
            }

            QCheckBox::indicator:unchecked {
                image: url(icons/icons8-toggle-off-40.png);  /* Replace with your toggle-off image */
            }
        ''')
        self.show()

    def enable_spinbox(self):
        if not self.ui.checkBox_fullname.isChecked():
            self.ui.spinBox_26.setEnabled(False)
            self.ui.spinBox_27.setEnabled(False)
            self.ui.spinBox_28.setEnabled(False) 
        else:
            self.ui.spinBox_26.setEnabled(True)
            self.ui.spinBox_27.setEnabled(True)
            self.ui.spinBox_28.setEnabled(True) 
        if not self.ui.checkBox_code.isChecked():
            self.ui.spinBox_11.setEnabled(False)
            self.ui.spinBox_12.setEnabled(False)
            self.ui.spinBox_13.setEnabled(False) 
        else:
            self.ui.spinBox_11.setEnabled(True)
            self.ui.spinBox_12.setEnabled(True)
            self.ui.spinBox_13.setEnabled(True) 
        if not self.ui.checkBox_givenname.isChecked():
            self.ui.spinBox_23.setEnabled(False)
            self.ui.spinBox_24.setEnabled(False)
            self.ui.spinBox_25.setEnabled(False) 
        else:
            self.ui.spinBox_23.setEnabled(True)
            self.ui.spinBox_24.setEnabled(True)
            self.ui.spinBox_25.setEnabled(True) 
        if not self.ui.checkBox_surname.isChecked():
            self.ui.spinBox_14.setEnabled(False)
            self.ui.spinBox_15.setEnabled(False)
            self.ui.spinBox_16.setEnabled(False) 
        else:
            self.ui.spinBox_14.setEnabled(True)
            self.ui.spinBox_15.setEnabled(True)
            self.ui.spinBox_16.setEnabled(True) 
        if not self.ui.checkBox_birthday.isChecked():
            self.ui.spinBox_17.setEnabled(False)
            self.ui.spinBox_18.setEnabled(False)
            self.ui.spinBox_19.setEnabled(False) 
        else:
            self.ui.spinBox_17.setEnabled(True)
            self.ui.spinBox_18.setEnabled(True)
            self.ui.spinBox_19.setEnabled(True)
        if not self.ui.checkBox_gender.isChecked():
            self.ui.spinBox_32.setEnabled(False)
            self.ui.spinBox_33.setEnabled(False)
            self.ui.spinBox_34.setEnabled(False) 
        else:
            self.ui.spinBox_32.setEnabled(True)
            self.ui.spinBox_33.setEnabled(True)
            self.ui.spinBox_34.setEnabled(True)
    def paint_images(self, background_image, foreground_image,
                     img_x, img_y, rotation_angle, img_width, img_height,
                     fullname_x, fullname_y,givenname_x, givenname_y, surname_x, surname_y,gender_x, gender_y,
                     birthday_x, birthday_y,code_x, code_y,
                     font_family, is_bold, 
                     text_color, font_size):
        if not self.ui.checkBox_fullname.isChecked():
            self.fullname = ""
            self.ui.spinBox_26.setEnabled(False)
            self.ui.spinBox_27.setEnabled(False)
            self.ui.spinBox_28.setEnabled(False) 
        else:
            self.fullname = "Full name"
            self.ui.spinBox_26.setEnabled(True)
            self.ui.spinBox_27.setEnabled(True)
            self.ui.spinBox_28.setEnabled(True) 
        if not self.ui.checkBox_code.isChecked():
            self.code = ""
            self.ui.spinBox_11.setEnabled(False)
            self.ui.spinBox_12.setEnabled(False)
            self.ui.spinBox_13.setEnabled(False) 
        else:
            self.code = "1234567890"
            self.ui.spinBox_11.setEnabled(True)
            self.ui.spinBox_12.setEnabled(True)
            self.ui.spinBox_13.setEnabled(True) 
        if not self.ui.checkBox_givenname.isChecked():
            self.givenname = ""
            self.ui.spinBox_23.setEnabled(False)
            self.ui.spinBox_24.setEnabled(False)
            self.ui.spinBox_25.setEnabled(False) 
        else:
            self.givenname = "First Name"
            self.ui.spinBox_23.setEnabled(True)
            self.ui.spinBox_24.setEnabled(True)
            self.ui.spinBox_25.setEnabled(True) 
        if not self.ui.checkBox_gender.isChecked():
            self.gender = ""
            self.ui.spinBox_32.setEnabled(False)
            self.ui.spinBox_33.setEnabled(False)
            self.ui.spinBox_34.setEnabled(False) 
        else:
            self.gender = "Gender"
            self.ui.spinBox_32.setEnabled(True)
            self.ui.spinBox_33.setEnabled(True)
            self.ui.spinBox_34.setEnabled(True) 
        if not self.ui.checkBox_surname.isChecked():
            self.surname = ""
            self.ui.spinBox_14.setEnabled(False)
            self.ui.spinBox_15.setEnabled(False)
            self.ui.spinBox_16.setEnabled(False) 
        else:
            self.surname = "Last Name"
            self.ui.spinBox_14.setEnabled(True)
            self.ui.spinBox_15.setEnabled(True)
            self.ui.spinBox_16.setEnabled(True) 
        if not self.ui.checkBox_birthday.isChecked():
            self.birthday = ""
            self.ui.spinBox_17.setEnabled(False)
            self.ui.spinBox_18.setEnabled(False)
            self.ui.spinBox_19.setEnabled(False) 
        else:
            self.ui.spinBox_17.setEnabled(True)
            self.ui.spinBox_18.setEnabled(True)
            self.ui.spinBox_19.setEnabled(True)
            if self.ui.comboBox_time_format.currentIndex() == 0:
                self.birthday = "dd/mm/yyyy"
            else:
                self.birthday = "dd Month yyyy"

        # font = QFont()
        # font_id = QFontDatabase.addApplicationFont('/home/baoanh/Desktop/qt5_application/app_v1/font passport/OCR-B 10 BT.ttf')
        # font_family = QFontDatabase.applicationFontFamilies(font_id)

        # Create a QFont object with the desired font family
        # font = QFont(font_family)
        # font.setFamily(font_family)
        font_id = QFontDatabase.addApplicationFont('./font passport/' + font_family)
        font_name = QFontDatabase.applicationFontFamilies(font_id)[0]

        # Create a QFont object with the loaded font
        font = QFont(font_name)
        font.setPointSize(font_size)
        font.setBold(is_bold)
        
        text_color = Qt.black

        self.ui.spinBox_3.setValue(img_x)
        self.ui.spinBox_4.setValue(img_y)

        foreground_image = foreground_image.scaled(img_width, img_height)
        transform = QTransform()
        transform.rotate(rotation_angle)
        rotated_image = foreground_image.transformed(transform)


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
        angle_code = self.ui.spinBox_13.value()
        angle_fullname = self.ui.spinBox_28.value()
        angle_gender = self.ui.spinBox_34.value()

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
        transform_4.translate(code_x, code_y)
        transform_4.rotate(angle_code)
        transform_4.translate(-code_x, -code_y)
          # Create a transformation matrix for the rotation angle around the center
        transform_5 = QTransform()
        transform_5.translate(fullname_x, fullname_y)
        transform_5.rotate(angle_fullname)
        transform_5.translate(-fullname_x, -fullname_y)

        transform_6 = QTransform()
        transform_6.translate(gender_y, gender_y)
        transform_6.rotate(angle_gender)
        transform_6.translate(-gender_y, -gender_y)

        painter.setTransform(transform_1)
        painter.drawText(givenname_x, givenname_y, self.givenname)

        painter.setTransform(transform_2)
        painter.drawText(surname_x, surname_y, self.surname)

        painter.setTransform(transform_3)
        painter.drawText(birthday_x, birthday_y, self.birthday)

        painter.setTransform(transform_4)
        painter.drawText(code_x, code_y, self.code)

        painter.setTransform(transform_5)
        painter.drawText(fullname_x, fullname_y, self.fullname)

        painter.setTransform(transform_6)
        painter.drawText(gender_x, gender_y, self.gender)

        self.combined_image = combined_image
        self.ui.label_img.setPixmap(combined_image)
        self.ui.label_img.show()
    def browser_images(self):
        fname = QFileDialog.getOpenFileName(self, "Open Image","", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fname:
            img_path = str(fname).replace("Image Files (*.png *.jpg *.jpeg *.bmp)","")[2:-6]
            self.ui.textEdit.setText(img_path)
            self.background_image = QPixmap(img_path)
            self.org_w = self.background_image.width()
            self.org_h = self.background_image.height()
            # print(self.org_w, self.org_h)
            self.foreground_image = QPixmap("phoi/a.png")
           
            if self.ui.spinBox.value() > 0 and self.ui.spinBox_2.value() > 0:
                w = self.ui.spinBox.value()
                h = self.ui.spinBox_2.value()
            else:
                w = self.foreground_image.width()
                h = self.foreground_image.height()
            # current_index = self.ui.comboBox_2.currentIndex()
            font_size = self.ui.comboBox_2.currentText()

            # current_index = self.ui.comboBox_3.currentIndex()
            font_family = self.ui.comboBox_3.currentText()
            givenname_x = self.ui.spinBox_23.value()
            givenname_y = self.ui.spinBox_25.value()

            surname_x = self.ui.spinBox_15.value()
            surname_y = self.ui.spinBox_14.value()

            birthday_x = self.ui.spinBox_18.value()
            birthday_y = self.ui.spinBox_17.value()

            code_x = self.ui.spinBox_12.value()
            code_y = self.ui.spinBox_11.value()

            fullname_x = self.ui.spinBox_26.value()
            fullname_y = self.ui.spinBox_27.value()

            gender_x = self.ui.spinBox_32.value()
            gender_y = self.ui.spinBox_33.value()
            self.paint_images(self.background_image, self.foreground_image,
                                img_x=self.ui.spinBox_3.value(), img_y=self.ui.spinBox_4.value(), rotation_angle = self.ui.spinBox_5.value(),
                                img_width =w , img_height = h,
                                fullname_x= fullname_x, fullname_y= fullname_y,
                                givenname_x = givenname_x, givenname_y= givenname_y, surname_x= surname_x, surname_y=surname_y,
                                gender_x=gender_x, gender_y=gender_y, birthday_x= birthday_x, birthday_y= birthday_y,code_x= code_x, code_y= code_y,
                                font_family=font_family, is_bold=True, 
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

            self.ui.comboBox_2.currentIndexChanged.connect(self.update)
            self.ui.comboBox_3.currentIndexChanged.connect(self.update)

            self.ui.spinBox_24.valueChanged.connect(self.update)
            self.ui.spinBox_16.valueChanged.connect(self.update)
            self.ui.spinBox_19.valueChanged.connect(self.update)
            self.ui.spinBox_13.valueChanged.connect(self.update)

            self.ui.spinBox_26.valueChanged.connect(self.update)
            self.ui.spinBox_27.valueChanged.connect(self.update)
            self.ui.spinBox_28.valueChanged.connect(self.update)

            self.ui.spinBox_32.valueChanged.connect(self.update)
            self.ui.spinBox_33.valueChanged.connect(self.update)
            self.ui.spinBox_34.valueChanged.connect(self.update)

            self.ui.checkBox_birthday.clicked.connect(self.update)
            self.ui.checkBox_fullname.clicked.connect(self.update)
            self.ui.checkBox_givenname.clicked.connect(self.update)
            self.ui.checkBox_surname.clicked.connect(self.update)
            self.ui.checkBox_code.clicked.connect(self.update)
            self.ui.checkBox_gender.clicked.connect(self.update)

            self.ui.comboBox_time_format.currentIndexChanged.connect(self.update)

        return 0
    def update(self):
        if not self.ui.checkBox_birthday.isChecked():
                self.birthday = ""
        else:
            if self.ui.comboBox_time_format.currentIndex() == 0:
                self.birthday = "dd/mm/yyyy"
            else:
                self.birthday = "dd Month yyyy"
        font_family = self.ui.comboBox_3.currentText()
        font_size = self.ui.comboBox_2.currentText()

        fullname_x = self.ui.spinBox_26.value()
        fullname_y = self.ui.spinBox_27.value()
 
        givenname_x = self.ui.spinBox_23.value()
        givenname_y = self.ui.spinBox_25.value()
 
        surname_x = self.ui.spinBox_15.value()
        surname_y = self.ui.spinBox_14.value()

        birthday_x = self.ui.spinBox_18.value()
        birthday_y = self.ui.spinBox_17.value()

        code_x = self.ui.spinBox_12.value()
        code_y = self.ui.spinBox_11.value()

        gender_x = self.ui.spinBox_32.value()
        gender_y = self.ui.spinBox_33.value()
        w = self.ui.spinBox.value()
        h = self.ui.spinBox_2.value()
        img_angle  = self.ui.spinBox_5.value()
        x = self.ui.spinBox_3.value()
        y = self.ui.spinBox_4.value()
        
        self.paint_images(self.background_image, self.foreground_image,
                                img_x=x, img_y=y, rotation_angle = img_angle,
                                img_width =w , img_height = h, 
                                fullname_x=fullname_x, fullname_y=fullname_y,
                                givenname_x = givenname_x, givenname_y= givenname_y, surname_x= surname_x, surname_y=surname_y,
                                gender_x=gender_x, gender_y=gender_y,birthday_x= birthday_x, birthday_y= birthday_y,code_x= code_x, code_y= code_y, 
                                font_family=font_family, is_bold=True, 
                                text_color ="Black", font_size = int(font_size))
        return 0
    def show_preview(self):
        try: 
            self.save_as_jpg(self.combined_image)
            self.save_value()
            QMessageBox.information(self, "Notification", "Config save!")
        except:
            QMessageBox.information(self, "Invalid action!", "Tải phôi lên trước khi lưu cấu hình")
    def save_as_jpg(self, image):
        try: 
            image.save("output/preview.jpg", "JPG")
        except:
            print("Error when saving image!")

    def load_value(self, filepath):
        settings = QSettings(filepath, QSettings.IniFormat)
        defaultValue = 0
        settings.beginGroup('section2')
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
        self.ui.spinBox_12.setValue(int(settings.value("Code_x", defaultValue)))
        self.ui.spinBox_11.setValue(int(settings.value("Code_y", defaultValue)))
        self.ui.spinBox_13.setValue(int(settings.value("Code_Angle", defaultValue)))
        self.ui.spinBox_26.setValue(int(settings.value("Fullname_x", defaultValue)))
        self.ui.spinBox_27.setValue(int(settings.value("Fullname_y", defaultValue)))
        self.ui.spinBox_28.setValue(int(settings.value("Fullname_Angle", defaultValue)))
        self.ui.spinBox_32.setValue(int(settings.value("Gender_x", defaultValue)))
        self.ui.spinBox_33.setValue(int(settings.value("Gender_y", defaultValue)))
        self.ui.spinBox_34.setValue(int(settings.value("Gender_Angle", defaultValue)))

        fullname_active = settings.value("Active_Fullname", False, bool)
        givenname_active = settings.value("Active_Givenname", False, bool)
        surname_active = settings.value("Active_Surname", False, bool)
        birthday_active = settings.value("Active_Birthday", False, bool)
        code_active = settings.value("Active_Code", False, bool)
        gender_active = settings.value("Active_Gender", False, bool)

        # Use the loaded values to set the checkbox states
        self.ui.checkBox_fullname.setChecked(fullname_active)
        self.ui.checkBox_givenname.setChecked(givenname_active)
        self.ui.checkBox_surname.setChecked(surname_active)
        self.ui.checkBox_birthday.setChecked(birthday_active)
        self.ui.checkBox_code.setChecked(code_active)
        self.ui.checkBox_gender.setChecked(gender_active)
        
        if settings.value("Time_format", defaultValue) == 0:
            self.ui.comboBox_time_format.setCurrentText("dd/mm/yyyy")
        else:
            self.ui.comboBox_time_format.setCurrentText("dd Month yyyy")
        settings.endGroup()
        print("Loading successfully!")
    def save_value(self):
        
        settings = QSettings(f"output/config.ini", QSettings.IniFormat)
        settings.beginGroup('section2')
        settings.setValue("Background_Width", self.org_w)
        settings.setValue("Background_Height",self.org_h)

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
        settings.setValue("Time_format", self.ui.comboBox_time_format.currentIndex())

        settings.setValue("Code_x", self.ui.spinBox_12.value())
        settings.setValue("Code_y",self.ui.spinBox_11.value())
        settings.setValue("Code_Angle", self.ui.spinBox_13.value())

        settings.setValue("Gender_x", self.ui.spinBox_32.value())
        settings.setValue("Gender_y",self.ui.spinBox_33.value())
        settings.setValue("Gender_Angle", self.ui.spinBox_34.value())

        settings.setValue("Fullname_x", self.ui.spinBox_26.value())
        settings.setValue("Fullname_y",  self.ui.spinBox_27.value())
        settings.setValue("Fullname_Angle", self.ui.spinBox_28.value()) 

        settings.setValue("Active_Fullname", self.ui.checkBox_fullname.isChecked())
        settings.setValue("Active_Givenname", self.ui.checkBox_givenname.isChecked())
        settings.setValue("Active_Surname", self.ui.checkBox_surname.isChecked())
        settings.setValue("Active_Birthday", self.ui.checkBox_birthday.isChecked())
        settings.setValue("Active_Code", self.ui.checkBox_code.isChecked())
        settings.setValue("Active_Gender", self.ui.checkBox_gender.isChecked())

        settings.sync()
        settings.endGroup()
        print(f"All configuration is saved in output/config.ini")


from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtWidgets import QMainWindow, QLabel

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Window 2", self)
        self.setWindowTitle("Window 2")

        self.label2 = QLabel("Hello, World!", self)
        self.label2.setGeometry(50, 50, 200, 30)
        self.setGeometry(200, 200, 400, 300)

        self.button = QPushButton("Test", self)
        self.button.clicked.connect(self.someEventHandlingMethod)
    def someEventHandlingMethod(self):
        self.label2.setText("some event handling method")

# if __name__ == '__main__':
#     import sys
#     from PyQt5.QtWidgets import QApplication

#     app = QApplication(sys.argv)
#     window2 = Window2()
#     window2.show()
#     sys.exit(app.exec_())

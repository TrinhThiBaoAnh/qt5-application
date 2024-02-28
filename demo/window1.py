from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt
from window2 import Window2

class Window1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Open Window 2", self)
        self.button.clicked.connect(self.openWindow2)

        self.setWindowTitle("Window 1")
        self.setGeometry(100, 100, 400, 300)

    def openWindow2(self):
        self.window2 = Window2()
        self.window2.show()


if __name__ == '__main__':
    app = QApplication([])
    window1 = Window1()
    window1.show()
    app.exec_()

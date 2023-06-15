import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Disable Window Move Out")
        self.setGeometry(100, 100, 400, 300)

        # Center the window on the screen
        self.centerWindow()

        # Disable moving the window out of the screen boundaries
        self.setFixedSize(self.size())

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

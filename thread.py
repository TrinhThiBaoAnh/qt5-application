import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal, QCoreApplication

class NumberGeneratorThread(QThread):
    number_generated = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.last_generated_number = 0

    def run(self):
        for i in range(self.last_generated_number + 1, 101):
            if self.isInterruptionRequested():
                return
            self.number_generated.emit(i)
            self.msleep(200)  # Add a delay of 200 milliseconds

    def set_last_generated_number(self, number):
        self.last_generated_number = number

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Number Generator")

        self.start_button = QPushButton("Start", self)
        self.start_button.setGeometry(50, 50, 100, 30)
        self.start_button.clicked.connect(self.start_generation)

        self.stop_button = QPushButton("Stop", self)
        self.stop_button.setGeometry(200, 50, 100, 30)
        self.stop_button.clicked.connect(self.stop_generation)
        self.stop_button.setEnabled(False)

        self.output_text_edit = QTextEdit(self)
        self.output_text_edit.setGeometry(50, 100, 250, 200)
        self.output_text_edit.setReadOnly(True)

        self.generator_thread = NumberGeneratorThread()
        self.generator_thread.number_generated.connect(self.handle_number_generated)

    def start_generation(self):
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.output_text_edit.clear()

        if not self.generator_thread.isRunning():
            # Start a new generation from the beginning
            self.generator_thread.set_last_generated_number(0)
            self.generator_thread.start()
        else:
            # Resume generation from the last generated number
            last_generated_number = int(self.output_text_edit.toPlainText().split()[-1])
            self.generator_thread.set_last_generated_number(last_generated_number)
            self.generator_thread.msleep(200)  # Add a small delay before resuming

    def stop_generation(self):
        self.start_button.setEnabled(True)
        self.generator_thread.requestInterruption()

    def handle_number_generated(self, number):
        self.output_text_edit.append(str(number))

app = QApplication(sys.argv)
window = MainWindow()
window.setGeometry(300, 300, 350, 350)
window.show()
sys.exit(app.exec_())

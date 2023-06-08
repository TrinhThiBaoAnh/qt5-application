import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal, QCoreApplication

class NumberGeneratorThread(QThread):
    number_generated = pyqtSignal(int, int)  # Signal with value and thread ID

    def __init__(self, thread_id, start_number):
        super().__init__()
        self.thread_id = thread_id
        self.start_number = start_number

    def run(self):
        for i in range(self.start_number, self.start_number + 10):
            if self.isInterruptionRequested():
                return
            self.number_generated.emit(i, self.thread_id)
            self.msleep(200)  # Add a delay of 200 milliseconds

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

        self.generator_threads = []

    def start_generation(self):
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.output_text_edit.clear()

        for i in range(1, 4):  # Create 3 generator threads
            generator_thread = NumberGeneratorThread(i, (i-1) * 10 + 1)
            generator_thread.number_generated.connect(self.handle_number_generated)
            self.generator_threads.append(generator_thread)
            generator_thread.start()

    def stop_generation(self):
        self.start_button.setEnabled(True)
        for generator_thread in self.generator_threads:
            generator_thread.requestInterruption()

    def handle_number_generated(self, number, thread_id):
        self.output_text_edit.append(f"Thread {thread_id}: {number}")

app = QApplication(sys.argv)
window = MainWindow()
window.setGeometry(300, 300, 350, 350)
window.show()
sys.exit(app.exec_())

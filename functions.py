import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal, QCoreApplication


class NumberGeneratorThread(QThread):
    do_work = pyqtSignal(int, str)  # Signal to indicate thread start do work
    number_generated = pyqtSignal(int, int)
    thread_finished = pyqtSignal(int)  # Signal to indicate thread completion

    def __init__(self, thread_id, start_number, delay_time):
        super().__init__()
        self.start_number = start_number
        self.delay_time = delay_time
        # print(delay_time)
        self.thread_id = thread_id
        self.cookie_login_success = None

    def run(self):
        # for i in range(self.start_number, self.start_number + 10):
        #     if self.isInterruptionRequested():
        #         return
        #     self.number_generated.emit(i, self.thread_id)
        #     self.msleep(200)  # Add a delay of 200 milliseconds
        if self.isInterruptionRequested():
            return
        # Gửi tín hiệu bắt đầu công việc
        self.do_work.emit(self.thread_id, self.cookie_login_success)
        # Gửi tín hiệu kết thúc công việc
        self.thread_finished.emit(self.thread_id)

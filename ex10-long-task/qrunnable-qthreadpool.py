import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, QThread, pyqtSignal, pyqtSlot, QRunnable, QThreadPool, QObject
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton


class MyTaskSignals(QObject):
    begin = pyqtSignal()
    progressing = pyqtSignal(float)
    done = pyqtSignal()


class MyTaskWorker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = MyTaskSignals()
        self.begin = self.signals.begin
        self.progressing = self.signals.progressing
        self.done = self.signals.done

    def run(self):
        self.begin.emit()
        time.sleep(5)
        self.progressing.emit(0.33)
        time.sleep(10)
        self.done.emit()


class HelloWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("Hello world")

        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        gridLayout = QGridLayout()
        centralWidget.setLayout(gridLayout)
        title = QLabel("Hello World from PyQt", self)
        title.setAlignment(QtCore.Qt.AlignCenter)
        gridLayout.addWidget(title, 0, 0)
        self.title = title

        self.button = button = QPushButton(self)
        button.setText("Good!")
        gridLayout.addWidget(button, 1, 0, QtCore.Qt.AlignHCenter)
        button.pressed.connect(self.long_task)

        self.threadpool = QThreadPool()

    @pyqtSlot()
    def task_begin(self):
        self.title.setText('Running a big task...')

    @pyqtSlot(float)
    def task_progressing(self, p):
        self.title.setText('Running a big task... Progress {0:.0f}%'.format(p * 100))

    @pyqtSlot()
    def task_done(self):
        self.title.setText('Task finished.')

    def long_task(self):
        worker = MyTaskWorker()
        worker.begin.connect(self.task_begin)
        worker.progressing.connect(self.task_progressing)
        worker.done.connect(self.task_done)
        self.threadpool.start(worker)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )
import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, QThread
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton


class MyTaskThread(QThread):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.title = title

    def run(self):
        self.title.setText('Running a big task...')
        time.sleep(5)
        self.title.setText('Running a big task... Progress 33%...')
        time.sleep(10)
        self.title.setText('Task finished.')


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

        button = QPushButton(self)
        button.setText("Good!")
        gridLayout.addWidget(button, 1, 0, QtCore.Qt.AlignHCenter)
        button.pressed.connect(self.long_task)

    def long_task(self):
        self.task = MyTaskThread(self.title)
        self.task.start()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )
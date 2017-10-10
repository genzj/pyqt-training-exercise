import logging
import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget, QPushButton, QPlainTextEdit
from PyQt5.QtCore import QSize, pyqtSlot


def create_slot(x):
    return lambda: logging.info('you pressed the button %d', x)


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
        gridLayout.addWidget(title, 0, 0, 1, 10)

        logging_text_edit = QPlainTextEdit()
        gridLayout.addWidget(logging_text_edit, 2, 0, 1, 10)

        for x in range(10):
            button = QPushButton(self)
            button.setText("Print %d" % (x, ))
            gridLayout.addWidget(button, 3, x, QtCore.Qt.AlignHCenter)
            button.pressed.connect(create_slot(x))

        class QLogHandler(logging.Handler):
            def __init__(self):
                logging.Handler.__init__(self)

            def emit(self, record):
                record = self.format(record)
                logging_text_edit.appendPlainText(record)

        q_log_handler = QLogHandler()
        q_log_handler.setLevel(logging.DEBUG)
        q_log_handler.setFormatter(logging.Formatter('%(asctime)s\n%(name)s\n%(levelname)s:%(message)s\n'))
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger('').addHandler(q_log_handler)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWin = HelloWindow()
    mainWin.show()
    sys.exit( app.exec_() )
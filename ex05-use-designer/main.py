# encoding: utf-8
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUiType

_ui_cls, _base = loadUiType('main.ui')


class MainDialog(_base):
    def __init__(self):
        super(MainDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = _ui_cls()
        self.ui.setupUi(self)

        self.ui.pushButtonSend.pressed.connect(self.send_something)

    def send_something(self):
        text = self.ui.lineEditData.text()
        if not text:
            return
        self.ui.plainTextEdit.appendPlainText(text)
        self.ui.lineEditData.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainDialog()
    window.show()
    ret = app.exec_()
    sys.exit(ret)
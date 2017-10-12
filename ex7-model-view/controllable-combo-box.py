# encoding: utf-8
import sys

from PyQt5.QtCore import QStringListModel, Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUiType

_ui_cls, _base = loadUiType('controllable-combo-box.ui')


class MainDialog(_base):
    def __init__(self):
        super(MainDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = _ui_cls()
        self.ui.setupUi(self)

        self.model = QStringListModel()
        for x in (self.ui.comboBox, self.ui.comboBox_2, self.ui.comboBox_3):
            x.setModel(self.model)
            x.currentTextChanged.connect(self.update_label_bg)

        for x in (self.ui.checkBox, self.ui.checkBox_2, self.ui.checkBox_3, self.ui.checkBox_4, self.ui.checkBox_5):
            x.stateChanged.connect(self.refresh_model)

    @pyqtSlot()
    def refresh_model(self):
        names = []
        for x in (self.ui.checkBox, self.ui.checkBox_2, self.ui.checkBox_3, self.ui.checkBox_4, self.ui.checkBox_5):
            if x.isChecked():
                names.append(x.text())
        self.model.setStringList(names)

    @pyqtSlot()
    def update_label_bg(self):
        for suffix in ('', '_2', '_3'):
            label = getattr(self.ui, 'label' + suffix)
            combobox = getattr(self.ui, 'comboBox' + suffix)
            bg = combobox.currentText()
            if not bg or bg.lower == 'transparent':
                bg = 'none'
            label.setStyleSheet('background: %s' % (bg, ))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainDialog()
    window.show()
    ret = app.exec_()
    sys.exit(ret)
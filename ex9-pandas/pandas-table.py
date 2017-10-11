import sys

import numpy as np
import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableView, QApplication


class PandasModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    view = QTableView()
    df = pd.DataFrame(np.random.randn(100, 4), index=pd.date_range('1/1/2000', periods=100), columns=list('ABCD'))
    model = PandasModel(df)
    view.setModel(model)

    view.show()
    sys.exit(application.exec_())
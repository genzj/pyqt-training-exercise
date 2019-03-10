from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt


class ArrayTableModel(QAbstractTableModel):
    def __init__(self, data, parent=None, *args):
        """ data: a list of lists
        """
        QAbstractTableModel.__init__(self, parent, *args)
        self._data = data

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._data[0])

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self._data[index.row()][index.column()])

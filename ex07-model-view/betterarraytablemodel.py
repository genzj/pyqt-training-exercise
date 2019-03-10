import operator
import pprint

from PyQt5.QtCore import QAbstractTableModel, QVariant, Qt, QModelIndex


class ArrayTableModel(QAbstractTableModel):
    def __init__(self, data, parent=None, *args):
        """ data: a list of lists
        """
        QAbstractTableModel.__init__(self, parent, *args)
        self._header = data[0]
        self._data = data[1:]

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._data[0])

    def setData(self, index, value, role=Qt.EditRole):
        if not index.isValid() or index.column() >= self.columnCount(None) or index.row() >= self.rowCount(None):
            return False
        self._data[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        pprint.pprint(self._data)
        return True

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role == Qt.DisplayRole or role == Qt.EditRole:
            return QVariant(self._data[index.row()][index.column()])
        else:
            return QVariant()

    def flags(self, index):
        if not index.isValid() or index.column() >= self.columnCount(None) or index.row() >= self.rowCount(None):
            return super().flags(index)
        return super().flags(index) | Qt.ItemIsEditable

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self._header[col])
        return QVariant()

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        self.layoutAboutToBeChanged.emit()
        self._data = sorted(self._data, key=operator.itemgetter(Ncol))
        if order == Qt.DescendingOrder:
            self._data.reverse()
        self.layoutChanged.emit()

    def addRow(self, data, parent=None):
        if parent is None:
            parent = QModelIndex()
        self.beginInsertRows(
            parent, len(self._data) - 1, len(self._data)
        )

        self._data.append(data)
        self.endInsertRows()

    def clearRows(self):
        self.beginResetModel()
        self._data = list()
        self.endResetModel()

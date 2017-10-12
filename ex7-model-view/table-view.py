# encoding: utf-8
import sys

from PyQt5.QtWidgets import QApplication, QStyle
from PyQt5.uic import loadUiType
from arraytablemodel import ArrayTableModel
# from betterarraytablemodel import ArrayTableModel
# from sqlitemodel import get_sql_model, query_sql_model


_ui_cls, _base = loadUiType('tableview.ui')


data = [
    ['ID', 'A', 'B', 'C', 'D'],
    ['1', 'x', 'x', 'y', 'z'],
    ['2', 'z', 'x', 'y', 'x'],
    ['3', 'y', 'x', 'z', 'z'],
]


class MainDialog(_base):
    def __init__(self):
        super(MainDialog, self).__init__()

        # Set up the user interface from Designer.
        self.ui = _ui_cls()
        self.ui.setupUi(self)
        model = ArrayTableModel(data)
        # model = get_sql_model()
        # model = query_sql_model('''
        #   SELECT tracks.Name, Title, artists.Name as Artist
        #   FROM tracks
        #   JOIN albums USING (AlbumId)
        #   JOIN artists USING (ArtistId)
        # ''')

        tableView = self.ui.tableView
        tableView.setModel(model)
        tableView.horizontalHeader().setStretchLastSection(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainDialog()
    window.show()
    ret = app.exec_()
    sys.exit(ret)
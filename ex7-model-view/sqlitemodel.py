from PyQt5 import QtSql


def get_sql_model():
    db = QtSql.QSqlDatabase('QSQLITE')
    db.setDatabaseName('db/chinook.db')
    db.open()

    model = QtSql.QSqlRelationalTableModel(db=db)

    model.setTable('tracks')
    model.setRelation(2, QtSql.QSqlRelation('albums', 'AlbumId', 'Title'))
    model.setRelation(3, QtSql.QSqlRelation('media_types', 'MediaTypeId', 'Name'))
    model.setRelation(4, QtSql.QSqlRelation('genres', 'GenreId', 'Name'))

    model.setEditStrategy(QtSql.QSqlTableModel.OnManualSubmit)
    model.select()
    # model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
    # model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
    # model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")
    return model
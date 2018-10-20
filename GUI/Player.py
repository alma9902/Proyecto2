import sys
from ..reproductor.database import database
from ..reproductor.getFiles import getFiles
from ..reproductor.consultas import consultas
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
        QGroupBox, QHBoxLayout, QLabel, QLineEdit, QTreeView, QVBoxLayout,
        QWidget,QDialogButtonBox, QPushButton, QDialog, QPushButton)

from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt,
        QTime)


class Player(QWidget):
    TITLE, PERFORMER, ALBUM, TRACK, YEAR, GENRE = range(6)
    def __init__(self):
        super().__init__()
        self.title = 'Proyecto2'
        self.left = 10
        self.top = 10
        self.width =1000
        self.height = 800
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.dataGroupBox = QGroupBox("player")
        self.dataView = QTreeView()
        self.dataView.setRootIsDecorated(False)
        self.dataView.setAlternatingRowColors(True)

        mina = QPushButton("Minar")
        mina.clicked.connect(self.on_click)

        self.busqueda = QLineEdit(self)
        self.busqueda.setPlaceholderText("Búsqueda")

        buscar = QPushButton("Buscar")
        buscar.clicked.connect(self.search)

        dataLayout = QHBoxLayout()

        dataLayout.addWidget(self.dataView)
        self.dataGroupBox.setLayout(dataLayout)

        model = self.createPlayerModel(self)
        self.dataView.setModel(model)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.dataGroupBox)
        mainLayout.addWidget(mina)
        mainLayout.addWidget(self.busqueda)
        mainLayout.addWidget(buscar)
        self.setLayout(mainLayout)
        self.show()

    def createPlayerModel(self,parent):
        model = QStandardItemModel(0,6,parent)
        model.setHeaderData(self.TITLE, Qt.Horizontal, "title")
        model.setHeaderData(self.PERFORMER, Qt.Horizontal, "Performer")
        model.setHeaderData(self.ALBUM, Qt.Horizontal, "Album")
        model.setHeaderData(self.TRACK, Qt.Horizontal, "Track")
        model.setHeaderData(self.YEAR, Qt.Horizontal, "Year")
        model.setHeaderData(self.GENRE, Qt.Horizontal, "Genre")
        return model

    def addSong(self, model, title, performer, album, track, year, genre):
        model.insertRow(0)
        model.setData(model.index(0, self.TITLE),title)
        model.setData(model.index(0, self.PERFORMER), performer)
        model.setData(model.index(0, self.ALBUM),album)
        model.setData(model.index(0, self.TRACK),track)
        model.setData(model.index(0, self.YEAR),year)
        model.setData(model.index(0, self.GENRE),genre)

    def search(self):
        print('oki'+self.busqueda.text())
        model = self.createPlayerModel(self)
        self.dataView.setModel(model)
        lista_canciones = consultas()
        rows = lista_canciones.get_rolas(self.busqueda.text())
        for song in rows:
            title = song[0]
            performer= song[1]
            album = song[2]
            track = song[3]
            year = song[4]
            genre = song[5]
            self.addSong(model,title, performer, album,track, year, genre)

    def on_click(self):
        model = self.createPlayerModel(self)
        self.dataView.setModel(model)
        minando = getFiles()
        minando.get_info()
        lista_canciones = database()
        rows = lista_canciones.show_rolas()
        num_rolas = len(rows)
        self.i =1
        for song in rows:
            title = song[0]
            performer= song[1]
            album = song[2]
            track = song[3]
            year = song[4]
            genre = song[5]
            self.addSong(model,title, performer, album,track, year, genre)
            self.i += 1

app= QApplication(sys.argv)
ex = Player()
sys.exit(app.exec_())

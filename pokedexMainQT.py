from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import Windows.windowMain as mainWindow
import data.pokeDatabase as database
from os import path

sqldb = database.pokeData()
dbfile = path.join(".", "data", "pokemonDatabase.db")
print(dbfile)
if path.isfile(dbfile):
    print("Database Exists; Openning Existing File")
elif not path.isfile(dbfile):
    sqldb.createDatabase(dbfile)
    print("success")

pokedex = QApplication([])
pokedex.setStyle('Fusion')
resolution = QtWidgets.QDesktopWidget().screenGeometry()
print(resolution.width())
print(resolution.height())

appWindow = mainWindow.windowMain(resolution)
appWindow.show()

pokedex.exec_()
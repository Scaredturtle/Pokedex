from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import Windows.windowMain as mainWindow
from os import path

pokedex = QApplication([])
pokedex.setStyle('Fusion')
resolution = QtWidgets.QDesktopWidget().screenGeometry()
print(resolution.width())
print(resolution.height())

appWindow = mainWindow.windowMain(resolution)
appWindow.show()

pokedex.exec_()
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import Windows.windowMain as mainWindow

pokedex = QApplication([])
pokedex.setStyle('Fusion')
resolution = QtWidgets.QDesktopWidget().screenGeometry()
#print(resolution.width())
#print(resolution.height())

appWindow = mainWindow.windowMain(resolution)
appWindow.show()

sys.exit(pokedex.exec_())
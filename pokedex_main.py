import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import windows.poke_main_window as main_window

pokedex = QApplication([])
pokedex.setStyle('Fusion')
#resolution = QtWidgets.QDesktopWidget().screenGeometry()
#print(resolution.width())
#print(resolution.height())

appWindow = main_window.pokedex_main_window()
appWindow.show()

sys.exit(pokedex.exec_())
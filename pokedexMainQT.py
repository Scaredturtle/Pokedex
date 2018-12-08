from PyQt5.QtWidgets import QApplication
import Windows.windowMain as mainWindow

pokedex = QApplication([])
pokedex.setStyle('Fusion')

appWindow = mainWindow.windowMain()
appWindow.show()

pokedex.exec_()
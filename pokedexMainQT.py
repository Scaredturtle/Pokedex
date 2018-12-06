from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QLineEdit
import DataGathering.WebGrab as gather

data = gather.Gather()

pokedex = QApplication([])
pokedex.setStyle('Fusion')

MWWidth = 800
MWHeight = 600
mainWindow = QMainWindow()
mainWindow.setWindowTitle('Improved Pokedex')
mainWindow.setGeometry(0, 0, MWWidth, MWHeight)
mainWindow.setStyleSheet("background-color: red;")


textLabel = QLabel(mainWindow)
textLabel.setText('Pokemon Name:')
textLabel.setGeometry(0, 0, 120, 30)
textLabel.setStyleSheet("background-color: cyan;")
pokemonEntry = QLineEdit(mainWindow)
pokemonEntry.setGeometry(121, 0, 150, 30)
pokemonEntry.setStyleSheet("background-color: white;")
pokemonEntry.returnPressed(data.dataCheck(pokemonEntry.text()))

mainWindow.show()
pokedex.exec_()
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QLineEdit, QPushButton, QCheckBox
from PyQt5.QtCore import Qt
import DataGathering.WebGrab as gather
import Windows.windowMain as mainWindow

data = gather.Gather()
pokedexButtonBackground = "background-color: cyan;"

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
textLabel.setStyleSheet(pokedexButtonBackground)

pokemonEntry = QLineEdit(mainWindow)
pokemonEntry.setText("*Name Here*")
pokemonEntry.setGeometry(121, 0, 150, 30)
pokemonEntry.setStyleSheet("background-color: white;")

searchButton = QPushButton(mainWindow)
searchButton.setText('Get Data!')
searchButton.setGeometry(272, 0, 75, 30)
searchButton.setStyleSheet(pokedexButtonBackground)

dataCheckBox = QCheckBox(mainWindow)
dataCheckBox.setText("Force Pull Data?")
dataCheckBox.setGeometry(348, 0, 100, 30)

pokemonEntry.returnPressed.connect(lambda: data.searchInit(pokemonEntry.text(), dataCheckBox.isChecked()))
searchButton.clicked.connect(lambda: data.searchInit(pokemonEntry.text(), dataCheckBox.isChecked()))

mainWindow.show()

pokedex.exec_()
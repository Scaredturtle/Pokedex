from PyQt5.QtWidgets import QLabel, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout, QCheckBox, QDesktopWidget
import DataGathering.dataGrab as gather
import math

class windowMain(QMainWindow):
    def __init__(self, resolution):
        super().__init__()

        self.data = gather.Gather()
        self.windowBk = "background-color: red;"
        self.widgetBk = "background-color: cyan;"
        self.setWindowTitle("Improved Pokedex")
        self.resolution = resolution
        self.windowWidth = 800
        self.windowHeight = 600
        self.hpos = (self.resolution.width() - self.windowWidth)/2
        self.vpos = (self.resolution.height() - self.windowHeight)/2

        self.initUI()

    def initUI(self):
        self.setStyleSheet(self.windowBk)
        self.mainLabel = QLabel(self)
        self.mainText = QLineEdit(self)
        self.searchButton = QPushButton(self)
        self.dataCheckBox = QCheckBox(self)

        self.resize(self.windowWidth, self.windowHeight)
        self.move(self.hpos, self.vpos)

        self.mainLabel.setText("Pokemon Name:")
        self.mainLabel.setStyleSheet(self.widgetBk)
        self.mainLabel.setGeometry(0, 0, 120, 30)

        self.mainText.setStyleSheet("background-color: white;")
        self.mainText.setGeometry(121, 0, 150, 30)

        self.searchButton.setText('Get Data!')
        self.searchButton.setGeometry(272, 0, 75, 30)
        self.searchButton.setStyleSheet(self.widgetBk)

        self.dataCheckBox.setText("Force Pull Data?")
        self.dataCheckBox.setGeometry(348, 0, 100, 30)
        self.dataCheckBox.setStyleSheet(self.widgetBk)

        self.mainText.returnPressed.connect(lambda: self.data.searchInit(self.mainText.text(), self.dataCheckBox.isChecked()))
        self.searchButton.clicked.connect(lambda: self.data.searchInit(self.mainText.text(), self.dataCheckBox.isChecked()))
from PyQt5.QtWidgets import QLabel, QMainWindow, QWidget, QLineEdit, QPushButton, QVBoxLayout
import DataGathering.WebGrab as gather

class windowMain():
    def __init__(self):
        super().__init__()

        self.data = gather.Gather()
        self.widgetbk = "background-color: cyan;"

        self.initUI()

    def initUI(self):
        self.mainUI = QMainWindow()
        self.mainLabel = QLabel(self.mainUI)
        self.mainText = QLineEdit(self.mainUI)

        self.mainUI.setGeometry(0, 0, 800, 600)

        self.mainLabel.setText("Pokemon Name:")
        self.mainLabel.setStyleSheet(self.widgetbk)
        self.mainLabel.setGeometry(0, 0, 120, 30)

        self.mainText.setStyleSheet("background-color: white;")
        self.mainText.setGeometry(121, 0, 150, 30)
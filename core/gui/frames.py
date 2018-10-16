from PyQt5.QtWidgets import (
    QMainWindow, QPushButton
)
from PyQt5 import QtCore
from core.constants.styles import MAIN_STYLE


class MainFrame(QMainWindow):

    def __init__(self, left=50, top=50, width=1024, height=600):
        super().__init__()
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        self.music_button = QPushButton(self)
        self.utility_button = QPushButton(self)
        self.nav_button = QPushButton(self)
        self.diag_button = QPushButton(self)

        self.init_ui()

    def init_ui(self):
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setObjectName('main_frame')
        self.setStyleSheet(MAIN_STYLE)

        self.music_button.setGeometry(0, 0, self.height * 0.25, self.height * 0.25)
        self.music_button.setObjectName('music_button')

        self.utility_button.setGeometry(0, self.height * 0.25, self.height * 0.25, self.height * 0.25)
        self.utility_button.setObjectName('utility_button')

        self.nav_button.setGeometry(0, 0 + self.height * 0.25 * 2, self.height * 0.25, self.height * 0.25)
        self.nav_button.setObjectName('nav_button')

        self.diag_button.setGeometry(0, 0 + self.height * 0.25 * 3, self.height * 0.25, self.height * 0.25)
        self.diag_button.setObjectName('diag_button')

        self.show()

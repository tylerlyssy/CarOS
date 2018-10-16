import sys
from core.gui.frames import MainFrame
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainFrame()
    sys.exit(app.exec_())

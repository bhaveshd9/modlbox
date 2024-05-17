from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from MainWindow import MyMainWindow

import sys

app = QApplication(sys.argv)

window = MyMainWindow()

window.show()

app.exec()
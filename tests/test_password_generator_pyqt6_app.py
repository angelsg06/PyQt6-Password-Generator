import sys
import random
import string
from PyQt6 import QtWidgets

# Subclass QMainWindow to customize your application's main window
class PasswordGenerator(QtWidgets.QtWidget):
    def __init__(self):
        super().__init__()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
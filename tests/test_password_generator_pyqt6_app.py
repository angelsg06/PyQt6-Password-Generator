import sys
from PyQt6 import QtWidgets, QtCore, QtGui

# Subclass QMainWindow to customize your application's main window
class PasswordGenerator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # set window title
        self.setWindowTitle("Password Generator")
        
        # Create a central widget that contains all the elements
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        # create a vertical box layout for the central widget

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())
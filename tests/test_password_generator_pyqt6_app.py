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
        layout = QtWidgets.QVBoxLayout(central_widget)

        # creates the widget variables for: labels, spinbox, checkboxes, buttons
        password_length_label = QtWidgets.QLabel("Password Length(1-15):")
        self.password_length = QtWidgets.QSpinBox()
        self.include_lowercase = QtWidgets.QCheckBox("Include Lowercase Letters")
        self.include_uppercase = QtWidgets.QCheckBox("Include Uppercase Letters")
        self.include_numbers = QtWidgets.QCheckBox("Include Numbers")
        self.include_symbols = QtWidgets.QCheckBox("Include Symbols")
        generate_button = QtWidgets.QPushButton("Generate Password")
        clear_button = QtWidgets.QPushButton("Clear")
        self.password_display = QtWidgets.QLabel()

        # Adds the widgets to the layout
        layout.addWidget(password_length_label)
        layout.addWidget(self.password_length)
        layout.addWidget(self.include_lowercase)
        layout.addWidget(self.include_uppercase)
        layout.addWidget(self.include_numbers)
        layout.addWidget(self.include_symbols)
        layout.addWidget(generate_button)
        layout.addWidget(clear_button)
        layout.addWidget(self.password_display)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())
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
        self.password_length_spinbox = QtWidgets.QSpinBox()
        self.include_lowercase_checkbox = QtWidgets.QCheckBox("Include Lowercase Letters")
        self.include_uppercase_checkbox = QtWidgets.QCheckBox("Include Uppercase Letters")
        self.include_numbers_checkbox = QtWidgets.QCheckBox("Include Numbers")
        self.include_symbols_checkbox = QtWidgets.QCheckBox("Include Symbols")
        generate_button = QtWidgets.QPushButton("Generate Password")
        clear_button = QtWidgets.QPushButton("Clear")
        self.password_display_label = QtWidgets.QLabel()
        clear_button.clicked.connect(self.clear_fields)

        self.password_length_spinbox.setRange(1,15)

        # Adds the widgets to the layout
        layout.addWidget(password_length_label)
        layout.addWidget(self.password_length_spinbox)
        layout.addWidget(self.include_lowercase_checkbox)
        layout.addWidget(self.include_uppercase_checkbox)
        layout.addWidget(self.include_numbers_checkbox)
        layout.addWidget(self.include_symbols_checkbox)
        layout.addWidget(generate_button)
        layout.addWidget(clear_button)
        layout.addWidget(self.password_display_label)
    
    def clear_fields(self):
        self.password_length_spinbox.clear()
        self.include_lowercase_checkbox.setChecked(False)
        self.include_uppercase_checkbox.setChecked(False)
        self.include_numbers_checkbox.setChecked(False)
        self.include_symbols_checkbox.setChecked(False)

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec())
import sys
import string
import random
from PyQt6 import QtWidgets, QtCore, QtGui

# Subclass QMainWindow to customize your application's main window
class PasswordGenerator(QtWidgets.QtWidget):
    def __init__(self):
        super().__init__()  

        # Creates the widget variables for: labels, spinbox, checkboxes, buttons
        password_length_label = QtWidgets.QLabel("Password Length(1-15):")
        self.password_length_spinbox = QtWidgets.QSpinBox()
        self.include_lowercase_checkbox = QtWidgets.QCheckBox("Include Lowercase Letters")
        self.include_uppercase_checkbox = QtWidgets.QCheckBox("Include Uppercase Letters")
        self.include_numbers_checkbox = QtWidgets.QCheckBox("Include Numbers")
        self.include_symbols_checkbox = QtWidgets.QCheckBox("Include Symbols")
        generate_button = QtWidgets.QPushButton("Generate Password")
        clear_button = QtWidgets.QPushButton("Clear")
        self.password_display_label = QtWidgets.QLabel()

        # Connects button to clear fields function
        clear_button.clicked.connect(self.clear_fields)

        generate_button.clicked.connect(self.generate_password)

        # Sets range of spinbox to desired amount
        self.password_length_spinbox.setRange(1,15)

        # Adds the widgets to the layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(password_length_label)
        layout.addWidget(self.password_length_spinbox)
        layout.addWidget(self.include_lowercase_checkbox)
        layout.addWidget(self.include_uppercase_checkbox)
        layout.addWidget(self.include_numbers_checkbox)
        layout.addWidget(self.include_symbols_checkbox)
        layout.addWidget(generate_button)
        layout.addWidget(clear_button)
        layout.addWidget(self.password_display_label)
        self.setLayout(layout)
    
        # Clears all of users input 
    def clear_fields(self):
        self.password_length_spinbox.clear()
        self.include_lowercase_checkbox.setChecked(False)
        self.include_uppercase_checkbox.setChecked(False)
        self.include_numbers_checkbox.setChecked(False)
        self.include_symbols_checkbox.setChecked(False)
        self.password_display_label.setText("")

    def generate_password(self):
        length = self.password_length_spinbox.value()
        if length > 15:
            self.password_display_label.setText("Errpr: Password length cannot exceed 15")
            return
        
        allowed_chars = ''
        if self.include_lowercase_checkbox.isChecked():
            allowed_chars += string.ascii_lowercase
        if self.include_uppercase_checkbox.isChecked():
            allowed_chars += string.ascii_uppercase
        if self.include_numbers_checkbox.isChecked():
            allowed_chars += string.digits
        if self.include_symbols_checkbox.isChecked():
            allowed_chars += string.punctuation
        
        if not allowed_chars:
            self.password_display_label.setText("Error: Please select at least one character")
            return

        password = ''.join(random.choice(allowed_chars) for _ in range(length))
        self.password_display_label.setText(f"Generated Password: {password}")
     
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PasswordGenerator()
     # Set window title
    window.setWindowTitle("Password Generator")
    window.show()
    sys.exit(app.exec())
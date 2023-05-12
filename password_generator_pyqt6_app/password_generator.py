import sys
import string
import random

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget ,QCheckBox, QSpinBox, QLabel, QVBoxLayout
)
 
# Subclass QMainWindow to customize your application's main window
class PasswordGenerator(QMainWindow):
    def __init__(self):
        super().__init__()  

        # Styles main window, fixed size and background color
        self.setFixedSize(460, 440)
        self.setStyleSheet("background-color: #ADD8E6;")
        
        # Creates the widget variable for the disclaimer at the top of the app
        disclaimer_label_1 = QLabel("Disclaimer: The recommended password length is 12 digits long!")
        disclaimer_label_2 = QLabel("Also, the password is AUTOMATICALLY copied to the clipboard!")

        # Creates the widget variable for the password length label
        password_length_label = QLabel("Password Length(1-15):")
        password_length_label.setFont(QFont("Arial", 12))

        # Creates a widget variable for the checkbox to include lowercase letters
        self.password_length_spinbox = QSpinBox()
        self.include_lowercase_checkbox = QCheckBox("Include Lowercase Letters")
        self.include_lowercase_checkbox.setStyleSheet("QCheckBox::indicator:checked {background-color: red}")

        # Creates a widget variable for the checkbox to include uppercase letters
        self.include_uppercase_checkbox = QCheckBox("Include Uppercase Letters")
        self.include_uppercase_checkbox.setStyleSheet("QCheckBox::indicator:checked {background-color: green}")

        # Creates a widget variable for the checkbox to include numbers
        self.include_numbers_checkbox = QCheckBox("Include Numbers")
        self.include_numbers_checkbox.setStyleSheet("QCheckBox::indicator:checked {background-color: blue}")

        # Creates a widget variable for the checkbox to include symbols
        self.include_symbols_checkbox = QCheckBox("Include Symbols")
        self.include_symbols_checkbox.setStyleSheet("QCheckBox::indicator:checked {background-color: violet}")

        # Creates a widget variable for the generate and clear button as well as styling for both
        generate_button = QPushButton("Generate Password")
        clear_button = QPushButton("Clear")
        self.password_display_label = QLabel()
        self.password_display_label.setFont(QFont("Verdana", 10))

        # Connects button to clear fields and generate password functions
        clear_button.clicked.connect(self.clear_fields)
        generate_button.clicked.connect(self.generate_password)

        # Sets range of spinbox to desired amount
        self.password_length_spinbox.setRange(1,15)

        # Adds the widget variables to the main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.addWidget(disclaimer_label_1)
        main_layout.addWidget(disclaimer_label_2)
        main_layout.addWidget(password_length_label)
        main_layout.addWidget(self.password_length_spinbox)
        main_layout.addWidget(self.include_lowercase_checkbox)
        main_layout.addWidget(self.include_uppercase_checkbox)
        main_layout.addWidget(self.include_numbers_checkbox)
        main_layout.addWidget(self.include_symbols_checkbox)
        main_layout.addWidget(generate_button)
        main_layout.addWidget(clear_button)
        main_layout.addWidget(self.password_display_label)     
    
    # Define the clear_fields method to clear all user input 
    def clear_fields(self):
        self.password_length_spinbox.clear()
        self.include_lowercase_checkbox.setChecked(False)
        self.include_uppercase_checkbox.setChecked(False)
        self.include_numbers_checkbox.setChecked(False)
        self.include_symbols_checkbox.setChecked(False)
        self.password_display_label.setText("")

    # Define the generate_password method to create a password
    def generate_password(self):
        length = self.password_length_spinbox.value()
        # Check that the length is within the specified range
        if length > 15:
            self.password_display_label.setText("Errpr: Password length cannot exceed 15")
            return
        
        allowed_chars = ''
        # Determine which characters to include based on the user's selections
        if self.include_lowercase_checkbox.isChecked():
            allowed_chars += string.ascii_lowercase
        if self.include_uppercase_checkbox.isChecked():
            allowed_chars += string.ascii_uppercase
        if self.include_numbers_checkbox.isChecked():
            allowed_chars += string.digits
        if self.include_symbols_checkbox.isChecked():
            allowed_chars += string.punctuation
        # Check that at least one character type is selected
        if not allowed_chars:
            self.password_display_label.setText("Error: Please select at least one character")
            return
        # Generate the password using the selected characters
        password = ''.join(random.choice(allowed_chars) for _ in range(length))
        self.password_display_label.setText(f"Generated Password: {password}")
        clipboard = QApplication.clipboard()
        clipboard.setText(password)
     
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
     # Set window title
    window.setWindowTitle("Password Generator")
    window.show()
    sys.exit(app.exec())
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit,
                             QFormLayout, QDesktopWidget, QHBoxLayout)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """
        Initialize the window, adjust its size to 1/3 of the screen, display its contents, and
        position the title in the top right.
        """
        self.setWindowTitle('My first UI')
        self.adjustWindowSize()

        # Set window style
        self.setFont(QFont('Arial', 10))
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))  # Light grey background
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))  # Black font color
        self.setPalette(palette)

        # Main layout
        main_layout = QVBoxLayout()

        # Title layout
        title_layout = QHBoxLayout()
        title = QLabel('My first UI')
        title.setFont(QFont('Arial', 24, QFont.Bold))
        title.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        title_layout.addWidget(title)
        main_layout.addLayout(title_layout)

        # Form layout for input fields
        form_layout = QFormLayout()
        
        name_input = QLineEdit()
        surname_input = QLineEdit()
        birthday_input = QLineEdit()
        gender_input = QLineEdit()

        form_layout.addRow("Name:", name_input)
        form_layout.addRow("Surname:", surname_input)
        form_layout.addRow("Birthday:", birthday_input)
        form_layout.addRow("Gender:", gender_input)

        # Submit button
        submit_button = QPushButton('Submit')
        submit_button.setFont(QFont('Arial', 12))
        submit_button.setStyleSheet("QPushButton {background-color: #A3C1DA; color: black;}")

        # Add form layout and submit button to the main layout
        main_layout.addLayout(form_layout)
        main_layout.addWidget(submit_button)

        self.setLayout(main_layout)

    def adjustWindowSize(self):
        """
        Adjust the window size to be 1/3 of the screen's width and height.
        """
        screen = QDesktopWidget().screenGeometry()  # Retrieves the screen geometry
        width, height = screen.width() // 3, screen.height() // 3
        self.setGeometry((screen.width() - width) // 2, (screen.height() - height) // 2, width, height)
        self.setFixedSize(self.size())  # Ensure the size is fixed to the one specified.


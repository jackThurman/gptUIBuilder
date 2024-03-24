import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QDesktopWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

class window(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
    
        self.setWindowTitle('My first UI')
        self.adjustWindowSize()

        # Set window style
        self.setFont(QFont('Arial', 10))
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(240, 240, 240))  # Light grey background
        palette.setColor(QPalette.WindowText, QColor(0, 0, 0))  # Black font color
        self.setPalette(palette)

        # Create layout and widgets
        layout = QVBoxLayout()

        title = QLabel('My first UI')
        title.setFont(QFont('Arial', 16, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        
        placeholder = QLabel('Placeholder Element')
        placeholder.setFont(QFont('Arial', 12))
        placeholder.setAlignment(Qt.AlignCenter)

        # Add widgets to layout
        layout.addWidget(title)
        layout.addWidget(placeholder)

        self.setLayout(layout)

    def adjustWindowSize(self):
        """
        Adjust the window size to be 1/3 of the screen's width and height.
        """
        screen = QDesktopWidget().screenGeometry()  # Retrieves the screen geometry
        width, height = screen.width() // 2, screen.height() // 2
        self.setGeometry((screen.width() - width) // 2, (screen.height() - height) // 2, width, height)
        self.setFixedSize(self.size())  # Ensure the size is fixed to the one specified.
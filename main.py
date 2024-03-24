from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import subprocess
import sys
import os
import chatCompletion as cc
from openai import OpenAI

client = OpenAI()
destinationPath = 'UI.py'

class GPTUIBuilder(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('GPT UI Builder')
        self.setGeometry(300, 300, 600, 400)
        
        layout = QVBoxLayout()

        # Title label
        titleLabel = QLabel('GPT UI Builder', self)
        titleLabel.setFont(QFont('Arial', 18, QFont.Bold))
        titleLabel.setAlignment(Qt.AlignCenter)

        # Text input field
        self.textInput = QTextEdit(self)
        self.textInput.setFont(QFont('Arial', 12))
        self.textInput.setPlaceholderText('Enter your prompt here...')

        # Create button
        createButton = QPushButton('CREATE', self)
        createButton.setFont(QFont('Arial', 12, QFont.Bold))
        createButton.clicked.connect(lambda: cc.create(client,self.textInput,destinationPath,app))

        layout.addWidget(titleLabel)
        layout.addWidget(self.textInput)
        layout.addWidget(createButton)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainUI = GPTUIBuilder()
    mainUI.show()
    sys.exit(app.exec_())

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import subprocess
import sys
import os
from openai import OpenAI

client = OpenAI()

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
        self.textInput = QLineEdit(self)
        self.textInput.setFont(QFont('Arial', 12))
        self.textInput.setPlaceholderText('Enter your prompt here...')

        # Create button
        createButton = QPushButton('CREATE', self)
        createButton.setFont(QFont('Arial', 12, QFont.Bold))
        createButton.clicked.connect(self.onSend)

        layout.addWidget(titleLabel)
        layout.addWidget(self.textInput)
        layout.addWidget(createButton)

        self.setLayout(layout)

    def onSend(self):
        prompt = self.textInput.text()
        exampleResponse = open('example.py','r').read()
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a python developer who is an expert using PyQt5. You only return code in your response"},
                {"role": "user", "content": "Generate me some python code using PyQt5 that will create a UI with a label saying 'Jack'. Return code only."},
                {"role": "system", "content": exampleResponse},
                {"role": "user", "content": prompt},
            ]
        )
        generated_code = response.choices[0].message.content
        clean_code = self.cleanResponse(generated_code)
        self.updateUIFile(clean_code)
        self.textInput.clear()
        self.runUIFile()


    def updateUIFile(self, code):
        with open('UI.py', 'w') as file:
            file.write("\n" + code)

    def runUIFile(self):
        script_path = 'UI.py'
        venv_python_path = os.path.join('.venv', 'Scripts', 'python.exe')  
        try:
            subprocess.run([venv_python_path,script_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running {script_path}: {e}")
        finally:
            QApplication.instance().quit()
            sys.exit()

    def cleanResponse(self, response):
        cleaned_response = response.strip()

        if cleaned_response.startswith('```python'):
            cleaned_response = cleaned_response[len('```python'):].strip()
        if cleaned_response.endswith('```'):
            cleaned_response = cleaned_response[:-len('```')].strip()

        return cleaned_response


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = GPTUIBuilder()
    ex.show()
    sys.exit(app.exec_())

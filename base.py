from PyQt5.QtWidgets import QMainWindow

class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('window')
        self.setGeometry(560, 240, 800, 600)  # Set position and size (x, y, width, height)


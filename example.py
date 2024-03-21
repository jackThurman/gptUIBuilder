from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sys

class SimpleUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Simple UI')
        layout = QVBoxLayout()

        # Creating a label
        label = QLabel('Jack', self)

        # Adding the label to the layout
        layout.addWidget(label)

        # Setting the layout for the main window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SimpleUI()
    ex.show()
    sys.exit(app.exec_())

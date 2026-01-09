# Signals Triggers and Events

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("This is Joshua! Uraaah")

        self.button = QPushButton("Press")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.click_button)
        self.button.clicked.connect(self.toggle_button)

        self.setCentralWidget(self.button)

    def click_button(self):
        self.button.setText("Disabled")
        self.button.setEnabled(True)
        print("Clicked!")

    def toggle_button(self, checked):
        self.button_checked = checked

        print("Check the label mommy", checked)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
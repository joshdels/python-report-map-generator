# Signals Triggers and Events

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Uraaah")

        self.button = QPushButton("Press True")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.toggle_button)

        self.setCentralWidget(self.button)

    def toggle_button(self, checked):
        """State True or false and changes the button UI"""
        if checked:
            self.button.setText("Press False")
            print("State is TRUE")
        else:
            self.button.setText("Press True")
            print("State is FALSE")

    print("Check state", checked)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()

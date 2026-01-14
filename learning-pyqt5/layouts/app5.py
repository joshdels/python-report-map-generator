# Grid

import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QGridLayout,
)
from color_layout1 import Color


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        layout = QGridLayout()
        
        layout.addWidget(Color('red'), 0,0)
        layout.addWidget(Color('green'), 1,0)
        layout.addWidget(Color('red'), 1,1)
        layout.addWidget(Color('green'), 1,3)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
     


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

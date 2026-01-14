import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from PyQt5.uic import loadUi #load this lib

class Window(QMainWindow):
    """Main Window."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.centralWidget = QPushButton("Employee...")
        self.centralWidget.clicked.connect(self.onEmployeeBtnClicked)
        self.setCentralWidget(self.centralWidget)

    def onEmployeeBtnClicked(self):
        """Launch the employee dialog"""
        dlg = EmployeeDlg(self)
        dlg.exec()


class EmployeeDlg(QDialog):
    """Subclass, Employee Dialog"""

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("employee.ui",self) #load the ui file


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

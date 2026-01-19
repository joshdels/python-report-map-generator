import sys

from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton

from employee_dlg import Ui_Dialog


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
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        
        self.resize(900, 500)
        self.setWindowTitle("Test PyQt5 v0.1")
        label_test = QtWidgets.QLabel(self)
        label_test.setGeometry(50, 50, 800, 200)
        label_test.setFont(QtGui.QFont("Courier New", 56, QtGui.QFont.Bold))
        label_test.setText("Test PyQt5 QLabel.")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = main_window()
    main_win.show()
    sys.exit(app.exec_()) 
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        
        self.resize(900, 500)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = main_window()
    main_win.show()
    sys.exit(app.exec_()) 
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        
        self.resize(900, 500)
        self.setWindowTitle("Test PyQt5 v0.1")
        self.label_test = QtWidgets.QLabel(self)
        self.label_test.setGeometry(50, 50, 800, 200)
        self.label_test.setFont(QtGui.QFont("Courier New", 40, QtGui.QFont.Bold))
        self.label_test.setText("Test PyQt5 QLabel.")
                
        start_button = QtWidgets.QPushButton(self)
        start_button.setGeometry(50, 300, 150, 70)
        start_button.setText("Start")
        start_button.setFont(QtGui.QFont("Times", 32, QtGui.QFont.Normal))
        start_button.clicked.connect(self.start_button_onclick)
        
        stop_button = QtWidgets.QPushButton(self)
        stop_button.setGeometry(250, 300, 150, 70)
        stop_button.setText("Stop")
        stop_button.setFont(QtGui.QFont("Times", 32, QtGui.QFont.Normal))
        stop_button.clicked.connect(self.stop_button_onclick)

        old_list = [1, 2, 3, 4, 5]
        self.list_widget = QtWidgets.QListWidget(self)
        self.list_widget.setGeometry(500, 200, 150, 200)
        for item in old_list:
            #self.list_widget.addItem("%s" % old_list[0])
            self.list_widget.addItem(f"{item}")

    def start_button_onclick(self):
        self.label_test.setText("Start")

    def stop_button_onclick(self):
        self.label_test.setText("Stop")
        self.list_widget.clear()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = main_window()
    main_win.show()
    sys.exit(app.exec_()) 
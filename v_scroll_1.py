import sys

# from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,
#                              QApplication, QHBoxLayout, QVBoxLayout, QMainWindow)
from PyQt5.QtWidgets import (QWidget, QLabel, QScrollArea, QVBoxLayout, QMainWindow)

# from PyQt5.QtCore import Qt, QSize
from PyQt5.QtCore import Qt

from PyQt5 import QtWidgets


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.vbox = None
        self.widget = None
        self.scroll = None

        self.init_ui()

    def init_ui(self):
        self.scroll = QScrollArea()       # Scroll Area which contains the widgets, set as the centralWidget
        self.widget = QWidget()           # Widget that contains the collection of Vertical Box
        self.vbox = QVBoxLayout()         # The Vertical Box that contains the Horizontal Boxes of  labels and buttons

        for i in range(1, 101):
            obj = QLabel("TextLabel: " + str(i))
            self.vbox.addWidget(obj)

        self.widget.setLayout(self.vbox)

        # Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        self.setGeometry(600, 100, 500, 500)
        self.setWindowTitle('Scroll Area Demonstration')
        self.show()

        return


def main():
    # app = PyQt5.QtWidgets.QApplication(sys.argv)
    # app.setStyle('Fusion')
    app = QtWidgets.QApplication(sys.argv)

    app_window_main = MainWindow()
    app_window_main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

# 385 in file main.py

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QScrollArea, QMainWindow


class ScrollableButtonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        scroll = QScrollArea()
        widget = QWidget()
        layout = QVBoxLayout()

        for i in range(20):
            button = QPushButton(f"Button {i+1}")
            layout.addWidget(button)

        widget.setLayout(layout)
        scroll.setWidgetResizable(True)
        scroll.setWidget(widget)

        self.setCentralWidget(scroll)
        self.setWindowTitle('Scrollable Button Window')
        self.setGeometry(100, 100, 300, 400)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ScrollableButtonWindow()
    window.show()
    sys.exit(app.exec_())

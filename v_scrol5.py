import sys
from PyQt5.Qt import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.widget = QWidget()
        self.vbox = QVBoxLayout(self.widget)

        for i in range(20):
            w = QWidget()
            hbox = QHBoxLayout(w)
            label = QLabel(f'Label {i}')
            lineEdit = QLineEdit(f'LineEdit {i}')
            button = QPushButton(f'Button {i}')
            hbox.addWidget(label)
            hbox.addWidget(lineEdit)
            hbox.addWidget(button)
            
            button.clicked.connect(lambda ch, lb=label, le=lineEdit: print(
                f'label -> {lb.text()}, lineEdit -> {le.text()}'
            ))
            self.vbox.addWidget(w)

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.setWindowTitle('Title MainWindow')
    main.resize(500, 300)
    main.show()                    
    sys.exit(app.exec_())

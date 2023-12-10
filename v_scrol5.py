import sys
from PyQt5.Qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Title MainWindow')
        self.resize(500, 300)

        # self.centralwidget = QWidget(MainWindow)
        # self.centralwidget.setObjectName(u"centralwidget")
        # self.widget = QWidget(self.centralwidget)
        # self.widget.setObjectName(u"widget")
        # self.widget.setGeometry(QRect(20, 20, 381, 301))
        # MainWindow.setCentralWidget(self.centralwidget)

        self.widget0 = QWidget()
        self.widget0.resize(100, 100)
        self.vbox0 = QVBoxLayout(self.widget0)

        self.widget = QWidget()
        self.widget.resize(100, 100)
        self.vbox = QVBoxLayout(self.widget)

        w = QWidget()
        hbox = QHBoxLayout(w)
        label = QLabel(f'Label---')
        lineEdit = QLineEdit(f'LineEdit---')
        button = QPushButton(f'Button---')
        hbox.addWidget(label)
        hbox.addWidget(lineEdit)
        hbox.addWidget(button)
        self.vbox.addWidget(w)

        w = QWidget()
        hbox = QHBoxLayout(w)
        label1 = QLabel(f'Label---1')
        label2 = QLabel(f'Label---2')
        label3 = QLabel(f'Label---3')
        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        self.vbox.addWidget(w)

        for i in range(1, 15+1):
            w = QWidget()
            hbox = QHBoxLayout(w)

            label = QLabel(f'Label {i}')
            lineEdit = QLineEdit(f'LineEdit {i}')
            button = QPushButton(f'Button {i}')

            hbox.addWidget(label)
            hbox.addWidget(lineEdit)
            hbox.addWidget(button)
            
            button.clicked.connect(lambda ch, lb=label, le=lineEdit: print(
                f'label -> {lb.text()}, lineEdit -> {le.text()}'))
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
    # main.setWindowTitle('Title MainWindow')
    # main.resize(500, 300)
    main.show()                    
    sys.exit(app.exec_())

    # self.verticalSpacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    # self.verticalLayout.addItem(self.verticalSpacer1)
    # self.horizontalLayout = QHBoxLayout()
    # self.horizontalLayout.setObjectName(u"horizontalLayout")
    # self.horizontalSpacer1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    # self.horizontalLayout.addItem(self.horizontalSpacer1)
    # self.horizontalSpacer2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    # self.horizontalLayout.addItem(self.horizontalSpacer2)
    # self.verticalLayout.addLayout(self.horizontalLayout)
    # self.verticalSpacer2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    # self.verticalLayout.addItem(self.verticalSpacer2)

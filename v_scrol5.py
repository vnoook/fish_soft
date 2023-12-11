import sys
import PyQt5.Qt
import PyQt5.QtGui
import PyQt5.QtCore
import PyQt5.QtWidgets

class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Title MainWindow')
        self.resize(500, 500)

        self.centralwidget = PyQt5.QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)

        self.widget1 = PyQt5.QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(PyQt5.QtCore.QRect(10, 10, 200, 200))
        # self.widget1.resize(200, 500)

        self.widget2 = PyQt5.QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(PyQt5.QtCore.QRect(10, 200, 200, 200))
        # self.widget2.resize(200, 500)

        self.vbox1 = PyQt5.QtWidgets.QVBoxLayout(self.widget1)
        self.vbox2 = PyQt5.QtWidgets.QVBoxLayout(self.widget2)

        w1 = PyQt5.QtWidgets.QWidget()
        hbox1 = PyQt5.QtWidgets.QHBoxLayout(w1)
        label1 = PyQt5.QtWidgets.QLabel(f'Label---')
        lineEdit1 = PyQt5.QtWidgets.QLineEdit(f'LineEdit---')
        button1 = PyQt5.QtWidgets.QPushButton(f'Button---')
        hbox1.addWidget(label1)
        hbox1.addWidget(lineEdit1)
        hbox1.addWidget(button1)
        self.vbox1.addWidget(w1)

        w2 = PyQt5.QtWidgets.QWidget()
        hbox2 = PyQt5.QtWidgets.QHBoxLayout(w2)
        label2 = PyQt5.QtWidgets.QLabel(f'Label---')
        lineEdit2 = PyQt5.QtWidgets.QLineEdit(f'LineEdit---')
        button2 = PyQt5.QtWidgets.QPushButton(f'Button---')
        hbox2.addWidget(label2)
        hbox2.addWidget(lineEdit2)
        hbox2.addWidget(button2)
        self.vbox2.addWidget(w2)

        # self.widget = PyQt5.QtWidgets.QWidget()
        # self.widget.resize(100, 100)
        # self.vbox = PyQt5.QtWidgets.QVBoxLayout(self.widget)

        # for i in range(1, 15+1):
        #     w = PyQt5.QtWidgets.QWidget()
        #     hbox = PyQt5.QtWidgets.QHBoxLayout(w)
        #
        #     label = PyQt5.QtWidgets.QLabel(f'Label {i}')
        #     lineEdit = PyQt5.QtWidgets.QLineEdit(f'LineEdit {i}')
        #     button = PyQt5.QtWidgets.QPushButton(f'Button {i}')
        #
        #     hbox.addWidget(label)
        #     hbox.addWidget(lineEdit)
        #     hbox.addWidget(button)
        #
        #     button.clicked.connect(lambda ch, lb=label, le=lineEdit: print(
        #         f'label -> {lb.text()}, lineEdit -> {le.text()}'))
        #     self.vbox2.addWidget(w)

        # self.scroll = PyQt5.QtWidgets.QScrollArea()
        # self.scroll.setVerticalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOn)
        # self.scroll.setHorizontalScrollBarPolicy(PyQt5.QtCore.Qt.ScrollBarAlwaysOff)
        # self.scroll.setWidgetResizable(True)
        # self.scroll.setWidget(self.widget2)
        #
        # self.setCentralWidget(self.scroll)


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
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

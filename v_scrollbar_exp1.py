import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Login(QtWidgets.QWidget): 

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('First')

    def setupUi(self, FirstWindow):
        FirstWindow.setObjectName("First")
        FirstWindow.setEnabled(True)
        FirstWindow.resize(675, 776)

        FirstWindow.setFocusPolicy(QtCore.Qt.TabFocus)


        self.spinBoxNUM = QtWidgets.QSpinBox()
        self.spinBoxLEVELS  = QtWidgets.QSpinBox()
        self.spinBoxLEVELS.setValue(2)
        self.spinBoxLEVELS.setMaximum(156)

        self.QuitButton      = QtWidgets.QPushButton("Quit")
        self.QContinueButton = QtWidgets.QPushButton("Continue")
        self.QuitButton.clicked.connect(FirstWindow.close)
        self.QContinueButton.clicked.connect(self.login)

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.spinBoxNUM,      1, 2)
        layout.addWidget(self.spinBoxLEVELS,  11, 2)
        layout.addWidget(self.QuitButton,     15, 1)
        layout.addWidget(self.QContinueButton,15, 2)

        self.setLayout(layout)

    def login(self):
        self.MAP    = [[1 for x in range(4)]for y in range(7)]     # ??? (self.LEVELS)]
        self.switch_window.emit()

    def sizeHint(self):                                            # <--- sizeHint
        return QtCore.QSize(700, 500)



#class Controller:
class Controller(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.show_login()

    def show_login(self):
        self.login = Login()

        self.scrollArea = QtWidgets.QScrollArea()                   # +++
        self.scrollArea.setWidget(self.login)                       # +++

        self.login.switch_window.connect(self.show_main)

        self.scrollArea.show()                                      # +++
        self.scrollArea.resize(700, 500)                            # +++
#        self.login.show()

    def show_main(self):
        self.MAP                   = self.login.MAP
        #Parameters from file
        self.NUM                    = self.login.spinBoxNUM.value()

#        self.login.close()
        self.scrollArea.hide()                                       # +++
        self.show()                                                  # +++


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.setWindowTitle("Controller")
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

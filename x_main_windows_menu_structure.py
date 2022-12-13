from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(889, 428)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 889, 18))
        self.menubar.setObjectName("menubar")
        self.menupr1 = QtWidgets.QMenu(self.menubar)
        self.menupr1.setObjectName("menupr1")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionpr2 = QtWidgets.QAction(MainWindow)
        self.actionpr2.setObjectName("actionpr2")
        self.actionp3 = QtWidgets.QAction(MainWindow)
        self.actionp3.setObjectName("actionp3")
        self.actionfr2 = QtWidgets.QAction(MainWindow)
        self.actionfr2.setObjectName("actionfr2")
        self.menupr1.addAction(self.actionpr2)
        self.menupr1.addAction(self.actionp3)
        self.menubar.addAction(self.menupr1.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menupr1.setTitle(_translate("MainWindow", "pr1"))
        self.actionpr2.setText(_translate("MainWindow", "pr2"))
        self.actionp3.setText(_translate("MainWindow", "p3"))
        self.actionfr2.setText(_translate("MainWindow", "fr2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

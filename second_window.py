import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, qApp, QPushButton
from PyQt5.QtCore import Qt, QPoint


class WindowSettings(QWidget):
    def __init__(self):
        super().__init__()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = WindowSettings()
        self.setCentralWidget(self.ui)
        self.setGeometry(300, 300, 700, 400)
        self.menu = self.menuBar()
        self.file = self.menu.addMenu('&&File')
        self.settings = self.menu.addMenu('&settings')
        self.exit = QAction('exit', self)
        self.button = QPushButton("Старт")
        self.button.move(10, 10)
        self.settings_win = QAction('settings', self)
        self.file.addAction(self.exit)
        self.settings.addAction(self.settings_win)
        self.exit.triggered.connect(qApp.quit)
        self.settings_win.triggered.connect(self.settings_show)

    def settings_show(self):
        w = QWidget(self, Qt.Window)
        w.setWindowModality(Qt.WindowModal)
        w.resize(100, 100)
        w.move(self.geometry().center() - w.rect().center() - QPoint(0, 30))
        w.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())

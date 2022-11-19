import sys
import PyQt5.QtWidgets
import PyQt5.QtCore

# класс главного окна
class WindowMain(PyQt5.QtWidgets.QMainWindow):
    """Класс главного окна"""

    # описание главного окна
    def __init__(self):
        super().__init__()
        # переменные
        pass

        # главное окно, надпись на нём и размеры
        self.setWindowTitle('Название главного окна')
        self.setGeometry(450, 100, 700, 490)

        # ГЛАВНОЕ МЕНЮ
        self.menu = self.menuBar()
        # ФАЙЛ
        self.file = self.menu.addMenu('Файл')
        self.file_open = self.file.addAction('Открыть')
        self.file_save = self.file.addAction('Сохранить')
        self.exit = PyQt5.QtWidgets.QAction('Выход', self)

        # НАСТРОЙКИ
        self.settings = self.menu.addMenu('Настройки')
        self.settings_win = PyQt5.QtWidgets.QAction('Настройка соревнования', self)
        # ПОМОЩЬ
        self.help = self.menu.addMenu('Помощь')
        self.help.addMenu('Правила соревнований')
        # О ПРОГРАММЕ
        self.about = self.menu.addMenu('О программе')

        self.file.addAction(self.exit)
        self.settings.addAction(self.settings_win)
        self.exit.triggered.connect(PyQt5.QtWidgets.qApp.quit)
        self.settings_win.triggered.connect(self.settings_show)

    def settings_show(self):
        w = PyQt5.QtWidgets.QWidget(self, PyQt5.QtCore.Qt.Window)
        w.setWindowModality(PyQt5.QtCore.Qt.WindowModal)
        w.resize(300, 200)
        w.move(self.geometry().center() - w.rect().center() - PyQt5.QtCore.QPoint(0, 30))
        w.show()
        # print(self.geometry().center())
        # print(w.rect().center())
        # print(PyQt5.QtCore.QPoint(30, 100))


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    myapp = WindowMain()
    myapp.show()
    sys.exit(app.exec_())

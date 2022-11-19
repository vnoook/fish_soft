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

    # окно настроек
    def settings_show(self):
        window_settings = PyQt5.QtWidgets.QWidget(self, PyQt5.QtCore.Qt.Window)
        window_settings.setWindowModality(PyQt5.QtCore.Qt.WindowModal)
        window_settings.resize(600, 600)
        window_settings.move(self.geometry().center() - window_settings.rect().center() - PyQt5.QtCore.QPoint(0, 30))

        # lineEdit_
        window_settings.lineEdit_ = PyQt5.QtWidgets.QLineEdit(window_settings)
        window_settings.lineEdit_.setObjectName('lineEdit_')
        window_settings.lineEdit_.setPlaceholderText('lineEdit_')
        window_settings.lineEdit_.setText('lineEdit_')
        window_settings.lineEdit_.setGeometry(PyQt5.QtCore.QRect(10, 160, 110, 20))
        window_settings.lineEdit_.setClearButtonEnabled(True)
        window_settings.lineEdit_.setEnabled(False)
        window_settings.lineEdit_.setToolTip(window_settings.lineEdit_.objectName())

        # print(f'{self.geometry().center() = }')
        # print(f'{window_settings.rect().center() = }')
        # print(f'{PyQt5.QtCore.QPoint(30, 100) = }')


        # # клуб CLUB_
        # "CLUB_ID": "1A2B-3C4D-5E6F",
        # # программа SOFT_
        # "SOFT_DB_FILE": "db_competition.db",
        # "SOFT_LAST_OPEN": "1980-06-30",  # fromisoformat('YYYY-MM-DD')
        # "SOFT_MAIN_WINDOW_SIZE": "1300:500",
        # # соревнование COMP_
        # "COMP_DATA_COMPETITION": "2022-02-24",  # fromisoformat('YYYY-MM-DD')
        # "COMP_q_tur": 1,
        # "COMP_q_period": 4,
        # "COMP_q_zone": 1,
        # "COMP_q_sector": 1,
        # "COMP_d_period": 45,
        # "COMP_q_anglers": 15,

        window_settings.show()


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    myapp = WindowMain()
    myapp.show()
    sys.exit(app.exec_())
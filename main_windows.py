import sys
import PyQt5.QtWidgets
import PyQt5.QtCore
import fish_consts as CONST

# класс главного окна
class WindowMain(PyQt5.QtWidgets.QMainWindow):
    """Класс главного окна"""

    # переменные класса
    pass

    # описание главного окна
    def __init__(self):
        """Метод инициализации класса главного окна"""
        super().__init__()

        # переменные
        pass

        # главное окно, надпись на нём и размеры
        self.setWindowTitle(CONST.SET_DEF['main_win_name'])
        self.setGeometry(CONST.SET_DEF['main_win_coord_x'],
                         CONST.SET_DEF['main_win_coord_y'],
                         CONST.SET_DEF['main_win_coord_height'],
                         CONST.SET_DEF['main_win_coord_width'])

        # ГЛАВНОЕ МЕНЮ
        self.menu = self.menuBar()

        # ФАЙЛ
        self.file = self.menu.addMenu('Файл')
        self.file_open = self.file.addAction('Открыть')
        self.file_save = self.file.addAction('Сохранить')
        self.file_exit = self.file.addAction('Выход')
        # self.exit = PyQt5.QtWidgets.QAction('Выход', self)
        # self.file.addAction(self.exit)
        # self.exit.triggered.connect(PyQt5.QtWidgets.qApp.quit)

        # НАСТРОЙКИ
        self.settings = self.menu.addMenu('Настройки')
        self.settings_soft = self.settings.addAction('Настройка программы')
        self.settings_comp = self.settings.addAction('Настройка соревнования')
        # self.settings_comp = PyQt5.QtWidgets.QAction('Настройка соревнования', self)
        self.settings_comp.triggered.connect(self.window_show_settings_comp)
        self.settings.addAction(self.settings_comp)

        # ПОМОЩЬ
        self.help = self.menu.addMenu('Помощь')
        self.help_rules_comp = self.help.addAction('Правила соревнований')

        # О ПРОГРАММЕ
        self.about = self.menu.addMenu('О программе')

    # окно настроек соревнований
    def window_show_settings_comp(self):
        """Функция окна настроек соревнований"""
        window_settings = PyQt5.QtWidgets.QWidget(self, PyQt5.QtCore.Qt.Window)
        window_settings.setWindowModality(PyQt5.QtCore.Qt.WindowModal)
        window_settings.resize(600, 600)
        window_settings.move(self.geometry().center() - window_settings.rect().center() - PyQt5.QtCore.QPoint(0, 30))

        # # lineEdit_
        # window_settings.lineEdit_ = PyQt5.QtWidgets.QLineEdit(window_settings)
        # window_settings.lineEdit_.setObjectName('lineEdit_')
        # window_settings.lineEdit_.setPlaceholderText('lineEdit_')
        # window_settings.lineEdit_.setText('lineEdit_')
        # window_settings.lineEdit_.setGeometry(PyQt5.QtCore.QRect(10, 160, 110, 20))
        # window_settings.lineEdit_.setClearButtonEnabled(True)
        # window_settings.lineEdit_.setEnabled(False)
        # window_settings.lineEdit_.setToolTip(window_settings.lineEdit_.objectName())

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

    # окно настроек программы
    def window_show_settings_soft(self):
        """Функция окна настроек программы"""
        pass

    # функция переназначения на закрытие окна
    def closeEvent(self, event):
        """Функция переназначения на закрытие окна"""
        print(f'    {self.closeEvent.__name__ = }')
        print(f'        {self = }')
        print(f'        {event = }')
        save_settings()


# функция чтения настроек, обычно для открытия программы
def read_settings():
    """Функция окна настроек"""
    print(read_settings.__name__)
    pass


# функция сохранения настроек, обычно для закрытия программы
def save_settings():
    """Функция окна настроек"""
    print(save_settings.__name__)
    pass


# основная функция запуска приложения
def run():
    print(run.__name__)
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    app_window_main = WindowMain()
    app_window_main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    read_settings()
    run()

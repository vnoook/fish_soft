import sys
import os.path
import PyQt5.QtGui
# import PyQt5.QtCore
import PyQt5.QtWidgets
if sys.version_info < (3, 11):
    import tomli as tomllib
    import tomli_w
else:
    import tomllib
    import tomli_w
import fish_consts as const
from pprint import pprint as pp

DEBUG = False
SETTINGS_FILE_DEF = 'fish_settings.toml'
SETTINGS_DATA_DEF = None


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
        main_window_n = const.SETT_DEF['settings_window_main']['window_name']['name']
        main_window_x = const.SETT_DEF['settings_window_main']['window_coords']['x']
        main_window_y = const.SETT_DEF['settings_window_main']['window_coords']['y']
        main_window_h = const.SETT_DEF['settings_window_main']['window_coords']['h']
        main_window_w = const.SETT_DEF['settings_window_main']['window_coords']['w']

        self.frame_geometry = None

        # главное окно, надпись на нём и размеры
        self.setWindowTitle(main_window_n)
        self.setGeometry(main_window_x, main_window_y, main_window_h, main_window_w)

        # ГЛАВНОЕ МЕНЮ
        self.menu = self.menuBar()

        # ФАЙЛ
        self.file = self.menu.addMenu('Файл')
        self.file_open = self.file.addAction('Открыть')
        self.file_save = self.file.addAction('Сохранить')
        self.file_exit = self.file.addAction('Выход')
        self.file_open.triggered.connect(self.window_file_open)
        self.file_save.triggered.connect(self.window_file_save)
        self.file_exit.triggered.connect(self.window_file_exit)

        # НАСТРОЙКИ
        self.settings = self.menu.addMenu('Настройки')
        self.settings_soft = self.settings.addAction('Настройка программы')
        self.settings_competition = self.settings.addAction('Настройка соревнования')
        self.settings_soft.triggered.connect(self.window_settings_soft)
        self.settings_competition.triggered.connect(self.window_settings_competition)
        self.settings.addAction(self.settings_competition)

        # ПОМОЩЬ
        self.help = self.menu.addMenu('Помощь')
        self.help_rules_competition = self.help.addAction('Правила соревнований')
        self.help_rules_competition.triggered.connect(self.window_rules_competition)

        # О ПРОГРАММЕ
        self.about = self.menu.addAction('О программе')
        self.about.triggered.connect(self.window_about)

    # функция по открытию меню Файл-Открыть
    def window_file_open(self):
        """Функция меню Файл-Открыть"""
        print(self.window_file_open.__name__) if DEBUG else ...
        pass

    # функция по открытию меню Файл-Сохранить
    def window_file_save(self):
        """Функция меню Файл-Сохранить"""
        print(self.window_file_save.__name__) if DEBUG else ...
        pass

    # функция по открытию меню Файл-Выход
    def window_file_exit(self):
        """Функция меню Файл-Выход"""
        print(self.window_file_exit.__name__) if DEBUG else ...
        self.exit_common()

    # окно настроек соревнований
    def window_settings_competition(self):
        """Функция окна настроек соревнований"""
        print(self.window_settings_competition.__name__) if DEBUG else ...
        pass

        # window_settings = PyQt5.QtWidgets.QWidget(self, PyQt5.QtCore.Qt.Window)
        # window_settings.setWindowModality(PyQt5.QtCore.Qt.WindowModal)
        # window_settings.resize(600, 600)
        # window_settings.move(self.geometry().center() - window_settings.rect().center() - PyQt5.QtCore.QPoint(0, 30))

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

        # window_settings.show()

    # окно настроек программы
    def window_settings_soft(self):
        """Функция окна настроек программы"""
        print(self.window_settings_soft.__name__) if DEBUG else ...
        pass

    # окно правил соревнований
    def window_rules_competition(self):
        """Функция окна правил соревнований"""
        print(self.window_rules_competition.__name__) if DEBUG else ...
        pass

    # окно О программе
    def window_about(self):
        """Функция окна О программе"""
        print(self.window_about.__name__) if DEBUG else ...
        pass

    # функция переназначения закрытия окна по X или Alt+F4
    def closeEvent(self, event):
        """Функция переназначения на закрытие окна"""
        print(self.closeEvent.__name__) if DEBUG else ...
        self.exit_common()

    # функция переназначения движение окна
    def moveEvent(self, event):
        """Функция переназначения движение окна"""
        print(self.moveEvent.__name__) if DEBUG else ...
        self.get_coords()

    # функция переназначения изменения размеров окна
    def resizeEvent(self, event):
        """Функция переназначения изменения размеров окна"""
        print(self.resizeEvent.__name__) if DEBUG else ...
        self.get_coords()

    # функция получения координат и запись их в переменную экземпляр класса
    def get_coords(self):
        """Функция получения координат и запись их в переменную экземпляра класса"""
        print(self.get_coords.__name__) if DEBUG else ...
        self.frame_geometry = self.geometry()

    # функция общего выхода из программы
    def exit_common(self):
        print('_'*25) if DEBUG else ...
        print(self.exit_common.__name__) if DEBUG else ...
        save_settings()
        exit_app()


# функция чтения настроек из файла toml ИЛИ установка дефолтных значений, обычно при открытии программы
def read_settings():
    """Функция чтения настроек из файла toml ИЛИ установка дефолтных значений"""
    print(read_settings.__name__) if DEBUG else ...

    global SETTINGS_FILE_DEF
    global SETTINGS_DATA_DEF

    if os.path.exists(SETTINGS_FILE_DEF):
        print(f'Файл {SETTINGS_FILE_DEF = } имеется читаю настройки из файла '
              f'и кладу в глобальную переменную SETTINGS_DATA_DEF')

        with open(SETTINGS_FILE_DEF, "rb") as fl_set:
            data = tomllib.load(fl_set)

        SETTINGS_DATA_DEF = data
    else:
        print(f'Файл {SETTINGS_FILE_DEF = } отсутствует, '
              f'значит SETTINGS_FILE_DEF надо заполнить данными из const.SETT_DEF')
        SETTINGS_DATA_DEF = const.SETT_DEF

    # pp(SETTINGS_DATA_DEF)


# функция валидности ключей и их количества в файле настроек
def repair_settings(cur_dict: dict, def_dict: dict):
    """Функция валидности ключей и их количества в файле настроек"""
    print(repair_settings.__name__) if DEBUG else ...

    # проверяю на нехватку нужных ключей в словаре и если нет, то добавляю из дефолтных
    for key in def_dict:
        if key not in cur_dict:
            cur_dict[key] = def_dict[key]

    # проверяю на наличие лишних ключей в словаре и если есть лишние, то удаляю их
    # временный список для лишних ключей
    list_keys = []

    # собираю в список лишние ключи
    for key in cur_dict:
        if key not in def_dict:
            list_keys.append(key)

    # по списку удаляю лишние ключи
    for key in list_keys:
        del cur_dict[key]

    # удаляю временный список
    del list_keys
    # возвращаю поправленный словарь настроек
    return cur_dict


# функция сохранения настроек в файл toml, обычно при закрытии программы
def save_settings():
    """Функция сохранения настроек в файл toml"""
    print(save_settings.__name__) if DEBUG else ...
    # print('*' * 50)

    global SETTINGS_DATA_DEF
    global SETTINGS_FILE_DEF

    # запись настроек в файл
    with open(SETTINGS_FILE_DEF, "wb") as file_set:
        tomli_w.dump(SETTINGS_DATA_DEF, file_set)


# функция непосредственного выхода из программы
def exit_app():
    """Функция окна настроек"""
    print(exit_app.__name__) if DEBUG else ...
    sys.exit()


# основная функция запуска приложения
def run():
    print(run.__name__) if DEBUG else ...

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    screen_geometry = app.desktop().screenGeometry()
    screen_size = [screen_geometry.width(), screen_geometry.height()]
    SETTINGS_DATA_DEF['settings_soft']['screen_resolution'] = screen_size

    app_window_main = WindowMain()
    app_window_main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    read_settings()
    run()

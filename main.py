import sys
import os.path
import PyQt5.QtGui
import PyQt5.QtCore
import PyQt5.QtWidgets

if sys.version_info < (3, 11):
    import tomli as tomllib
else:
    import tomllib
import tomli_w
import fish_consts as fcs

# from pprint import pprint as pp

# определение констант
# выводит информацию по входу в каждую функцию
DEBUG = False
# название файла с настройками
SETTINGS_FILE = 'fish_settings.toml'
# набор констант для открытого и закрытого хранения
SETTINGS_DATA_DEF = None
SETTINGS_COMMON_DEF = None


# класс главного окна
class WindowMain(PyQt5.QtWidgets.QMainWindow):
    """Класс главного окна"""

    # описание главного окна
    def __init__(self):
        """Метод инициализации класса главного окна"""

        super().__init__()

        # переменные
        soft_version = SETTINGS_COMMON_DEF['version']
        main_window_n = SETTINGS_COMMON_DEF['window_name_main']
        main_window_x = SETTINGS_DATA_DEF['settings_window_main']['window_coords_x']
        main_window_y = SETTINGS_DATA_DEF['settings_window_main']['window_coords_y']
        main_window_h = SETTINGS_DATA_DEF['settings_window_main']['window_coords_h']
        main_window_w = SETTINGS_DATA_DEF['settings_window_main']['window_coords_w']

        # переменная для доступа к координатам окна
        self.frame_geometry = None

        # главное окно, надпись на нём и размеры
        self.setWindowTitle(main_window_n + ' - ' + soft_version)
        self.setGeometry(main_window_x, main_window_y, main_window_w, main_window_h)

        # создание главного меню
        self.menu = None
        self.file = None
        self.file_open = None
        self.file_save = None
        self.file_exit = None
        self.settings = None
        self.settings_soft = None
        self.settings_competition = None
        self.help = None
        self.help_rules_competition = None
        self.about = None
        self.create_menu()

        # генерация объектов для ввода данных по соревнованиям
        self.gen_main_objects()

    # функция создания главного меню
    def create_menu(self):
        """Функция создания главного меню"""
        print(self.create_menu.__name__) if DEBUG else ...

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
        self.settings_soft = self.settings.addAction('Настройки программы')
        self.settings_competition = self.settings.addAction('Настройки соревнования')
        self.settings_soft.triggered.connect(self.window_settings_soft)
        self.settings_competition.triggered.connect(self.window_settings_competition)
        self.settings.addAction(self.settings_competition)

        # ПОМОЩЬ
        self.help = self.menu.addMenu('Помощь')
        self.help_rules_competition = self.help.addAction('Правила соревнований')
        self.help_rules_competition.triggered.connect(self.window_rules_competition)

        # О ПРОГРАММЕ
        self.about = self.menu.addAction('О программе')
        self.about.triggered.connect(self.window_about_soft)

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

        # переменные
        comp_window_n = SETTINGS_COMMON_DEF['window_name_set_comp']
        comp_window_x = SETTINGS_COMMON_DEF['settings_window_set_comp']['window_coords_x']
        comp_window_y = SETTINGS_COMMON_DEF['settings_window_set_comp']['window_coords_y']
        comp_window_w = SETTINGS_COMMON_DEF['settings_window_set_comp']['window_coords_w']
        comp_window_h = SETTINGS_COMMON_DEF['settings_window_set_comp']['window_coords_h']

        # окно настроек, надпись на нём и размеры
        window_settings = PyQt5.QtWidgets.QWidget(self, PyQt5.QtCore.Qt.Window)
        window_settings.setWindowTitle(comp_window_n)
        window_settings.setWindowModality(PyQt5.QtCore.Qt.WindowModal)
        window_settings.setGeometry(comp_window_x + 25, comp_window_y + 25, comp_window_w, comp_window_h)
        window_settings.show()

    # окно настроек программы
    def window_settings_soft(self):
        """Функция окна настроек программы"""
        print(self.window_settings_soft.__name__) if DEBUG else ...

        # переменные
        soft_window_n = SETTINGS_COMMON_DEF['window_name_set_soft']
        soft_window_x = SETTINGS_COMMON_DEF['settings_window_set_soft']['window_coords_x']
        soft_window_y = SETTINGS_COMMON_DEF['settings_window_set_soft']['window_coords_y']
        soft_window_w = SETTINGS_COMMON_DEF['settings_window_set_soft']['window_coords_w']
        soft_window_h = SETTINGS_COMMON_DEF['settings_window_set_soft']['window_coords_h']

        # окно настроек, надпись на нём и размеры
        window_settings = PyQt5.QtWidgets.QWidget(self, PyQt5.QtCore.Qt.Window)
        window_settings.setWindowTitle(soft_window_n)
        window_settings.setWindowModality(PyQt5.QtCore.Qt.WindowModal)
        window_settings.setGeometry(soft_window_x + 25, soft_window_y + 25, soft_window_w, soft_window_h)
        window_settings.show()

    # окно правил соревнований
    def window_rules_competition(self):
        """Функция окна правил соревнований"""
        print(self.window_rules_competition.__name__) if DEBUG else ...

        pass

    # окно О программе
    def window_about_soft(self):
        """Функция окна О программе"""
        print(self.window_about_soft.__name__) if DEBUG else ...

        # переменные
        soft_version = SETTINGS_COMMON_DEF['version']
        about_window_n = SETTINGS_COMMON_DEF['window_name_about']
        about_window_text = SETTINGS_COMMON_DEF['about_text']

        window_about = PyQt5.QtWidgets.QMessageBox(self)
        window_about.setWindowTitle(about_window_n)
        window_about.setText(about_window_text + ', версия ' + soft_version)
        window_about.show()

    # генерация объектов для ввода данных по соревнованиям
    def gen_main_objects(self):
        """Генерация объектов для ввода данных"""
        print(self.gen_main_objects.__name__) if DEBUG else ...

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

        # переопределение встроенной класса в локальную для доступа к координатам
        self.frame_geometry = self.geometry()

        SETTINGS_DATA_DEF['settings_window_main']['window_coords_x'] = self.frame_geometry.x()
        SETTINGS_DATA_DEF['settings_window_main']['window_coords_y'] = self.frame_geometry.y()
        SETTINGS_DATA_DEF['settings_window_main']['window_coords_h'] = self.frame_geometry.height()
        SETTINGS_DATA_DEF['settings_window_main']['window_coords_w'] = self.frame_geometry.width()
        SETTINGS_COMMON_DEF['settings_window_set_comp']['window_coords_x'] = self.frame_geometry.x()
        SETTINGS_COMMON_DEF['settings_window_set_comp']['window_coords_y'] = self.frame_geometry.y()
        SETTINGS_COMMON_DEF['settings_window_set_soft']['window_coords_x'] = self.frame_geometry.x()
        SETTINGS_COMMON_DEF['settings_window_set_soft']['window_coords_y'] = self.frame_geometry.y()
        SETTINGS_COMMON_DEF['settings_window_about']['window_coords_x'] = self.frame_geometry.x()
        SETTINGS_COMMON_DEF['settings_window_about']['window_coords_y'] = self.frame_geometry.y()

    # функция общего выхода из программы
    def exit_common(self):
        """Функция общего выхода из программы"""
        print('_' * 25) if DEBUG else ...
        print(self.exit_common.__name__) if DEBUG else ...

        save_settings()
        exit_app()


# функция чтения констант из файла toml ИЛИ установка дефолтных значений, обычно при открытии программы
def read_settings():
    """Функция чтения констант из файла toml ИЛИ установка дефолтных значений"""
    print(read_settings.__name__) if DEBUG else ...

    # добавление глобальных констант
    # которые не требуется сохранять в файл, но для работы они нужны
    global SETTINGS_COMMON_DEF
    SETTINGS_COMMON_DEF = fcs.SETT_DEF_COMMON

    # добавление глобальных констант
    # которые требуется сохранять в файл
    global SETTINGS_FILE
    global SETTINGS_DATA_DEF

    # если файла нет, то настройки берут по-умолчанию
    # если файл есть, то пробую прочитать
    #   если файл не TOML, то ставлю настройки по-умолчанию
    #   если файл TOML, то ставлю настройки из файла
    if not os.path.exists(SETTINGS_FILE):
        # если файла нет, то настройки берутся по-умолчанию
        SETTINGS_DATA_DEF = fcs.SETT_DEF_SOFT
    else:
        try:
            # пробую открыть, прочитать и распознать данные в файле
            with open(SETTINGS_FILE, "rb") as file_settings:
                data = tomllib.load(file_settings)
        except Exception as _err:
            print('какая-то ошибка', _err)

            # любая ошибка распознаётся как нечитаемый файл и значит настройки берутся по-умолчанию
            SETTINGS_DATA_DEF = fcs.SETT_DEF_SOFT
        else:
            SETTINGS_DATA_DEF = repair_settings(data, fcs.SETT_DEF_SOFT)


# функция валидности ключей и их количества в хранилище настроек
def repair_settings(cur_dict: dict, def_dict: dict):
    """Функция валидности ключей и их количества в хранилище настроек"""
    print(repair_settings.__name__) if DEBUG else ...

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

    # проверяю на нехватку нужных ключей в словаре и если нет, то добавляю из дефолтных
    for key, val in def_dict.items():
        if not cur_dict.get(key, False):
            cur_dict[key] = def_dict[key]
        else:
            if type(val) != type(cur_dict[key]):
                cur_dict[key] = val

        if isinstance(val, dict):
            repair_settings(cur_dict[key], val)

    # возвращаю поправленный словарь настроек
    return cur_dict


# функция сохранения настроек в файл toml, обычно при закрытии программы
def save_settings():
    """Функция сохранения настроек в файл toml"""
    print(save_settings.__name__) if DEBUG else ...

    global SETTINGS_DATA_DEF
    global SETTINGS_FILE

    data = repair_settings(SETTINGS_DATA_DEF, fcs.SETT_DEF_SOFT)

    # запись настроек в файл
    with open(SETTINGS_FILE, "wb") as file_settings:
        tomli_w.dump(data, file_settings)


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
    SETTINGS_DATA_DEF['settings_soft']['screen_resolution_x'] = screen_geometry.width()
    SETTINGS_DATA_DEF['settings_soft']['screen_resolution_y'] = screen_geometry.height()

    app_window_main = WindowMain()
    app_window_main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    read_settings()
    run()

# # lineEdit_
# window_settings.lineEdit_ = PyQt5.QtWidgets.QLineEdit(window_settings)
# window_settings.lineEdit_.setObjectName('lineEdit_')
# window_settings.lineEdit_.setPlaceholderText('lineEdit_')
# window_settings.lineEdit_.setText('lineEdit_')
# window_settings.lineEdit_.setGeometry(PyQt5.QtCore.QRect(10, 160, 110, 20))
# window_settings.lineEdit_.setClearButtonEnabled(True)
# window_settings.lineEdit_.setEnabled(False)
# window_settings.lineEdit_.setToolTip(window_settings.lineEdit_.objectName())

# # label_select_file
# self.label_select_file = PyQt5.QtWidgets.QLabel(self)
# self.label_select_file.setObjectName('label_select_file')
# self.label_select_file.setText('Выберите файл CSV')
# self.label_select_file.setGeometry(PyQt5.QtCore.QRect(10, 10, 150, 40))
# font = PyQt5.QtGui.QFont()
# font.setPointSize(12)
# self.label_select_file.setFont(font)
# self.label_select_file.adjustSize()
# self.label_select_file.setToolTip(self.label_select_file.objectName())

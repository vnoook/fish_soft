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
    def __init__(self) -> None:
        """Метод инициализации класса главного окна"""
        print(self.__init__.__name__) if DEBUG else ...

        super().__init__()

        # версия программы
        self.soft_version = SETTINGS_COMMON_DEF['version']
        # название главного окна
        self.main_window_n = SETTINGS_COMMON_DEF['window_name_main']

        # координаты и длины сторон главного окна
        self.main_window_x = SETTINGS_DATA_DEF['settings_window_main']['window_coords_x']
        self.main_window_y = SETTINGS_DATA_DEF['settings_window_main']['window_coords_y']
        self.main_window_w = SETTINGS_DATA_DEF['settings_window_main']['window_coords_w']
        self.main_window_h = SETTINGS_DATA_DEF['settings_window_main']['window_coords_h']

        # переменная для доступа к координатам окна
        self.frame_geometry = None

        # главное окно, надпись на нём и размеры
        self.setWindowTitle(self.main_window_n + ' - ' + self.soft_version)
        self.setGeometry(self.main_window_x, self.main_window_y, self.main_window_w, self.main_window_h)

        # переменные для создания главного меню
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
        self.render_main_window()

    # функция создания главного меню
    def create_menu(self) -> None:
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
        # self.settings.addAction(self.settings_competition)

        # ПОМОЩЬ
        self.help = self.menu.addMenu('Помощь')
        self.help_rules_competition = self.help.addAction('Правила соревнований')
        self.help_rules_competition.triggered.connect(self.window_rules_competition)

        # О ПРОГРАММЕ
        self.about = self.menu.addAction('О программе')
        self.about.triggered.connect(self.window_about_soft)

    # функция по открытию меню Файл-Открыть
    def window_file_open(self) -> None:
        """Функция меню Файл-Открыть"""
        print(self.window_file_open.__name__) if DEBUG else ...

    # функция по открытию меню Файл-Сохранить
    def window_file_save(self) -> None:
        """Функция меню Файл-Сохранить"""
        print(self.window_file_save.__name__) if DEBUG else ...

    # функция по открытию меню Файл-Выход
    def window_file_exit(self) -> None:
        """Функция меню Файл-Выход"""
        print(self.window_file_exit.__name__) if DEBUG else ...

        self.exit_common()

    # окно настроек соревнований
    def window_settings_competition(self) -> None:
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
    def window_settings_soft(self) -> None:
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
    def window_rules_competition(self) -> None:
        """Функция окна правил соревнований"""
        print(self.window_rules_competition.__name__) if DEBUG else ...

    # окно О программе
    def window_about_soft(self) -> None:
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

    # генерация всех объектов на главной форме
    def render_main_window(self) -> None:
        """Генерация всех объектов на главной форме"""
        print(self.render_main_window.__name__) if DEBUG else ...

        # создание строки чекбоксов
        self.render_checkbox_main_window()
        # создание строки описаний
        self.render_desc_main_window()
        # создание строк спортиков
        self.render_objects_main_window()

    # генерация чекбоксов
    def render_checkbox_main_window(self) -> None:
        """Генерация чекбоксов"""
        print(self.render_checkbox_main_window.__name__) if DEBUG else ...
        # print('генерация чекбоксов')

        # checkbox_name = 'checkbox_' + str(Window.checkbox_counter)
        # checkBox = PyQt5.QtWidgets.QCheckBox(self)
        # checkBox.setObjectName(checkbox_name)
        # checkBox.setVisible(True)
        # checkBox.setText(checkbox_name)
        # checkBox.setToolTip(checkBox.objectName())
        # checkBox.clicked.connect(self.click_checkbox)
        # # self.checkBox.setGeometry(10, 50, 40, 40)
        # checkBox.resize(20, 20)
        # checkBox.adjustSize()
        # checkBox.move(10, 60+(30*(Window.checkbox_counter-1)))
        # checkBox.show()

    # генерация описаний
    def render_desc_main_window(self) -> None:
        """Генерация описаний"""
        print(self.render_desc_main_window.__name__) if DEBUG else ...
        # print('генерация описаний')

        # q_tur = SETTINGS_DATA_DEF['competition_action']['COMP_q_tur']
        # q_period = SETTINGS_DATA_DEF['competition_action']['COMP_q_period']
        # q_zone = SETTINGS_DATA_DEF['competition_action']['COMP_q_zone']
        # q_fio = SETTINGS_COMMON_DEF['competition_stat']['COMP_q_fio']
        # q_checkbox_in_line = SETTINGS_COMMON_DEF['competition_stat']['COMP_q_checkbox_in_line']
        # q_desc_in_line = SETTINGS_COMMON_DEF['competition_stat']['COMP_q_desc_in_line']

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

    # генерация объектов для ввода данных по соревнованиям
    def render_objects_main_window(self) -> None:
        """Генерация объектов для ввода данных"""
        print(self.render_objects_main_window.__name__) if DEBUG else ...
        # print('генерация объектов для ввода данных по соревнованиям')

        # сбор переменных для формирования объектов на форме
        start_x = SETTINGS_COMMON_DEF['form_sizes']['start_x']
        start_y = SETTINGS_COMMON_DEF['form_sizes']['start_y']
        gap_x = SETTINGS_COMMON_DEF['form_gaps']['gap_x']
        gap_y = SETTINGS_COMMON_DEF['form_gaps']['gap_y']
        obj_h = SETTINGS_COMMON_DEF['form_sizes']['obj_h']
        q_anglers = SETTINGS_DATA_DEF['competition_action']['COMP_q_anglers']

        list_of_units = get_list_fields_and_coords(start_x=start_x, start_y=start_y,
                                                   shift_x=gap_x, shift_y=gap_y,
                                                   field_h=obj_h,
                                                   q_sportsmen=q_anglers)
        # print(*list_of_units, sep='\n')

        # изменения размера окна
        self.resize_main_windows_for_render(list_of_units)

        # вставка на форму объектов
        q_steps = 6       # количество шагов считывания для списка
        for unit_sting in list_of_units:
            for i in range(0, len(unit_sting), q_steps):
                unit = unit_sting[i:(i+q_steps)]
                # print(i, type(unit), unit)

                # переменные из разделения списка на составляющие
                unit_name = unit[0]
                unit_x = unit[1]
                unit_y = unit[2]
                unit_w = unit[3]
                unit_h = unit[4]
                unit_type = unit[5]

                if unit_type == 'edit_on':
                    # lineEdit
                    line_edit_name = unit_name
                    line_edit = PyQt5.QtWidgets.QLineEdit(self)
                    line_edit.setObjectName(line_edit_name)
                    line_edit.setPlaceholderText(unit_name)
                    line_edit.setText(unit_name)
                    line_edit.setGeometry(unit_x, unit_y, unit_w, unit_h)
                    line_edit.setClearButtonEnabled(False)
                    line_edit.setEnabled(True)
                    line_edit.setToolTip(line_edit.objectName())
                    line_edit.show()

                elif unit_type == 'edit_off':
                    # lineEdit
                    line_edit_name = unit_name
                    line_edit = PyQt5.QtWidgets.QLineEdit(self)
                    line_edit.setObjectName(line_edit_name)
                    line_edit.setPlaceholderText(unit_name)
                    line_edit.setText(unit_name)
                    line_edit.setGeometry(unit_x, unit_y, unit_w, unit_h)
                    line_edit.setClearButtonEnabled(False)
                    line_edit.setEnabled(False)
                    line_edit.setToolTip(line_edit.objectName())
                    line_edit.show()

                elif unit_type == 'combobox_on':
                    # combobox_on
                    combo_box_name = unit_name
                    combo_box = PyQt5.QtWidgets.QComboBox(self)
                    combo_box.setObjectName(combo_box_name)
                    combo_box.setPlaceholderText(unit_name)
                    combo_box.setToolTip(combo_box.objectName())
                    combo_box.addItem(combo_box_name)
                    combo_box.setGeometry(unit_x, unit_y, unit_w, unit_h)
                    combo_box.setEnabled(True)
                    combo_box.show()

    # изменения размера окна
    def resize_main_windows_for_render(self, list_objects: list) -> None:
        """Изменения размера окна"""
        print(self.render_objects_main_window.__name__) if DEBUG else ...

        rez_x = SETTINGS_DATA_DEF['settings_soft']['screen_resolution_x']
        rez_y = SETTINGS_DATA_DEF['settings_soft']['screen_resolution_y']
        win_x = SETTINGS_DATA_DEF['settings_window_main']['window_coords_x']
        win_y = SETTINGS_DATA_DEF['settings_window_main']['window_coords_y']
        gap_x = SETTINGS_COMMON_DEF['form_gaps']['gap_x']
        gap_y = SETTINGS_COMMON_DEF['form_gaps']['gap_y']
        min_width = SETTINGS_COMMON_DEF['form_sizes']['min_width']
        min_height = SETTINGS_COMMON_DEF['form_sizes']['min_height']

        # изменение размера окна после рендеринга всех объектов устанавливается фиксированный размер,
        # чтобы все объекты входили в окно
        # находится последний правый объект, берутся координаты и суммируются с длиной объекта и отступом справа и вниз,
        # но не менее чем минимальный размер по стороне
        new_width = list_objects[-1][-5] + list_objects[-1][-3] + gap_x
        if new_width < min_width:
            new_width = min_width
        if new_width > rez_x:
            new_width = rez_x - win_x

        new_height = list_objects[-1][-4] + list_objects[-1][-2] + gap_y
        if new_height < min_height:
            new_height = min_height
        if new_height > rez_y:
            new_height = rez_y - win_y

        # print(f'{win_x = } ... {win_y = }')
        # print(f'{rez_x = } ... {rez_y = }')
        # print(f'{new_width = } ... {new_height = }')

        self.setFixedSize(new_width, new_height)
        # self.resize(new_width, new_height)
        self.show()

    # функция переназначения закрытия окна по X или Alt+F4
    def closeEvent(self, event) -> None:
        """Функция переназначения на закрытие окна"""
        print(self.closeEvent.__name__) if DEBUG else ...

        self.exit_common()

    # функция переназначения движение окна
    def moveEvent(self, event) -> None:
        """Функция переназначения движение окна"""
        print(self.moveEvent.__name__) if DEBUG else ...

        self.get_coords()

    # функция переназначения изменения размеров окна
    def resizeEvent(self, event) -> None:
        """Функция переназначения изменения размеров окна"""
        print(self.resizeEvent.__name__) if DEBUG else ...

        self.get_coords()

    # функция получения координат и запись их в переменную экземпляр класса
    def get_coords(self) -> None:
        """Функция получения координат и запись их в переменную экземпляра класса"""
        print(self.get_coords.__name__) if DEBUG else ...

        # переопределение встроенной переменной в локальную для доступа к координатам
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
    def exit_common(self) -> None:
        """Функция общего выхода из программы"""
        print('_' * 25) if DEBUG else ...
        print(self.exit_common.__name__) if DEBUG else ...

        # сохранение настроек перед выходом
        save_settings()
        # выход из приложения
        exit_app()


# функция чтения констант из файла toml ИЛИ установка дефолтных значений, обычно при открытии программы
def read_settings() -> None:
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
def repair_settings(cur_dict: dict, def_dict: dict) -> dict:
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
def save_settings() -> None:
    """Функция сохранения настроек в файл toml"""
    print(save_settings.__name__) if DEBUG else ...

    global SETTINGS_DATA_DEF
    global SETTINGS_FILE

    data = repair_settings(SETTINGS_DATA_DEF, fcs.SETT_DEF_SOFT)

    # запись настроек в файл
    with open(SETTINGS_FILE, "wb") as file_settings:
        tomli_w.dump(data, file_settings)


def get_list_fields_and_coords(start_x: int, start_y: int, shift_x: int,
                               shift_y: int, field_h: int, q_sportsmen: int) -> list:
    """Универсальная функция для описания полей и расчёта их координат на форме"""
    print(get_list_fields_and_coords.__name__) if DEBUG else ...

    # список всех полей и их координаты
    list_coord_of_fields = []

    # распределение входных переменных
    # точка начала отчёта
    start_dot_x = start_x
    start_dot_y = start_y
    # расстояние между объектами на форме
    gap_x = shift_x
    gap_y = shift_y
    # высота для всех полей
    field_height = field_h
    # количество спортиков
    q_sportiks = q_sportsmen
    # шаг по вертикали
    field_step_y = start_dot_y

    # кортеж из полей на форме "Название поля", длина, вид объекта на форме
    fields = (
              ('Sportik_number_', 40, 'edit_off'),
              ('Sportik_lottery_', 40, 'edit_off'),
              ('Sportik_fio_', 180, 'edit_on'),
              ('Sportik_team_', 180, 'edit_on'),
              ('Sportik_rank_', 40, 'edit_on'),
              ('Sportik_zona1_', 70, 'combobox_on'),
              ('Sportik_zona2_', 70, 'combobox_on'),
              ('Sportik_period1_', 40, 'edit_on'),
              ('Sportik_period2_', 40, 'edit_on'),
              ('Sportik_period3_', 40, 'edit_on'),
              ('Sportik_period4_', 40, 'edit_on'),
              ('Sportik_points_', 40, 'edit_off'),
              ('Sportik_team_place_', 40, 'edit_off'),
              ('Sportik_self_place_', 40, 'edit_off')
              )

    # цикл расчёта координат каждого поля
    for n_sportik in range(1, q_sportiks + 1):
        # шаг вправо начинается с первой точки и идёт вправо
        field_step_x = start_dot_x
        # список координат в строке
        list_coord_of_field = []

        # проход по строке полей
        for field in fields:
            # формирование имени спортика
            field_name = field[0] + str(n_sportik)
            # выбор ширины поля
            field_width = field[1]
            # вид объекта для вывода
            field_obj = field[2]

            # добавление в список параметров объекта
            list_coord_of_field.append(field_name)
            list_coord_of_field.append(field_step_x)
            list_coord_of_field.append(field_step_y)
            list_coord_of_field.append(field_width)
            list_coord_of_field.append(field_height)
            list_coord_of_field.append(field_obj)

            # увеличение шага вправо на ширину поля
            field_step_x = field_step_x + field_width

            # увеличение шага вправо на ширину промежутка между полями
            field_step_x = field_step_x + gap_x

        # добавление шага вниз на промежуток между строками полей
        field_step_y = field_step_y + field_height + gap_y

        # добавление в главный список списка строки полей
        list_coord_of_fields.append(list_coord_of_field)

    return list_coord_of_fields


# функция непосредственного выхода из программы
def exit_app() -> None:
    """Функция окна настроек"""
    print(exit_app.__name__) if DEBUG else ...

    sys.exit()


# основная функция запуска приложения
def run() -> None:
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

# # функция подготовки числа к двух разрядному символьному виду '1 -> 01'
# def get_bin_num(var: int) -> str:
#     """Функция подготовки числа к двух разрядному символьному виду 1 -> 01'"""
#     print(get_bin_num.__name__) if DEBUG else ...
#
#     if 0 < var < 10:
#         return ''.join(('0', str(var)))
#     elif var > 99:
#         return None
#     else:
#         return str(var)

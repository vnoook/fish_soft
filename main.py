# TODO
# сделать проверку вводимых данных в периоды, чтобы было без "000"

import sys
import os.path
import random
import PyQt5.QtGui
import PyQt5.QtCore
import PyQt5.QtWidgets

if sys.version_info < (3, 11):
    import tomli as tomllib
else:
    import tomllib

import tomli_w
import fish_consts as fcs

from pprint import pprint as pp


# определение констант
# выводит информацию по входу в каждую функцию
DEBUG = False
# название файла с настройками
SETTINGS_FILE = 'fish_settings.toml'
# файл для хранения последнего состояния значений на форме
LAST_STATE_FILE = 'last_state.toml'
# набор констант для открытого и закрытого хранения
SETTINGS_DATA_DEF = None
SETTINGS_COMMON_DEF = None
SETT_MODEL = None
LAST_STATE = None


# класс главного окна
class WindowMain(PyQt5.QtWidgets.QMainWindow):
    """Класс главного окна"""

    # описание главного окна
    def __init__(self) -> None:
        """Метод инициализации класса главного окна"""
        print(self.__init__.__name__) if DEBUG else ...

        super().__init__()

        # словарь всех объектов рендеринга, нужен для хранения, поиска и чистки на форме
        # можно было использовать findChildren, но этот вариант мне кажется уместнее
        self.dict_all_units = {}

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
        self.file_sep = None
        self.file_send = None
        self.file_exit = None
        self.settings = None
        self.settings_soft = None
        self.settings_competition = None
        self.help = None
        self.help_rules_competition = None
        self.about = None

        # создание главного меню
        self.create_menu()

        # генерация объектов для ввода данных по соревнованиям
        self.render_objects_main_window()

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
        self.file_sep = self.file.addSeparator()
        self.file_send = self.file.addAction('Отправить')
        self.file_sep = self.file.addSeparator()

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.cleaner = self.file.addAction('cleaner')
        self.adder = self.file.addAction('adder')
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.file_sep = self.file.addSeparator()
        self.file_exit = self.file.addAction('Выход')
        self.file_open.triggered.connect(self.window_file_open)
        self.file_save.triggered.connect(self.window_file_save)
        self.file_send.triggered.connect(self.window_file_send)
        self.file_exit.triggered.connect(self.window_file_exit)

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.cleaner.triggered.connect(self.del_form_units)
        self.adder.triggered.connect(self.add_form_units)
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # НАСТРОЙКИ
        self.settings = self.menu.addMenu('Настройки')
        self.settings_soft = self.settings.addAction('Настройки программы')
        self.settings_competition = self.settings.addAction('Настройки соревнования')
        self.settings_soft.triggered.connect(self.window_settings_soft)
        self.settings_competition.triggered.connect(self.window_settings_competition)

        # ПОМОЩЬ
        self.help = self.menu.addMenu('Помощь')
        self.help_rules_competition = self.help.addAction('Правила соревнований')
        self.help_rules_competition.triggered.connect(self.window_rules_competition)

        # О ПРОГРАММЕ
        self.about = self.menu.addAction('О программе')
        self.about.triggered.connect(self.window_about_soft)

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # функция очистки главного окна от объектов
    def del_form_units(self) -> None:
        """Функция очистки главного окна от объектов"""
        print(self.del_form_units.__name__) if DEBUG else ...

        # если словарь с объектами не пуст, то удалить все объекты в нём и очистить его
        if self.dict_all_units:
            for unit in self.dict_all_units:
                self.dict_all_units[unit].deleteLater()
            self.dict_all_units = {}

    # функция добавления объектов на главное окно
    def add_form_units(self) -> None:
        """Функция добавления объектов на главное окно"""
        print(self.add_form_units.__name__) if DEBUG else ...

        # если словарь с объектами пуст, то добавить все объекты на форму
        if not self.dict_all_units:
            # генерация объектов для ввода данных по соревнованиям
            self.render_objects_main_window()
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    # функция по открытию меню Файл-Открыть
    def window_file_open(self) -> None:
        """Функция меню Файл-Открыть"""
        print(self.window_file_open.__name__) if DEBUG else ...

    # функция по открытию меню Файл-Сохранить
    def window_file_save(self) -> None:
        """Функция меню Файл-Сохранить"""
        print(self.window_file_save.__name__) if DEBUG else ...

    # функция по открытию меню Файл-Отправить
    def window_file_send(self) -> None:
        """Функция меню Файл-Отправить"""
        print(self.window_file_send.__name__) if DEBUG else ...

    # функция по открытию меню Файл-Выход
    def window_file_exit(self) -> None:
        """Функция меню Файл-Выход"""
        print(self.window_file_exit.__name__) if DEBUG else ...

        # процесс выхода из программы
        self.exit_common()

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
        comp_section = SETTINGS_DATA_DEF['competition_action']

        # окно настроек, надпись на нём и размеры
        self.window_settings = PyQt5.QtWidgets.QWidget(self, PyQt5.QtCore.Qt.Window)
        self.window_settings.setWindowTitle(comp_window_n)
        self.window_settings.setWindowModality(PyQt5.QtCore.Qt.WindowModal)
        self.window_settings.setGeometry(comp_window_x + 25, comp_window_y + 25, comp_window_w, comp_window_h)

        # алгоритм автоматического вывода настроек в окно
        # все объекты далее в этом окне будут иметь начало имён ws_
        # переменная индекс
        ws_ind = 0

        # группа для выводимых настроек
        ws_group = PyQt5.QtWidgets.QGroupBox('Введите новые параметры соревнований')

        # слой для автоматического распределения в окне
        ws_layout = PyQt5.QtWidgets.QGridLayout(self.window_settings)

        # цикл в котором создаются объекты настроек
        for key, val in comp_section.items():
            # QLabel
            ws_label = PyQt5.QtWidgets.QLabel(self.window_settings)
            ws_label.setObjectName('ws_label_'+key)
            ws_label.setText(key)
            ws_label.adjustSize()

            # QLineEdit
            ws_edit = PyQt5.QtWidgets.QLineEdit(self.window_settings)
            ws_edit.setObjectName('ws_edit_'+key)
            ws_edit.setText(str(val))
            ws_edit.adjustSize()
            ws_edit.setValidator(PyQt5.QtGui.QIntValidator(ws_edit))

            # добавление объектов в слой
            ws_layout.addWidget(ws_label, 0+ws_ind, 0)
            ws_layout.addWidget(ws_edit, 0+ws_ind, 1)

            # увеличение счетчика
            ws_ind += 1

        # кнопка YES
        ws_btn_yes = PyQt5.QtWidgets.QPushButton(self.window_settings)
        ws_btn_yes.setObjectName('ws_btn_yes')
        ws_btn_yes.setText('Сохранить')
        ws_btn_yes.adjustSize()
        # ws_btn_yes.setGeometry(PyQt5.QtCore.QRect(10, 70, 20, 20))
        ws_btn_yes.setFixedWidth(150)
        ws_btn_yes.clicked.connect(self.window_settings_btn)

        # кнопка NO
        ws_btn_no = PyQt5.QtWidgets.QPushButton(self.window_settings)
        ws_btn_no.setObjectName('ws_btn_no')
        ws_btn_no.setText('Отмена')
        ws_btn_no.adjustSize()
        # ws_btn_no.setGeometry(PyQt5.QtCore.QRect(10, 70, 50, 20))
        ws_btn_no.setFixedWidth(150)
        ws_btn_no.clicked.connect(self.window_settings_btn)

        # добавление кнопок в слой
        ws_layout.addWidget(ws_btn_yes, 0+ws_ind, 0)
        ws_layout.addWidget(ws_btn_no, 0+ws_ind, 1)

        # добавление слоя в группу
        ws_group.setLayout(ws_layout)
        layout = PyQt5.QtWidgets.QGridLayout(self.window_settings)
        layout.addWidget(ws_group, 0, 0)
        self.window_settings.setLayout(layout)

        # показать окно настроек
        self.window_settings.show()

    # функция действия по кнопке подтверждения в настройках соревнования
    def window_settings_btn(self) -> None:
        """Функция действия по кнопке подтверждения в настройках соревнования"""
        print(self.window_settings_btn.__name__) if DEBUG else ...

        # имя кнопки, пославшей событие
        btn_name = self.sender().objectName()

        # если кнопка ОК, то нужно:
        # получить новые числа, сохранить в константы и файл новые параметры,
        # закрыть окно настроек, перерисовать главное окно, поставить фокус на что-то
        if btn_name == 'ws_btn_yes':
            # собираются секции настроек соревнования
            comp_section = SETTINGS_DATA_DEF['competition_action']
            # ищутся все объекты для редактирования
            list_of_edits = self.window_settings.findChildren(PyQt5.QtWidgets.QLineEdit)

            # в цикле по секциям находятся имена объектов с совпадающими именами
            # и из этих объектов значения устанавливаются в константы
            for section in comp_section:
                for unit in list_of_edits:
                    if section in unit.objectName():
                        # TODO
                        # добавить проверка чисел, чтобы пользователь не ввёл слишком большие числа
                        SETTINGS_DATA_DEF['competition_action'][section] = int(unit.text())

            # если были изменения настроек, то сделать следующие действия
            # чистится главное окно
            self.del_form_units()
            # добавляются объекты на главное окно
            self.add_form_units()
            # сохраняются настройки в файл
            save_settings()

        # закрытие окна в любом случае
        self.window_settings.close()

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

    # генерация объектов для ввода данных по соревнованиям
    def render_objects_main_window(self) -> None:
        """Генерация объектов для ввода данных"""
        print(self.render_objects_main_window.__name__) if DEBUG else ...

        # сбор переменных для формирования объектов на форме
        start_x = SETTINGS_COMMON_DEF['form_sizes']['start_x']
        start_y = SETTINGS_COMMON_DEF['form_sizes']['start_y']
        gap_x = SETTINGS_COMMON_DEF['form_gaps']['gap_x']
        gap_y = SETTINGS_COMMON_DEF['form_gaps']['gap_y']
        obj_h = SETTINGS_COMMON_DEF['form_sizes']['obj_h']
        q_anglers = SETTINGS_DATA_DEF['competition_action']['COMP_q_anglers']
        q_zone = SETTINGS_DATA_DEF['competition_action']['COMP_q_zone']
        zones = SETTINGS_COMMON_DEF['name_of_zone']

        # хитрое вычисление текста строки label
        # делается сначала словарь, потом из unit_name берётся второе слово и ищется в словаре
        desc_dict = {}
        for val in SETT_MODEL:
            desc_dict[val[0]] = val[3]

        # получение списка объектов для вывода их в главном окне
        list_of_units = get_list_fields_and_coords(start_x=start_x, start_y=start_y,
                                                   shift_x=gap_x, shift_y=gap_y,
                                                   field_h=obj_h,
                                                   q_sportsmen=q_anglers)

        # изменения размера окна под объекты из списка объектов
        self.resize_main_windows_for_render(list_of_units)

        # вставка на форму объектов
        q_steps = 6  # количество шагов считывания из списка
        for unit_sting in list_of_units:
            # временный счётчик для добавления к описанию - порядковый номер описания
            counter_zona = 0
            counter_period = 0
            for i in range(0, len(unit_sting), q_steps):
                unit = unit_sting[i:(i + q_steps)]

                # переменные из разделения списка на составляющие
                unit_name = unit[0]
                unit_x = unit[1]
                unit_y = unit[2]
                unit_w = unit[3]
                unit_h = unit[4]
                unit_type = unit[5]

                # выбор объекта для вывода на форму
                if unit_type == 'edit_on':
                    # общее описание полей
                    # QLineEdit
                    line_edit_name = unit_name
                    line_edit = PyQt5.QtWidgets.QLineEdit(self)
                    line_edit.setObjectName(line_edit_name)
                    line_edit.setGeometry(unit_x, unit_y, unit_w, unit_h)
                    line_edit.setToolTip(line_edit.objectName() + '\n' +
                                         str(unit_x) + '-' + str(unit_y) + '-' +
                                         str(unit_w) + '-' + str(unit_h))
                    self.dict_all_units[line_edit_name] = line_edit
                    # line_edit.setPlaceholderText(unit_name)
                    # line_edit.setText(unit_name)
                    # line_edit.setText(str(unit_x) + '-' + str(unit_y) + '-' + str(unit_w) + '-' + str(unit_h))
                    # line_edit.setClearButtonEnabled(False)
                    # line_edit.setEnabled(True)

                    # дополнительная обработка полей
                    unit_model = unit_name.split('_')[1]
                    if unit_model == 'rank':
                        line_edit.setMaxLength(4)
                        line_edit.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
                    elif unit_model == 'fio':

                        # TODO
                        # перенести в константы
                        # количество символом на ФИО
                        length_fio = 30

                        # длина ввода для ФИО
                        line_edit.setMaxLength(length_fio)
                        # регулярное выражение для ввода только букв
                        regexp_alph = PyQt5.QtCore.QRegExp("[a-zA-Zа-яА-Я .,]{" + str(length_fio) + "}")
                        line_edit.setValidator(PyQt5.QtGui.QRegExpValidator(regexp_alph))
                    elif unit_model == 'team':
                        line_edit.setMaxLength(20)
                    elif unit_model == 'period':
                        line_edit.setMaxLength(5)
                        line_edit.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
                        line_edit.setValidator(PyQt5.QtGui.QIntValidator(line_edit))
                    elif unit_model in ('points', 'teams', 'self'):
                        line_edit.setAlignment(PyQt5.QtCore.Qt.AlignCenter)

                    # рендеринг объектов
                    line_edit.show()

                elif unit_type == 'edit_off':
                    # общее описание полей
                    # QLineEdit
                    line_edit_name = unit_name
                    line_edit = PyQt5.QtWidgets.QLineEdit(self)
                    line_edit.setObjectName(line_edit_name)
                    line_edit.setGeometry(unit_x, unit_y, unit_w, unit_h)
                    line_edit.setEnabled(False)
                    line_edit.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
                    line_edit.setToolTip(line_edit.objectName() + '\n' +
                                         str(unit_x) + '-' + str(unit_y) + '-' +
                                         str(unit_w) + '-' + str(unit_h))
                    self.dict_all_units[line_edit_name] = line_edit
                    # line_edit.setPlaceholderText(unit_name)
                    # line_edit.setText(unit_name)
                    # line_edit.setText(str(unit_x) + '-' + str(unit_y) + '-' + str(unit_w) + '-' + str(unit_h))
                    # line_edit.setClearButtonEnabled(False)

                    # дополнительная обработка полей
                    # TODO
                    # заполнение номеров спортсменов, можно заменить на заполнение через количество спортиков q_anglers
                    unit_model = unit_name.split('_')[1]
                    if unit_model == 'number':
                        line_edit.setText(unit_name.split('_')[2])

                    # рендеринг объектов
                    line_edit.show()

                elif unit_type == 'combobox_on':
                    # общее описание полей
                    # QComboBox
                    combo_box_name = unit_name
                    combo_box = PyQt5.QtWidgets.QComboBox(self)
                    combo_box.setObjectName(combo_box_name)
                    combo_box.setToolTip(combo_box.objectName() + '\n' + str(unit_x) + '-' +
                                         str(unit_y) + '-' + str(unit_w) + '-' + str(unit_h))
                    combo_box.addItem('')
                    combo_box.setGeometry(unit_x, unit_y, unit_w, unit_h)
                    self.dict_all_units[combo_box_name] = combo_box
                    # combo_box.setPlaceholderText(unit_name)
                    # combo_box.setEnabled(True)

                    # дополнительная обработка полей
                    for zone in range(q_zone):
                        combo_box.addItem(zones[zone])

                    # рендеринг объектов
                    combo_box.show()

                elif unit_type == 'checkbox':
                    # некоторые чекбоксы не нужны, поэтому не вывожу их на форму
                    if unit_name.split('_')[1] not in ('number', 'points', 'teams', 'self'):
                        # общее описание полей
                        # QCheckBox
                        check_box_name = unit_name
                        check_box = PyQt5.QtWidgets.QCheckBox(self)
                        check_box.setObjectName(check_box_name)
                        check_box.setText(' ' * unit_w)
                        check_box.setToolTip(check_box.objectName() + '\n' +
                                             str(unit_x) + '-' + str(unit_y) + '-' +
                                             str(unit_w) + '-' + str(unit_h))
                        check_box.setGeometry(unit_x, unit_y, unit_w, unit_h)
                        check_box.clicked.connect(self.change_status_checkbox)
                        self.dict_all_units[check_box_name] = check_box
                        # check_box.setVisible(True)

                        # дополнительная обработка полей
                        ...

                        # рендеринг объектов
                        check_box.show()

                elif unit_type == 'label':
                    # хитрое вычисление текста строки label
                    # делается сначала словарь, потом из unit_name берётся второе слово и ищется в словаре
                    if 'zona' in unit_name:
                        counter_zona += 1
                        counter = counter_zona
                    elif 'period' in unit_name:
                        counter_period += 1
                        counter = counter_period
                    else:
                        counter = ''

                    # общее описание полей
                    # QLabel
                    label_name = unit_name
                    label = PyQt5.QtWidgets.QLabel(self)
                    label.setObjectName(label_name)
                    label_text = desc_dict[unit_name.split('_')[1]] + str(counter)
                    label.setText(label_text)
                    label.adjustSize()
                    label.setToolTip(label.objectName() + '\n' +
                                     str(unit_x) + '-' + str(unit_y) + '-' +
                                     str(unit_w) + '-' + str(unit_h) + '\n' + label_text)
                    label.setGeometry(unit_x, unit_y, unit_w, unit_h)
                    self.dict_all_units[label_name] = label

                    # font = PyQt5.QtGui.QFont()
                    # font.setPointSize(8)
                    # label.setFont(font)
                    # label.setAlignment(PyQt5.QtCore.Qt.AlignCenter)

                    # дополнительная обработка полей
                    ...

                    # показывание объектов
                    label.show()

    # изменения размера окна
    def resize_main_windows_for_render(self, list_objects: list) -> None:
        """Изменения размера окна"""
        print(self.resize_main_windows_for_render.__name__) if DEBUG else ...

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
        #
        # находится последний правый объект, берутся координаты
        # и суммируются с длиной объекта и отступом справа и вниз,
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

        self.setFixedSize(new_width, new_height)
        # self.resize(new_width, new_height)
        self.show()

    # функция нажатия на чекбокс в описании
    def change_status_checkbox(self) -> None:
        """Функция нажатия на чекбокс в описании"""
        print(self.change_status_checkbox.__name__) if DEBUG else ...

        # узнать на какой колонке нажато, заблочено или нет, и заблочить или разблочить колонку
        # объект, который послал событие
        obj_cur = self.sender()
        # имя объекта пославшего событие
        obj_cur_name = obj_cur.objectName().split('_')[1]
        # колонка в которой объект находится
        obj_cur_col = obj_cur.objectName().split('_')[-1]
        # списки имен объектов для реакции
        checkbox_of_lottery = 'lottery'
        checkbox_of_names = ('fio', 'team', 'rank', 'zona')
        checkbox_of_period = 'period'

        # определение - какой чекбокс в какой колонке нажат:
        # если чекбокс "жеребьёвка"
        if obj_cur_name == checkbox_of_lottery:
            # количество спортсменов
            q_anglers = SETTINGS_DATA_DEF['competition_action']['COMP_q_anglers']
            lottery_list = [x for x in range(1, q_anglers + 1)]
            random.shuffle(lottery_list)

            # пробегает по всем объектам, ищет по совпадению в имени название колонки и реагирует
            for unit, unit_obj in self.dict_all_units.items():
                if 'sportik_lottery' in unit:
                    # номер строки спортсмена
                    unit_row = int(unit.split('_')[2])
                    # заполнение поля жеребьёвки соответствующим значением из списка жеребьёвок
                    unit_obj.setText(str(lottery_list[unit_row - 1]))

            # блокирую и скрываю чекбокс потому, что жеребьёвка проводится один раз за соревнования
            if obj_cur.isChecked():
                # нужно ли прятать чекбокс или нет? пока буду прятать
                obj_cur.setEnabled(False)
                obj_cur.setVisible(False)

        # если чекбоксы с полями о спортсмене
        elif obj_cur_name in checkbox_of_names:
            # получение флага заполненности колонки
            flag_fill_col = self.get_flag_fill_column(obj_cur_col)

            # если все поля в колонке заполнены, то можно блокировать объекты
            if flag_fill_col:
                # пробегает по всем объектам, ищет по совпадению в имени название колонки и реагирует
                for unit, unit_obj in self.dict_all_units.items():
                    # номер колонки
                    unit_col = unit.split('_')[-1]

                    # поиск конкретных объектов из конкретной колонки
                    if (obj_cur_col == unit_col) and \
                            ((unit_obj.__class__ is PyQt5.QtWidgets.QComboBox) or
                             (unit_obj.__class__ is PyQt5.QtWidgets.QLineEdit)):

                        # блокировка или разблокировка объекта на форме
                        if obj_cur.isChecked():
                            unit_obj.setEnabled(False)
                        else:
                            unit_obj.setEnabled(True)

                # действия после блокировки колонки - расчёт очков в периоде
                if (obj_cur_name == 'period') and (obj_cur.isChecked()):
                    # если нужные колонки тоже заблокированы, то можно делать расчёт
                    if self.check_for_calc():
                        self.calc_period(obj_cur)

            else:
                # если не всё заполнено, то возвращаю исходное состояние чекбокса
                obj_cur.setChecked(False)

                # если не всё заполнено, то перевожу фокус на первый "пустой" объект в колонке
                self.shift_focus_on_empty_unit(obj_cur_col)

                # информационное окно про полное заполнение колонки
                PyQt5.QtWidgets.QMessageBox.information(self, 'Блокировка не получилась',
                                                        f'Заполните все поля в колонке')

        # если чекбоксы "период"
        elif obj_cur_name == checkbox_of_period:
            # получение флага заполненности чекбоксов спортсмена
            flag_checkboxes = self.check_for_calc()
            # получение флага заполненности колонки
            flag_fill_col = self.get_flag_fill_column(obj_cur_col)

            # если чекбоксы о спортсменах и поля в колонке "период" заполнены, то можно блокировать объекты
            if not flag_checkboxes:
                # если не всё зафиксировано, то возвращаю исходное состояние чекбокса
                obj_cur.setChecked(False) if obj_cur.isChecked() else obj_cur.setChecked(True)
                # информационное окно про полное заполнение колонки
                PyQt5.QtWidgets.QMessageBox.information(self, 'Блокировка не получилась',
                                                        f'Зафиксируйте все колонки о спортсменах, кроме Жеребьёвки')

            else:
                if flag_fill_col:
                    print('"нужные" чекбоксы зафиксированы и поля в колонке "период" заполнены')

                    # пробегает по всем объектам, ищет по совпадению в имени название колонки и реагирует
                    for unit, unit_obj in self.dict_all_units.items():
                        # номер колонки
                        unit_col = unit.split('_')[-1]

                        # поиск конкретных объектов из конкретной колонки
                        if (obj_cur_col == unit_col) and \
                                ((unit_obj.__class__ is PyQt5.QtWidgets.QComboBox) or
                                 (unit_obj.__class__ is PyQt5.QtWidgets.QLineEdit)):

                            # блокировка или разблокировка объекта на форме
                            if obj_cur.isChecked():
                                unit_obj.setEnabled(False)
                            else:
                                unit_obj.setEnabled(True)

                    if obj_cur.isChecked():
                        # действия после блокировки колонки - расчёт очков в периоде
                        self.calc_period(obj_cur)

                else:
                    # если не всё заполнено, то возвращаю исходное состояние чекбокса
                    obj_cur.setChecked(False)

                    # если не всё заполнено, то перевожу фокус на первый "пустой" объект в колонке
                    self.shift_focus_on_empty_unit(obj_cur_col)

                    # информационное окно про полное заполнение колонки
                    PyQt5.QtWidgets.QMessageBox.information(self, 'Блокировка не получилась',
                                                            f'Заполните все поля в колонке')

        # оставшийся вариант для неизвестной ситуации
        else:
            print('!!! ...', obj_cur_name)
            pass

    # функция проверки блокировки нужных колонок перед расчётом
    def check_for_calc(self) -> bool:
        """Функция проверки блокировки нужных колонок перед расчётом"""
        print(self.check_for_calc.__name__) if DEBUG else ...

        # множество названий колонок, которые должны быть "нажаты" чтобы начать считать
        tuple_of_names = ('fio', 'team', 'rank', 'zona')

        # флаг нажатия всех нужных чекбоксов
        flag_for_calc = False

        # список для сбора всех значений чекбоксов
        list_checkbox_checked = []

        # пробегает по всем объектам, ищет по совпадению в имени название колонки и реагирует
        for unit, unit_obj in self.dict_all_units.items():
            # имя колонки
            unit_name = unit.split('_')[1]
            # класс объекта
            unit_class = unit_obj.__class__

            # поиск конкретных объектов с названием из множества
            if (unit_class is PyQt5.QtWidgets.QCheckBox) and (unit_name in tuple_of_names):
                list_checkbox_checked.append(unit_obj.isChecked())

        # проверка на "нажатость" всех чекбоксов
        if all(list_checkbox_checked):
            # если все нажаты, то можно приступить к расчёту
            flag_for_calc = True

        return flag_for_calc

    # функция расчёта очков в периоде
    def calc_period(self, calculate_column: PyQt5.QtWidgets.QCheckBox) -> None:
        """Функция расчёта очков в периоде"""
        print(self.calc_period.__name__) if DEBUG else ...

        print('расчёт очков в периоде', calculate_column.objectName(), calculate_column)

    # функция определения заполнены ли все объекты в колонке
    def get_flag_fill_column(self, cur_column: str) -> bool:
        """Функция определения заполнены ли все объекты в колонке"""
        print(self.get_flag_fill_column.__name__) if DEBUG else ...

        # список для хранения заполненности объекта в колонке
        list_of_fill_col = []

        for unit, unit_obj in self.dict_all_units.items():
            # номер колонки
            unit_col = unit.split('_')[-1]

            # поиск объектов из конкретной колонки
            if (cur_column == unit_col) and \
                    ((unit_obj.__class__ is PyQt5.QtWidgets.QComboBox) or
                     (unit_obj.__class__ is PyQt5.QtWidgets.QLineEdit)):

                # проверка на пустоту значения объекта
                # если у объекта есть параметр который содержит значение (text или item)
                # то True если не пустое (строка из пробелов считается пустой), иначе False
                if hasattr(unit_obj, 'text'):
                    list_of_fill_col.append(True if unit_obj.text() and not unit_obj.text().isspace() else False)
                elif hasattr(unit_obj, 'currentText'):
                    list_of_fill_col.append(True if unit_obj.currentText() else False)

        # установка флага заполненности колонки
        flag_fill_col = True if all(list_of_fill_col) else False

        return flag_fill_col

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

    # функция переназначения нажатия клавиш в главном окне
    def keyPressEvent(self, event) -> None:
        """Функция переназначения нажатия клавиш в главном окне"""
        print(self.keyPressEvent.__name__) if DEBUG else ...

        # имя объекта, который послал событие
        if self.focusWidget():
            unit_name = self.focusWidget().objectName()
        else:
            # TODO
            # !!! Поставить тут фокус на что-нибудь
            pass

        # # колонка объекта, который послал событие
        # unit_col = self.get_num_col_of_unit(unit_name)

        # выбор нажатой кнопки
        if event.key() == PyQt5.QtCore.Qt.Key_Escape:
            # print('Key_Escape ... ', event.key().numerator)

            # TODO
            # написать выбор выхода из программы ДА-НЕТ
            # написать обработку нажатия ENTER - переход на строку ниже в одной колонке

            # процесс выхода из программы
            self.exit_common()

        elif event.key() == PyQt5.QtCore.Qt.Key_Up:
            # print('Key_Up ... ', event.key().numerator)
            self.shift_focus_up(unit_name)
        elif event.key() == PyQt5.QtCore.Qt.Key_Down:
            # print('Key_Down ... ', event.key().numerator)
            self.shift_focus_down(unit_name)
        elif event.key() == PyQt5.QtCore.Qt.Key_Left:
            print('Key_Left ... ', event.key().numerator)
        elif event.key() == PyQt5.QtCore.Qt.Key_Right:
            print('Key_Right ... ', event.key().numerator)
        elif event.key() == PyQt5.QtCore.Qt.Key_Enter:
            # print('Key_Enter (rightEnter) ... ', event.key().numerator)
            self.shift_focus_down(unit_name)
        elif event.key() == PyQt5.QtCore.Qt.Key_Return:
            # print('Key_Return (leftEnter) ... ', event.key().numerator)
            self.shift_focus_down(unit_name)
        else:
            print('unknown ... ', event.key().numerator)

        super().keyPressEvent(event)

    # функция переназначения нажатия мыши в главном окне
    def mousePressEvent(self, event) -> None:
        """Функция переназначения нажатия мыши в главном окне"""
        print(self.mousePressEvent.__name__) if DEBUG else ...

        # print('pressed key: ' + str(event.button()))
        # if event.button() == PyQt5.QtCore.Qt.LeftButton:
        #     print('pressed key: ' + str(event.button()))
        # super().mousePressEvent(event)

    # функция получения номера колонки из названия объекта на форме
    def get_num_col_of_unit(self, obj: str) -> str:
        """Функция получения номера колонки из названия объекта на форме"""
        print(self.get_num_col_of_unit.__name__) if DEBUG else ...

        # получаю имя колонки по первому вхождению в имя объекта
        obj_name_col = obj.split('_')[0]

        # получение номера колонки (тип - текстовый)
        if obj_name_col in ('checkbox', 'label'):
            return obj.split('_')[2]
        elif obj_name_col == 'sportik':
            return obj.split('_')[3]

    # функция смещения фокуса на форме по реакции клавиш клавиатуры
    def shift_focus_down(self, obj: str) -> None:
        """Функция смещения фокуса на форме по реакции клавиш клавиатуры"""
        print(self.shift_focus_down.__name__) if DEBUG else ...

        # временный список разделения строки имени объекта
        temp_list = obj.split('_')

        if temp_list[0] == 'sportik':
            # переменная для определения прыжка в начало строк
            q_anglers = SETTINGS_DATA_DEF['competition_action']['COMP_q_anglers']

            # определение следующего номера строки
            if int(temp_list[2]) >= int(q_anglers):
                temp_list[2] = '1'
            else:
                temp_list[2] = str(int(temp_list[2])+1)

            # сбор нового имени объекта
            new_temp_list = '_'.join(temp_list)

            # смещение фокуса на новый объект
            self.dict_all_units[new_temp_list].setFocus()

    # функция смещения фокуса на форме по реакции клавиш клавиатуры
    def shift_focus_up(self, obj: str) -> None:
        """Функция смещения фокуса на форме по реакции клавиш клавиатуры"""
        print(self.shift_focus_up.__name__) if DEBUG else ...

        # временный список разделения строки имени объекта
        temp_list = obj.split('_')

        if temp_list[0] == 'sportik':
            # переменная для определения прыжка в начало строк
            q_anglers = SETTINGS_DATA_DEF['competition_action']['COMP_q_anglers']

            # определение следующего номера строки
            if int(temp_list[2]) <= 1:
                temp_list[2] = str(q_anglers)
            else:
                temp_list[2] = str(int(temp_list[2])-1)

            # сбор нового имени объекта
            new_temp_list = '_'.join(temp_list)

            # смещение фокуса на новый объект
            self.dict_all_units[new_temp_list].setFocus()

    # функция смещения фокуса на форме на пустой объект
    def shift_focus_on_empty_unit(self, cur_column: str) -> None:
        """Функция смещения фокуса на форме на пустой объект"""
        print(self.shift_focus_on_empty_unit.__name__) if DEBUG else ...

        for unit, unit_obj in self.dict_all_units.items():
            # номер колонки объекта
            unit_col = unit.split('_')[-1]

            # поиск объектов из конкретной колонки
            if (cur_column == unit_col) and (isinstance(unit_obj, PyQt5.QtWidgets.QComboBox)
                                             or isinstance(unit_obj, PyQt5.QtWidgets.QLineEdit)):

                # выбор поля с текстом у текущего объекта
                if hasattr(unit_obj, 'text'):
                    content = getattr(unit_obj, 'text')()
                elif hasattr(unit_obj, 'currentText'):
                    content = getattr(unit_obj, 'currentText')()

                # проверка на пустоту значения объекта
                if not content or content.isspace():
                    # смещение фокуса на "пустой" объект
                    self.dict_all_units[unit].setFocus()

    # функция получения координат и запись их в переменную экземпляр класса
    def get_coords(self) -> None:
        """Функция получения координат и запись их в переменную экземпляре класса"""
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
        # SETTINGS_COMMON_DEF['settings_window_about']['window_coords_x'] = self.frame_geometry.x()
        # SETTINGS_COMMON_DEF['settings_window_about']['window_coords_y'] = self.frame_geometry.y()

    # функция общего выхода из программы
    def exit_common(self) -> None:
        """Функция общего выхода из программы"""
        print('_' * 25) if DEBUG else ...
        print(self.exit_common.__name__) if DEBUG else ...

        # сохранение настроек перед выходом
        save_settings()
        # сохранения последнего состояния значений на форме
        save_last_state(self)
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

    # модель объектов в главном окне
    global SETT_MODEL
    SETT_MODEL = fcs.SETT_MODEL

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


    global LAST_STATE
    print('-'*30)
    pp(SETTINGS_DATA_DEF['competition_action'])
    # сюда добавить обработку данных из последнего состояния
    print('-'*30)
    if LAST_STATE == None:
        pp(LAST_STATE)
    else:
        pp(LAST_STATE['competition_action'])
    print('-' * 30)


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
            # первая версия проверки через сравнение типов
            # if type(val) != type(cur_dict[key]):
            if not isinstance(val, type(cur_dict[key])):
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

    # проверка на корректность и наличие ключей настроек
    data = repair_settings(SETTINGS_DATA_DEF, fcs.SETT_DEF_SOFT)

    # запись настроек в файл
    with open(SETTINGS_FILE, "wb") as file_settings:
        tomli_w.dump(data, file_settings)


# универсальная функция для описания полей и расчёта их координат на форме
def get_list_fields_and_coords(start_x: int, start_y: int, shift_x: int,
                               shift_y: int, field_h: int, q_sportsmen: int) -> list:
    """Универсальная функция для описания полей и расчёта их координат на форме"""
    print(get_list_fields_and_coords.__name__) if DEBUG else ...

    # --- СОЗДАНИЕ СПИСКА ОБЪЕКТОВ
    # итоговый список всех полей и их координаты
    list_coord_of_fields = []

    # распределение входных переменных
    # расстояние между объектами на форме
    gap_x = shift_x
    gap_y = shift_y
    # высота для всех полей
    field_height = field_h
    # точка начала отчёта
    start_dot_x = start_x
    start_dot_y = start_y + 2 * gap_y + 2 * field_height  # сдвиг для добавления вверх описаний и чекбоксов
    # количество спортиков
    q_sportiks = q_sportsmen
    # шаг по вертикали, далее по коду будет изменяться
    field_step_y = start_dot_y

    # переменные которые могут принимать значение больше "1"
    q_zone = SETTINGS_DATA_DEF['competition_action']['COMP_q_zone']
    q_tur = SETTINGS_DATA_DEF['competition_action']['COMP_q_tur']
    q_period = SETTINGS_DATA_DEF['competition_action']['COMP_q_period']
    model = SETT_MODEL

    # пустой список для собирания конечного списка объектов для рендеринга
    total_model = []

    # цикл для генерации объектов конечного списка на основе общей модели
    for block in model:
        # есть колонки, которые могут повторяться
        # если это та колонка, то добавляется она столько, сколько в настройках соревнования
        if block[0] == 'zona':
            for i in range(1, q_zone + 1):
                total_model.append(block)

        elif block[0] == 'period':
            # разбивка периодов по турам
            for i in range(1, q_tur + 1):
                for j in range(1, q_period + 1):
                    total_model.append(block)

                # добавление после каждого тура колонки points как итога за тур
                total_model.append(model[7])

        elif block[0] == 'points':
            # пропускаю потому, что эта строка нужна после каждого тура, а не по-очереди в модели
            pass

        else:
            # простое добавление колонки из модели
            total_model.append(block)

    # цикл расчёта координат полей для соревнования
    for n_sportik in range(1, q_sportiks + 1):
        # шаг вправо начинается с первой точки и идёт вправо
        field_step_x = start_dot_x
        # список координат в строке
        list_coord_of_field = []

        # переменная счётчик колонок
        field_count = 1

        # проход по строке полей
        for field in total_model:
            # формирование имени спортика
            field_name = 'sportik' + '_' + field[0] + '_' + str(n_sportik) + '_' + str(field_count)
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

            # переход на следующую колонку
            field_count += 1

        # добавление шага вниз на промежуток между строками полей
        field_step_y = field_step_y + field_height + gap_y

        # добавление в главный список списка строки полей
        list_coord_of_fields.append(list_coord_of_field)

    # --- СОЗДАНИЕ СПИСКА ОПИСАНИЙ
    # распределение входных переменных
    # расстояние между объектами на форме
    gap_x = shift_x
    gap_y = shift_y
    # высота для всех полей
    field_height = field_h
    # точка начала отчёта
    start_dot_x = start_x
    start_dot_y = start_y
    # шаг по вертикали, далее по коду будет изменяться
    field_step_y = start_dot_y

    # список координат в строке
    list_desc_of_fields = []

    # цикл расчёта координат полей для описания
    for unit_line in range(1, 2 + 1):
        # шаг вправо начинается с первой точки и идёт вправо
        field_step_x = start_dot_x
        # переменная счётчик колонок
        field_count = 1

        # временный цикл для хранения одной строки выводимых объектов
        list_desc_of_field = []

        # выбор добавляемой строки
        if unit_line == 1:
            u_name = 'checkbox'
        else:
            u_name = 'label'

        # проход по строке полей
        for field in total_model:
            # формирование имени выводимого поля
            field_name = u_name + '_' + field[0] + '_' + str(field_count)
            # field_name = field[0] + '_' + str(field_count)
            # выбор ширины поля
            field_width = field[1]
            # вид объекта для вывода
            field_obj = u_name

            # добавление в список параметров объекта
            list_desc_of_field.append(field_name)
            list_desc_of_field.append(field_step_x)
            list_desc_of_field.append(field_step_y)
            list_desc_of_field.append(field_width)
            list_desc_of_field.append(field_height)
            list_desc_of_field.append(field_obj)

            # увеличение шага вправо на ширину поля
            field_step_x = field_step_x + field_width

            # увеличение шага вправо на ширину промежутка между полями
            field_step_x = field_step_x + gap_x

            # переход на следующую колонку
            field_count += 1

        # добавление шага вниз на промежуток между строками полей
        field_step_y = field_step_y + field_height + gap_y

        # добавление в главный список списка строки полей
        list_desc_of_fields.append(list_desc_of_field)

    # объединение списков описаний и полей
    list_of_fields = list_desc_of_fields + list_coord_of_fields

    return list_of_fields


# функция загрузки последнего состояния значений на форме
def load_last_state() -> None:
    """Функция загрузки последнего состояния значений на форме"""
    print(load_last_state.__name__) if DEBUG else ...

    global LAST_STATE

    # если файл существует, то читаю его и правлю настройки, рендерю и заполняю значениями из файла
    if os.path.exists(LAST_STATE_FILE):
        with open(LAST_STATE_FILE, "rb") as fl_last_state:
            LAST_STATE = tomllib.load(fl_last_state)


# функция сохранения последнего состояния значений на форме
def save_last_state(obj: PyQt5.QtWidgets.QMainWindow) -> None:
    """Функция сохранения последнего состояния значений на форме"""
    print(save_last_state.__name__) if DEBUG else ...

    # словарь для хранения настроек с последующим переводом в toml
    last_state_dict = {}

    # СЕКЦИЯ НАСТРОЕК соревнования
    comp_section = SETTINGS_DATA_DEF['competition_action']
    # беру сразу всю секцию из настроек
    last_state_dict['competition_action'] = comp_section

    # СЕКЦИЯ ЗНАЧЕНИЙ полей которые редактируются на главной форме
    # читаю все объекты двух типов и складываю их в словарь значений
    list_of_edits = obj.findChildren(PyQt5.QtWidgets.QLineEdit)
    list_of_combo = obj.findChildren(PyQt5.QtWidgets.QComboBox)
    # словарь значений объектов на форме
    last_state_dict['competition_fields'] = {}

    # получение имён и значений объектов
    for unit in list_of_edits:
        last_state_dict['competition_fields'][unit.objectName()] = unit.text()
    for unit in list_of_combo:
        last_state_dict['competition_fields'][unit.objectName()] = unit.currentIndex()

    # СЕКЦИЯ ДЛЯ ДОП ПОЛЕЙ, например для сохранения состояния жеребьёвки
    last_state_dict['misc'] = {}

    # перенос состояния жеребьёвки
    for unit in obj.findChildren(PyQt5.QtWidgets.QCheckBox):
        if 'checkbox_lottery' in unit.objectName():
            last_state_dict['misc'][unit.objectName()] = unit.isChecked()

    # запись настроек в файл
    with open(LAST_STATE_FILE, "wb") as file_settings:
        tomli_w.dump(last_state_dict, file_settings)


# функция непосредственного выхода из программы
def exit_app() -> None:
    """Функция непосредственного выхода из программы"""
    print(exit_app.__name__) if DEBUG else ...

    sys.exit()


# основная функция запуска приложения
def run() -> None:
    """Основная функция запуска приложения"""
    print(run.__name__) if DEBUG else ...

    # загрузка последнего состояния значений на форме
    load_last_state()

    # чтение настроек программы
    read_settings()

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')

    screen_geometry = app.desktop().screenGeometry()
    SETTINGS_DATA_DEF['settings_soft']['screen_resolution_x'] = screen_geometry.width()
    SETTINGS_DATA_DEF['settings_soft']['screen_resolution_y'] = screen_geometry.height()

    app_window_main = WindowMain()
    app_window_main.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run()

# print(*list_of_fields, sep='\n')

# print()
# for i in dir(event):
#     if '_' not in i:
#         print(f'... {i} ... {getattr(event, i, None)}')
#         print('_' * 45)
# print()

# # информационное окно про полное заполнение колонки
# PyQt5.QtWidgets.QMessageBox.information(self, "ошибка", f"инфо текст")

# print(f'{event.key().as_integer_ratio() = } ... {event.key().bit_length() = }')
# print(f'{event.key().conjugate() = } ... {event.key().denominator = }')
# print(f'{event.key().numerator = } ... {event.key().real = }')
# print(f'{event.key().imag = }')

# .strip() .isspace()

# print(f'{hasattr(unit_obj, "text") = }')
# print(f'{getattr(unit_obj, "text")() = }')

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
# from pprint import pprint as pp


# определение констант
# выводит информацию по входу в каждую функцию
DEBUG = False
# название файла с настройками
SETTINGS_FILE = 'fish_settings.toml'
# набор констант для открытого и закрытого хранения
SETTINGS_DATA_DEF = None
SETTINGS_COMMON_DEF = None
SETT_MODEL = None


# класс главного окна
class WindowMain(PyQt5.QtWidgets.QMainWindow):
    """Класс главного окна"""

    # описание главного окна
    def __init__(self) -> None:
        """Метод инициализации класса главного окна"""
        print(self.__init__.__name__) if DEBUG else ...

        super().__init__()

        # словарь всех объектов рендеринга, нужен для хранения, поиска и чистки на форме
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

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.cleaner = self.file.addAction('cleaner')
        self.adder = self.file.addAction('adder')
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.file_sep = self.file.addSeparator()
        self.file_exit = self.file.addAction('Выход')
        self.file_open.triggered.connect(self.window_file_open)
        self.file_save.triggered.connect(self.window_file_save)
        self.file_send.triggered.connect(self.window_file_send)
        self.file_exit.triggered.connect(self.window_file_exit)

        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        self.cleaner.triggered.connect(self.del_form_units)
        self.adder.triggered.connect(self.add_form_units)
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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

    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # функция очистки главного окна от объектов
    def del_form_units(self) -> None:
        """Функция очистки главного окна от объектов"""
        print(self.clean_form.__name__) if DEBUG else ...

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
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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

        # окно настроек, надпись на нём и размеры
        window_settings = PyQt5.QtWidgets.QWidget(self, PyQt5.QtCore.Qt.Window)
        window_settings.setWindowTitle(comp_window_n)
        window_settings.setWindowModality(PyQt5.QtCore.Qt.WindowModal)
        window_settings.setGeometry(comp_window_x + 25, comp_window_y + 25, comp_window_w, comp_window_h)
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
        # print(*list_of_units, sep='\n')

        # вставка на форму объектов
        q_steps = 6                                              # количество шагов считывания из списка
        for unit_sting in list_of_units:
            # временный счётчик для добавления к описанию - порядковый номер описания
            counter_zona = 0
            counter_period = 0
            for i in range(0, len(unit_sting), q_steps):
                unit = unit_sting[i:(i+q_steps)]

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
                        line_edit.setMaxLength(4)
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
                    # !!!
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
                        check_box.setText(' '*unit_w)
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
        obj_cur = self.sender()
        obj_cur_col = obj_cur.objectName().split('_')[-1]
        obj_cur_name = obj_cur.objectName().split('_')[1]

        # определение - какой чек бокс в какой колонке нажат
        if obj_cur_name == 'lottery':
            # количество спортсменов
            q_anglers = SETTINGS_DATA_DEF['competition_action']['COMP_q_anglers']
            lottery_list = [x for x in range(1, q_anglers+1)]
            random.shuffle(lottery_list)

            # пробегает по всем объектам, ищет по совпадению в имени название колонки и реагирует
            for unit, obj_unit in self.dict_all_units.items():
                if 'sportik_lottery' in unit:
                    # номер строки спортсмена
                    obj_unit_row = int(unit.split('_')[2])
                    # заполнение поля жеребьёвки соответствующим значением из списка жеребьёвок
                    obj_unit.setText(str(lottery_list[obj_unit_row-1]))

            # блокирую и скрываю чекбокс потому, что жеребьёвка проводится один раз за соревнования
            if obj_cur.isChecked():
                # возможно тут надо ещё и прятать чекбокс, но не уверен
                obj_cur.setEnabled(False)
                # obj_cur.setVisible(False)

        elif obj_cur_name in ('fio', 'team', 'rank', 'zona', 'period'):
            # пробегает по всем объектам, ищет по совпадению в имени название колонки и реагирует
            for unit, obj_unit in self.dict_all_units.items():
                # номер колонки
                obj_unit_col = unit.split('_')[-1]

                # поиск объектов из конкретной колонки
                if (obj_cur_col == obj_unit_col) and (obj_unit.__class__ != PyQt5.QtWidgets.QCheckBox):

                    if hasattr(obj_unit, 'text'):
                        if obj_unit.text():
                            print(unit, ' ... ', obj_unit.text())
                            print()

                    if obj_cur.isChecked():
                        obj_unit.setEnabled(False)
                    else:
                        obj_unit.setEnabled(True)
        else:
            print(obj_cur_name)
            pass

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
    def keyPressEvent(self, event):
        """Функция переназначения нажатия клавиш в главном окне"""
        print(self.keyPressEvent.__name__) if DEBUG else ...

        # выбор нажатой кнопки
        if event.key() == PyQt5.QtCore.Qt.Key_Escape:
            print('ESC')

            # TODO
            # написать выбор выхода из программы ДА-НЕТ
            # написать обработку нажатия ENTER - переход на строку ниже в одной колонке

            # процесс выхода из программы
            self.exit_common()
        elif event.key() == PyQt5.QtCore.Qt.Key_Up:
            print('UP')
        elif event.key() == PyQt5.QtCore.Qt.Key_Down:
            print('DOWN')
        elif event.key() == PyQt5.QtCore.Qt.Key_Left:
            print('LEFT')
        elif event.key() == PyQt5.QtCore.Qt.Key_Right:
            print('RIGHT')
        elif event.key() == PyQt5.QtCore.Qt.Key_Enter:
            # EnterKeyDefault
            # 16777220
            # 16777221
            print('ENTER 16777220')
        else:
            print('pressed key: ' + str(event.key()))
            # print(f'{event.key().as_integer_ratio() = } ... {event.key().bit_length() = }')
            # print(f'{event.key().conjugate() = } ... {event.key().denominator = }')
            # print(f'{event.key().numerator = } ... {event.key().real = }')
            # print(f'{event.key().imag = }')

        # print('pressed key: ' + str(event.key()))

        super().keyPressEvent(event)

    # функция переназначения нажатия мыши в главном окне
    def mousePressEvent(self, event):
        """Функция переназначения нажатия мыши в главном окне"""
        print(self.mousePressEvent.__name__) if DEBUG else ...

        # print('pressed key: ' + str(event.button()))
        # if event.button() == PyQt5.QtCore.Qt.LeftButton:
        #     print('pressed key: ' + str(event.button()))
        # super().mousePressEvent(event)

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
        # SETTINGS_COMMON_DEF['settings_window_about']['window_coords_x'] = self.frame_geometry.x()
        # SETTINGS_COMMON_DEF['settings_window_about']['window_coords_y'] = self.frame_geometry.y()

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
    start_dot_y = start_y + 2*gap_y + 2*field_height    # сдвиг для добавления вверх описаний и чекбоксов
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


# функция непосредственного выхода из программы
def exit_app() -> None:
    """Функция непосредственного выхода из программы"""
    print(exit_app.__name__) if DEBUG else ...

    sys.exit()


# основная функция запуска приложения
def run() -> None:
    """Основная функция запуска приложения"""
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

# print(*list_of_fields, sep='\n')

# print()
# for i in dir(event):
#     if '_' not in i:
#         print(f'... {i} ... {getattr(event, i, None)}')
#         print('_' * 45)
# print()

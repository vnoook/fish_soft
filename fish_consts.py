# файл констант по-умолчанию

# константы для сохранения в файл
SETT_DEF_SOFT = {
    'settings_window_main': {
        'window_coords_h': 400,
        'window_coords_w': 1200,
        'window_coords_x': 100,
        'window_coords_y': 100},
    'settings_soft': {
        # 'emergency_exit': False,
        # 'CLUB_ID': '1A2B-3C4D-5E6F',
        # 'SOFT_LAST_OPEN': '1980-06-30',          # fromisoformat('YYYY-MM-DD')
        # 'COMP_DATA_COMPETITION': '2022-02-24',   # fromisoformat('YYYY-MM-DD')
        'screen_resolution_x': 1400,
        'screen_resolution_y': 900},
    'competition_action': {
        'COMP_q_tur': 2,
        'COMP_q_period': 4,
        'COMP_q_zone': 2,
        # 'COMP_q_sector': 1,
        # 'COMP_d_period': 45,
        'COMP_q_anglers': 8},
    'misc': {}
}

# константы для работы программе, остаются в памяти
SETT_DEF_COMMON = {
    'version': '0.1.2',
    'window_name_main': 'ЧСВ - НХНЧ',
    'about_text': 'Чтобы Соревнования Выиграть - "Ни хвоста, Ни чешуи"',
    'window_name_set_comp': 'Настройки соревнования',
    'window_name_set_soft': 'Настройки программы',
    'window_name_about': 'О программе',
    # 'soft_db_file': 'db_competition.db',
    'file_settings_soft': 'fish_settings.toml',
    'name_of_zone': ['Зона А', 'Зона Б', 'Зона В', 'Зона Г', 'Зона Д', 'Зона Е', 'Зона Ж', 'Зона З'],
    # 'name_of_sector': 'Сектор XXX',    # Сектор 1, Сектор 2, Сектор 3 ...
    'form_sizes': {
        'min_width': 300,
        'min_height': 300,
        'start_x': 10,
        'start_y': 100,
        'obj_h': 20},
    'form_gaps': {
        'gap_x': 5,
        'gap_y': 5},
    # 'competition_stat': {
    #     'COMP_q_fio': 1,
    #     'COMP_q_checkbox_in_line': 1,
    #     'COMP_q_desc_in_line': 1},
    'settings_window_set_comp': {
        'window_coords_h': 200,
        'window_coords_w': 400,
        'window_coords_x': 100,
        'window_coords_y': 100},
    'settings_window_set_soft': {
        'window_coords_h': 200,
        'window_coords_w': 400,
        'window_coords_x': 100,
        'window_coords_y': 100},
    # 'settings_window_about': {
    #     'window_coords_h': 100,
    #     'window_coords_w': 400,
    #     'window_coords_x': 100,
    #     'window_coords_y': 100},
    'misc': {}
}

# модель - список из полей (колонок) на форме - имя поля, длина, вид, описание поля для подписи
SETT_MODEL = (
              ('number', 30, 'edit_off', 'Номер'),
              ('lottery', 25, 'edit_off', 'Жереб'),
              ('fio', 120, 'edit_on', 'ФИО'),
              ('team', 120, 'edit_on', 'Команда'),
              ('rank', 30, 'edit_on', 'Разряд'),
              ('zona', 70, 'combobox_on', 'Зона'),
              ('period', 40, 'edit_on', 'П'),
              ('points', 30, 'edit_off', 'Очки'),
              ('team', 40, 'edit_off', 'МК'),
              ('self', 40, 'edit_off', 'МЛ')
)

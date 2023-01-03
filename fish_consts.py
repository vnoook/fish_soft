# файл констант по-умолчанию

SETT_DEF_SOFT = {
    'settings_window_main': {
        'window_coords_h': 400,
        'window_coords_w': 1200,
        'window_coords_x': 100,
        'window_coords_y': 100,
        'window_name': 'Название главного окна'},
    'settings_window_set_comp': {
        'window_coords_h': 400,
        'window_coords_w': 400,
        'window_coords_x': 100,
        'window_coords_y': 100,
        'window_name': 'Название окна настроек соревнований'},
    'settings_window_set_soft': {
        'window_coords_h': 400,
        'window_coords_w': 400,
        'window_coords_x': 100,
        'window_coords_y': 100,
        'window_name': 'Название окна настроек программы'},
    'settings_window_about': {
        'window_coords_h': 400,
        'window_coords_w': 400,
        'window_coords_x': 100,
        'window_coords_y': 100,
        'window_name': 'Название окна о программе'},
    'settings_soft': {
        'emergency_exit': True,
        'CLUB_ID': '1A2B-3C4D-5E6F',
        'SOFT_DB_FILE': 'db_competition.db',
        'SOFT_LAST_OPEN': '1980-06-30',         # fromisoformat('YYYY-MM-DD')
        'COMP_DATA_COMPETITION': '2022-02-24',  # fromisoformat('YYYY-MM-DD')
        'file_settings_soft': 'fish_settings.toml',
        'screen_resolution_x': 1400,
        'screen_resolution_y': 900}
}

SETT_DEF_COMP = {
    'competition_action': {
        'COMP_q_tur': 1,
        'COMP_q_period': 4,
        'COMP_q_zone': 1,
        'COMP_q_sector': 1,
        'COMP_d_period': 45,
        'COMP_q_anglers': 15
    }
}

SETT_DEF_additional = {
    'misc': {
        'name_of_zone': ["Зона А", "Зона Б", "Зона В", "Зона Г", "Зона Д", "Зона Е", "Зона Ж"],
        'name_of_sector': "Сектор XXX"  # Сектор 1, Сектор 2, Сектор 3 ...
    }
}

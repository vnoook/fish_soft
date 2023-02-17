# файл констант по-умолчанию

SETT_DEF_SOFT = {
    'settings_window_main': {
        'window_coords_h': 400,
        'window_coords_w': 1200,
        'window_coords_x': 100,
        'window_coords_y': 100},
    'settings_soft': {
        'emergency_exit': False,
        'CLUB_ID': '1A2B-3C4D-5E6F',
        'SOFT_LAST_OPEN': '1980-06-30',          # fromisoformat('YYYY-MM-DD')
        'COMP_DATA_COMPETITION': '2022-02-24',   # fromisoformat('YYYY-MM-DD')
        'screen_resolution_x': 1400,
        'screen_resolution_y': 900},
    'competition_action': {
        'COMP_q_tur': 1,
        'COMP_q_period': 4,
        'COMP_q_zone': 1,
        'COMP_q_sector': 1,
        'COMP_d_period': 45,
        'COMP_q_anglers': 15},
    'misc': {}
}

SETT_DEF_COMMON = {
    'version': '0.0.3',
    'window_name_main': 'ЧСВ - НХНЧ',
    'about_text': 'Чтобы Соревнования Выиграть - "Ни хвоста, Ни чешуи"',
    'window_name_set_comp': 'Настройки соревнования',
    'window_name_set_soft': 'Настройки программы',
    'window_name_about': 'О программе',
    'soft_db_file': 'db_competition.db',
    'file_settings_soft': 'fish_settings.toml',
    'name_of_zone': "Зона XXX",                  # Зона А, Зона Б, Зона В, Зона Г ...
    'name_of_sector': "Сектор XXX",              # Сектор 1, Сектор 2, Сектор 3 ...
    'form_sizes': {
        'min_width': 300,
        'min_height': 300,
        'start_x': 10,
        'start_y': 100,
        'obj_h': 20},
    'form_gaps': {
        'gap_x': 20,
        'gap_y': 10},
    'competition_stat': {
        'COMP_q_fio': 1,
        'COMP_q_checkbox_in_line': 1,
        'COMP_q_desc_in_line': 1},
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
    'settings_window_about': {
        'window_coords_h': 100,
        'window_coords_w': 400,
        'window_coords_x': 100,
        'window_coords_y': 100},

}

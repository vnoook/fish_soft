from pprint import pprint as pp

sett_def = {'settings_window_main': {
                'window_coords_h': 1200,
                'window_coords_w': 400,
                'window_coords_x': 100,
                'window_coords_y': 100,
                'window_name': 'Название главного окна'},
            'settings_window_about': {
                'window_coords_h': 400,
                'window_coords_w': 300,
                'window_coords_x': 99,
                'window_coords_y': 99,
                'window_name': 'Название окна о программе'},
            'settings_soft': {
                'emergency_exit': True,
                'file_settings_soft': 'fish_settings.toml',
                'screen_resolution_x': 1400,
                'screen_resolution_y': 900}}

sett_cur = {'settings_window_main': {
                'window_coords_h': 1200,
                'window_coords_w': 400,
                'window_coords_x': 100,
                'window_coords_y': 100,
                'window_name': 'Название главного окна'},
            'settings_window_about': {
                'window_coords_h': 400,
                'window_coords_w': 300,
                'window_coords_x': 99,
                'window_coords_y': 99,
                'window_name': 'Название окна о программе'},
            'settings_soft': {
                'emergency_exit': True,
                'file_settings_soft': 'fish_settings.toml',
                'screen_resolution_x': 1400,
                'screen_resolution_y': 900}}


# функция валидности ключей и их количества в файле настроек
def repair_settings(cur_dict: dict, def_dict: dict):
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
    return cur_dict


if __name__ == '__main__':
    print()
    pp(repair_settings(sett_cur, sett_def))
    print()

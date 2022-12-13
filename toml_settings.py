# TODO
# 1 - исправление ошибки когда дублируется строка в файле настроек
# 2 - переделать в сторону порядка записи параметров в файл
# 3 - переделать формирование файла настроек с добавлением разделов в скобках []

import sys
if sys.version_info < (3, 11):
    import os.path
    import tomli as tomllib
    import tomli_w
    import datetime
else:
    import os.path
    import tomllib
    import tomli_w
    import datetime


# название файла настроек по-умолчанию
SETTINGS_FILE_DEF = "toml_settings.toml"
# список настроек по-умолчанию - ..., клуб, программы, соревнования, ...
SETTINGS_DATA_DEF = {
    # файл настроек SET_
    "SET_VER": 1,
    "SET_Q": 18,
    # клуб CLUB_
    "CLUB_ID": "1A2B-3C4D-5E6F",
    # программа SOFT_
    "SOFT_DB_FILE": "db_competition.db",
    "SOFT_LAST_OPEN": "1980-06-30",  # fromisoformat('YYYY-MM-DD')
    "SOFT_MAIN_WINDOW_SIZE": "1300:500",
    # соревнование COMP_
    "COMP_DATA_COMPETITION": "2022-02-24",  # fromisoformat('YYYY-MM-DD')
    "COMP_q_tur": 1,
    "COMP_q_period": 4,
    "COMP_q_zone": 1,
    "COMP_q_sector": 1,
    "COMP_d_period": 45,
    "COMP_q_anglers": 15,
    # другие настройки OTH_
    "OTH_PER1": 13,
    "OTH_PER2": 3,
    "OTH_PER3": 40,
    "OTH_PER4": 999,
    "OTH_PER5": "abcdef"
}


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


# функция сохранения данных в файл, формат TOML
def save_settings(data: dict, file: str):
    # проверка на правильность входных данных и запись
    if type(data) == dict:
        # перед записью валидируется набор настроек
        repair_settings(data, SETTINGS_DATA_DEF)
        # запись настроек в файл
        with open(file, "wb") as fl_set:
            tomli_w.dump(data, fl_set)
        return True
    else:
        print('Неправильные входные данные - ожидается словарь')
        return False


# функция чтения файла с настройками
def read_settings(file_settings: str):
    # если файл существует, то прочитать содержимое
    if os.path.exists(file_settings):
        with open(file_settings, "rb") as fl_set:
            data = tomllib.load(fl_set)
        return data
    else:
        # иначе содержимое считается значениями по-умолчанию
        save_settings(SETTINGS_DATA_DEF, SETTINGS_FILE_DEF)
        return SETTINGS_DATA_DEF


if __name__ == '__main__':
    print()

    settings_dict = read_settings(SETTINGS_FILE_DEF)
    print(settings_dict)
    print()

    settings_dict['SOFT_LAST_OPEN'] = str(datetime.datetime.now())
    settings_dict['OTH_PER4'] = 1000
    print(settings_dict)
    print()

    save_settings(settings_dict, SETTINGS_FILE_DEF)
    print(settings_dict)
    print()

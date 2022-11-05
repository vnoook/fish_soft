import os.path
import tomllib
import tomli_w
import datetime

# название файла настроек по-умолчанию
SETTINGS_FILE_DEF = "settings.toml"
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
    "OTH_PER5": "abcdefghij"
}


# функция валидности ключей и их количества в файле настроек
def repair_settings(cur_dict: dict, def_dict: dict):
    # print()
    # print('... проверка валидности настроек ...')
    # print(cur_dict)
    # проверяю на нехватку нужных ключей в словаре и если нет, то добавляю из дефолтных
    for key in def_dict:
        if key not in cur_dict:
            cur_dict[key] = def_dict[key]
    # print(cur_dict)
    # проверяю на наличие лишних ключей в словаре и если есть лишние, то удаляю их
    list_keys = []
    for key in cur_dict:
        if key not in def_dict:
            list_keys.append(key)
    for key in list_keys:
        del cur_dict[key]
        # cur_dict.pop(key, None)
    del list_keys
    # print(cur_dict)
    # print('... проверка валидности настроек ... OK')
    # print(cur_dict)
    # print()
    return cur_dict


# функция сохранения данных в файл, формат TOML
def save_settings(data: dict, file: str):
    # перед записью проверяется количество вхождений, их количество сохранено в одном из параметров
    repair_settings(data, SETTINGS_DATA_DEF)

    if type(data) == dict:
        with open(file, "wb") as fl_set:
            tomli_w.dump(data, fl_set)
        return True
    else:
        print('Неправильные входные данные - ожидается словарь')
        return False


# функция чтения файла с настройками
def read_settings(file_settings: str):
    if os.path.exists(file_settings):
        with open(file_settings, "rb") as fl_set:
            data = tomllib.load(fl_set)
        return data
    else:
        print(f'Ожидается файл "{file_settings}"')
        print(f'Если его нет, то создаю новый со значениями по-умолчанию')
        save_settings(SETTINGS_DATA_DEF, SETTINGS_FILE_DEF)
        print(f'Файл "{file_settings}" создан, поменяйте настройки в программе под Ваши условия')
        return None


if __name__ == '__main__':
    settings_dict = read_settings(SETTINGS_FILE_DEF)
    print(settings_dict)

    settings_dict['SOFT_LAST_OPEN'] = str(datetime.datetime.now())
    print(settings_dict)

    save_settings(settings_dict, SETTINGS_FILE_DEF)




# print(type(tomli_w.dumps(setting1)))
# print(tomli_w.dumps(setting1))
#
# doc = {"one": 1, "two": 2, "pi": 3}
# with open("conf1.toml", "wb") as f:
#     tomli_w.dump(doc, f)
#
# with open("conf2.toml", "wb") as f:
#     tomli_w.dump(dict_data1, f)

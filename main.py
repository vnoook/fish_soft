# вспомогательные данные для расчётов консольной версии
# впоследствии это будет браться из базы ИЛИ формы GUI
# !!! главное чтобы в table_anglers И table_anglers_rank И table_anglers_teams ключи id совпадали

import uuid

# таблица рыбаков с id и fio
table_anglers = {1: 'Иванов', 2: 'Петров', 3: 'Ветров', 4: 'Фролов',
                 5: 'Попков', 6: 'Котова', 7: 'Рыбова', 8: 'Локтев'}
# таблица рыбаков с id и разрядами
table_anglers_rank = {1: '1 разряд', 2: '2 разряд', 3: '3 разряд', 4: '1 разряд',
                      5: None, 6: 'МС', 7: 'КМС', 8: 'МС'}
# таблица рыбаков с id и командами
table_anglers_teams = {1: 'Караси', 2: 'Караси', 3: 'Тим-Ту', 4: 'FreeHunt',
                       5: 'Тим-Ту', 6: 'FreeHunt', 7: None, 8: None}
# таблица поимок в Tournament.quantity_period периодах
table_catches = {1: (1,  4,  7,  1,  1,  9),
                 2: (2,  52, 7,  2,  2,  9),
                 3: (43, 4,  7,  6,  3,  9),
                 4: (1,  0,  12, 22, 4,  9),
                 5: (15, 4,  12, 71, 5,  9),
                 6: (15, 18, 1,  0,  6,  9),
                 7: (0,  16, 13, 3,  7,  9),
                 8: (5,  17, 1,  4,  8,  9)
                 }


# класс Соревнование
class Tournament:
    def __init__(self, q_tur=1, q_period=4, q_zone=1, q_sector=None, d_period=45, q_anglers=15):
        # TODO
        # дата начала соревнований
        # уникальный номер сорев для списка сорев в будущем, делать через uuid.uuid4()

        # количество туров
        self.quantity_tur = q_tur
        # количество периодов
        self.quantity_period = q_period
        # количество зон
        self.quantity_zone = q_zone
        # количество секторов
        self.quantity_sector = q_sector
        # длительность периода в минутах
        self.duration_period = d_period
        # количество соревнующихся
        self.quantity_anglers = q_anglers

    def get_tournament_info(self):
        q_sector = 'нет' if self.quantity_sector is None else self.quantity_sector
        q_zone = 'нет' if self.quantity_zone is None else self.quantity_zone
        return f'В этих соревнованиях: туров {self.quantity_tur}, ' \
               f'периодов {self.quantity_period}, ' \
               f'зон {q_zone}, ' \
               f'секторов {q_sector}, ' \
               f'период длится {self.duration_period} минут, ' \
               f'количество соревнующихся {self.quantity_anglers}'


# класс Рыбак
class Angler:
    def __init__(self, a_id, a_fio, a_rank=None, a_team=None):
        # TODO
        # тут сделать проверку входных данных, а только потом присвоить
        # id только число, фио только буквы, ранг и команда None если не заполнено
        self.__angler_uid = uuid.uuid4()
        self.angler_id = a_id
        self.angler_fio = a_fio
        self.angler_rank = a_rank
        self.angler_team = a_team
        self.flag_disqual = False
        self.flag_team = True if a_team is not None else False

    def get_angler_class_name(self):
        for k, v in globals().items():
            if v is self:
                return k

    def get_rank(self):
        return f'{"без разряда" if self.angler_rank is None else self.angler_rank}'

    def get_team(self):
        return f'{"личник" if self.angler_team is None else self.angler_team}'

    def get_flag_disqual(self):
        return f'{"дисквалифицирован" if self.flag_disqual else "не дисквалифицирован"}'

    def get_flag_team(self):
        return f'{"в команде" if self.flag_team else "не в команде"}'

    def get_all_info(self):
        return f'Объект {self.get_angler_class_name()}, id={self.angler_id}, ' \
               f'{str(self.angler_fio).center(8)}, {str(self.get_rank()).ljust(12)}, ' \
               f'{str(self.get_team()).ljust(12)}, ' \
               f'{self.get_flag_disqual()}, {self.get_flag_team()}'


# функция по созданию сорев, чисто утилитарная для хранения переменных в конкретных соревах
def create_tournament():
    tournament = Tournament(q_tur=1, q_period=4, q_zone=1, q_sector=None, d_period=45, q_anglers=8)
    print(tournament.get_tournament_info())


# функция по созданию рыбака на соревах
def create_anglers():
    # создание экземпляров рыбаков по количеству из table_anglers
    for angler_id, angler_fio in table_anglers.items():
        # создаётся название экземпляра
        string_angler_class = 'Angler'+str(angler_id)

        # создаётся экземпляр
        globals()[string_angler_class] = Angler(angler_id,
                                                angler_fio,
                                                a_rank=table_anglers_rank[angler_id],
                                                a_team=table_anglers_teams[angler_id]
                                                )
        print(f'{globals()["Angler"+str(angler_id)].get_all_info()}')


# функция для проверки входных данных на наличие только цифр
def only_numbers():
    pass


# функция считающая победителей в одном периоде
# на вход даётся таблица уловов и номер тура который нужно посчитать
# возвращать нужно сортированный список по убыванию уже с местами
# (место, ид участника, улов, количество очков за этот период)
def calc_tur(t_catches, n_tur):
    # список поимок в туре и id рыбака
    catches_tur = [[k, v[n_tur - 1]] for k, v in t_catches.items()]
    print(f'{catches_tur      = }')

    # сортировка списка по поимкам по уловам с уменьшением
    catches_tur_sort = sorted(catches_tur, key=lambda nud: (nud[1], nud[0]), reverse=True)
    print(f'{catches_tur_sort = }')

    # список только поимок в туре отсортированное с уменьшением
    catches = sorted((v[1] for v in catches_tur_sort), reverse=True)
    print(f'{catches          = }')

    # уникальные поимки в туре отсортированные с уменьшением
    unique_catches = sorted(list(set(v[1] for v in catches_tur_sort)), reverse=True)
    print(f'{unique_catches   = }')

    # итоговая таблица с очками и местами тура
    tur_result = catches_tur_sort[:]

    # алгоритм подсчёта мест и очков
    for catch in unique_catches:
        q_catch = catches.count(catch)
        # print(catch, q_catch)
        if q_catch == 1:
            # тут выдать данные и внести их в итоговую таблицу - id, catch, место, очки
            # print()

            # id = index
            a_index = catches.index(catch)
            # print(f'{a_index = }', end=', ')

            # улов
            # a_catch = catch
            # print(f'{a_catch = }', end=', ')

            # место
            a_place = unique_catches.index(catch) + 1
            # print(f'{a_place = }', end=', ')

            # очки
            a_score = unique_catches.index(catch) + 1
            # print(f'{a_score = }', end=', ')

            tur_result[a_index].append(a_place)
            tur_result[a_index].append(a_score)
        else:
            # тут посчитать очки, место при одинаковых поимках
            print()

            # id = index
            a_index = catches.index(catch)
            print(f'{a_index = }', end=', ')

            # улов
            a_catch = catch
            print(f'{a_catch = }', end=', ')

            # количество повторов улова
            print(f'{q_catch = }', end=', ')

            # место
            a_place = '?'
            print(f'{a_place = }', end=', ')

            # очки
            a_score = '?'
            print(f'{a_score = }', end=', ')

            tur_result[a_index].append(a_place)
            tur_result[a_index].append(a_score)

    print()
    print()
    print(f'{tur_result = }')

    return tur_result


if __name__ == '__main__':
    # print()
    # create_tournament()
    # print()
    # create_anglers()

    # for tur in range(1, len(table_catches[1])+1):
    for tur in range(0 + 1):
        print('*'*50)
        calc_tur(table_catches, tur)

# вспомогательные данные для расчётов консольной версии
# впоследствии это будет браться из базы ИЛИ формы GUI
# !!! главное чтобы в table_anglers И table_anglers_rank И table_anglers_teams ключи id совпадали
# таблица рыбаков с id и fio
table_anglers = {1: 'Иванов', 2: 'Петров', 3: 'Ветров', 4: 'Фролов',
                 5: 'Попков', 6: 'Котова', 7: 'Рыбова', 8: 'Локтев'}
# таблица рыбаков с id и разрядами
table_anglers_rank = {1: '1 разряд', 2: '2 разряд', 3: '3 разряд', 4: '1 разряд',
                      5: None, 6: 'МС', 7: 'КМС', 8: 'МС'}
# таблица рыбаков с id и командами
table_anglers_teams = {1: 'team1', 2: 'team1', 3: 'team2', 4: 'team3',
                       5: 'team2', 6: 'team3', 7: None, 8: None}
# таблица поимок в четырёх периодах
table_catches = {1: [1, 4, 7, 1], 2: [2, 52, 0, 2], 3: [43, 4, 5, 6], 4: [1, 0, 4, 22],
                 5: [8, 0, 12, 71], 6: [15, 18, 1, 0], 7: [0, 16, 13, 3], 8: [5, 17, 4, 4]}
table_tournament = ''


# класс Соревнование
class Tournament:
    def __init__(self, q_tur=1, q_period=4, q_zone=1, q_sector=None, d_period=45):
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

    def get_tournament_info(self):
        q_sector = 'нет' if self.quantity_sector is None else self.quantity_sector
        q_zone = 'нет' if self.quantity_zone is None else self.quantity_zone
        return f'В этих соревнованиях: туров {self.quantity_tur}, ' \
               f'периодов {self.quantity_period}, ' \
               f'зон {q_zone}, ' \
               f'секторов {q_sector}, ' \
               f'период длится {self.duration_period} минут'


# класс Рыбак
class Angler:
    def __init__(self, a_id, a_fio, a_rank=None, a_team=None):
        # TODO
        # тут сделать проверку входных данных, а только потом присвоить
        # id только число, фио только буквы, ранг и команда None если не заполнено
        self.angler_id = a_id
        self.angler_fio = a_fio
        self.angler_rank = a_rank
        self.angler_team = a_team

    def get_angler_class_name(self):
        for k, v in globals().items():
            if v is self:
                return k

    def get_rank(self):
        return f'{"без разряда" if self.angler_rank is None else self.angler_rank}'

    def get_team(self):
        return f'{"Личник" if self.angler_team is None else self.angler_team}'

    def get_all_info(self):
        return f'{self.get_angler_class_name()} . {self.angler_id} . {self.angler_fio} . {self.get_rank()} . {self.get_team()}'


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


def create_tournament():
    tournament = Tournament(q_tur=1, q_period=4, q_zone=1, q_sector=None, d_period=45)
    print(tournament.get_tournament_info())


if __name__ == '__main__':
    print()

    create_tournament()
    print()
    create_anglers()
    print()

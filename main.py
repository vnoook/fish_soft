# вспомогательные данные для расчётов консольной версии
# впоследствии это будет браться из базы ИЛИ формы GUI
# таблица рыбаков с id и fio
table_anglers = {1: 'Иванов', 2: 'Петров', 3: 'Ветров', 4: 'Фролов',
                 5: 'Попков', 6: 'Котова', 7: 'Рыбова', 8: 'Локтев'}
# таблица рыбаков с id и разрядами
table_anglers_rank = {1: '1 разряд', 2: '2 разряд', 3: '3 разряд', 4: '1 разряд',
                      5: 'б/р', 6: 'МС', 7: 'КМС', 8: 'МС'}
# таблица поимок в четырёх периодах
table_catches = {1: [1, 4, 7, 1], 2: [2, 52, 0, 2], 3: [43, 4, 5, 6], 4: [1, 0, 4, 22],
                 5: [8, 0, 12, 71], 6: [15, 18, 1, 0], 7: [0, 16, 13, 3], 8: [5, 17, 4, 4]}
table_tournament = ''


# класс Рыбак
class Angler:
    def __init__(self, a_id, a_fio, a_rank=None, a_team=None):
        self.angler_id = a_id
        self.angler_fio = a_fio
        self.angler_rank = a_rank
        self.angler_team = a_team

    def angler_info_all(self):
        a_team = 'Личник' if self.angler_team is None else self.angler_team
        print(f'{self.angler_id} . {self.angler_fio} . {self.angler_rank} . {a_team}')

    def angler_info_id(self):
        print(f'{self.angler_fio} = {self.angler_id}')

    def angler_info_fio(self):
        print(f'{self.angler_id} = {self.angler_fio}')

    def angler_info_rank(self):
        a_rank = 'нет данных' if self.angler_rank is None else self.angler_rank
        print(f'{self.angler_fio} = {self.angler_rank}')

    def angler_info_team(self):
        if self.angler_team is None:
            print(f'{self.angler_fio} не в команде, он Личник')
        else:
            print(f'{self.angler_fio} в команде {self.angler_team}')

    def get_angler_class_name(self):
        for k, v in globals().items():
            if v is self:
                return k

if __name__ == '__main__':
    print()

    a1 = Angler(1, 'fio1', 'rank1', 'team1')
    print(a1.get_angler_class_name())
    print(a1.angler_info_all())
    print()

    a2 = Angler(2, 'fio2', a_rank='rank2',)
    print(a2.get_angler_class_name())
    print(a2.angler_info_all())
    print()

    a3 = Angler(3, 'fio3', a_team='team3')
    print(a3.get_angler_class_name())
    print(a3.angler_info_all())
    print()

    a4 = Angler(4, 'fio4',)
    print(a4.get_angler_class_name())
    print(a4.angler_info_all())
    print()

    # # создание экземпляров рыбаков по количеству из table_anglers
    # for angler_id, angler_fio in table_anglers.items():
    #     # создаётся название экземпляра
    #     string_angler_class = 'Angler'+str(angler_id)
    #     # создаётся экземпляр
    #     globals()[string_angler_class] = Angler(angler_id, angler_fio)
    #     # print(f'{string_angler_class} ... {angler_fio} ... {table_anglers_rank[angler_id]}')
    #     print(globals()[string_angler_class].angler_info_all())

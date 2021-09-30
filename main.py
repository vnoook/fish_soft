# вспомогательные данные для расчётов консольной версии
# таблица рыбаков с id и fio
table_anglers = {1:'Иванов', 2:'Петров', 3:'Сидоров', 4:'Фролов', 5:'Попов', 6:'Котов', 7:'Рыбов', 8:'Лотов'}
# таблица рыбаков с id и разрядами
table_anglers_rank = {1:'1 разряд', 2:'2 разряд', 3:'3 разряд', 4:'1 разряд', 5:'3 разряд', 6:'МС', 7:'КМС', 8:'МС'}
# таблица поимок в четырёх периодах
table_catches = {1:[1,4,7,1], 2:[2,52,2,2], 3:[43,4,5,6], 4:[1,0,4,22], 5:[8,0,12,71], 6:[15,18,1,0], 7:[0,16,13,3], 8:[5,17,4,4]}
table_tournament = ''

# класс Рыболов
class Angler:
    def __init__(self, id, fio, rank, team=None):
        self.angler_id = id
        self.angler_fio = fio
        self.angler_rank = rank
        self.angler_team = team
    def angler_info(self):
        print(f'{self.angler_id} ... {self.angler_fio}')

if __name__ == '__main__':
    print()

    # создание экземпляров рыболовов по количеству в table_anglers
    for angler in table_anglers:
        pass

    print()

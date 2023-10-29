import fish_consts as fc
from collections import namedtuple

list1 = {'apple': 1, 'orange': 2, 'lemon': 3}
box = namedtuple('fruits', list1)
fruit = box(2, 5, 7)
print(f'{box = }')
print(f'{box.apple = }')
box.apple = 11
print(f'{box.apple = }')

# print(f'{fruit = }')
# print(f'{fruit.apple = }')


dict1 = fc.SETT_DEF_SOFT
SETTINGS_DATA_DEF = namedtuple('settings', dict1)
# print(SETTINGS_DATA_DEF)
# print(SETTINGS_DATA_DEF._fields)
# print(SETTINGS_DATA_DEF.competition_action)

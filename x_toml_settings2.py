from pprint import pprint as pp
dict_def = {'set1':1,
            'set2':2,
            'set3':{'set31': {'set311':311, 'set312':312}, 'set32':32}}
dict_cur = {'set1':11,
            'set2':'22',
            'set3':{'set31':'311', 'set32':322},
            'set4':4,
            'set5':{'set51':51, 'set52':52}}
def rep_dict(dict_cur, dict_def):
    for key, val in dict_def.items():
        if not dict_cur.get(key, False):
            dict_cur[key] = dict_def[key]
        else:
            if type(val) != type(dict_cur[key]):
                dict_cur[key] = val
        if isinstance(val, dict):
            rep_dict(dict_cur[key], val)
    list_keys = []
    for key in dict_cur:
        if key not in dict_def:
            list_keys.append(key)
    for key in list_keys:
        del dict_cur[key]
    return dict_cur

rep_dict(dict_cur, dict_def)
# print(dict_def)
# print()
pp(dict_cur)
# print(dict_cur)
# print()

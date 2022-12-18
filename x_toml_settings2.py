dict_def = {'set1':1,
            'set2':2,
            'set3':{'set31':31,
                    'set32':32}}

dict_cur = {'set1':1,
            'set2':22,
            'set3':{'set31':311,
                    'set32':32},
            'set4':4,
            'set5':{'set51':51,
                    'set52':52}
            }

def rep_dict(dict_cur, dict_def):
    for key, val in dict_def.items():
        print(dict_cur.get(key))

#    for key, val in dict_def.items():
#        if isinstance(val, dict):
#            print(key, val)

print(dict_def)
print()
print(dict_cur)
print()
print()
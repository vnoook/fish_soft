import tomli_w
import tomllib
import pprint

setts = {'settings_window_main': {'window_coords': {'h': 1100,
                                                    'w': 400,
                                                    'x': 100,
                                                    'y': 100},
                                  'window_name': {'file': 'file1.py',
                                                  'icon': 'icon1.ico',
                                                  'name': 'main window'}},
         'settings_window_set_comp': {'window_coords': {'h': 400,
                                                        'w': 400,
                                                        'x': 100,
                                                        'y': 100},
                                      'window_name': {'file': 'file1.py',
                                                      'icon': 'icon2.ico',
                                                      'name': 'settings window '
                                                              'competition'}},
         'settings_window_set_soft': {'window_coords': {'h': 400,
                                                        'w': 400,
                                                        'x': 100,
                                                        'y': 100},
                                      'window_name': {'file': 'file1.py',
                                                      'icon': 'icon3.ico',
                                                      'name': 'settings window '
                                                              'software'}}}

with open("conf.toml", "wb") as fl_set:
    tomli_w.dump(setts, fl_set)

with open("conf.toml", "rb") as fl_set:
    data = tomllib.load(fl_set)

dt = data["settings_window_set_comp"]["window_name"]["name"]

pprint.pprint(dt)

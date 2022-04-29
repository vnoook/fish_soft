def get_list_fields_and_coords(start_x, start_y, shift_x, shift_y, field_h, q_sportmen):
    """Универсальная функция для описания полей и расчёта их координат на форме"""
    # список всех полей и их координаты
    list_coodr_of_fields = []

    # точка начала отчёта
    start_dot_x = start_x
    start_dot_y = start_y

    # расстояние между объектами на форме
    gap_x = shift_x
    gap_y = shift_y

    # высота для всех полей
    field_height = field_h

    # кортеж из полей на форме "Название поля", длина
    fields = (('Sportik01_number_', 40),
              ('Sportik02_lottery_', 40),
              ('Sportik03_fio_', 180),
              ('Sportik04_team_', 180),
              ('Sportik05_rank_', 40),
              ('Sportik06_zona1_', 70),
              ('Sportik07_zona2_', 70),
              ('Sportik08_period1_', 40),
              ('Sportik09_period2_', 40),
              ('Sportik10_period3_', 40),
              ('Sportik11_period4_', 40),
              ('Sportik12_points_', 40),
              ('Sportik13_team_place_', 40),
              ('Sportik14_self_place_', 40)
    )

    # количество спортиков
    q_sportiks = q_sportmen

    # шаг по вертикали
    field_step_y = start_dot_y

    # цикл расчёта координат каждого поля
    for sportik in range(1, q_sportiks + 1):
        # шаг вправо начинается с первой точки и идёт вправо
        field_step_x = start_dot_x
        # список координат в строке
        list_coodr_of_field = []

        # проход по строке полей
        for field in fields:
            # формирование имени спортика
            field_name = field[0] + str(sportik)
            # выбор ширины поля
            field_width = field[1]

            # добавление в список координат
            list_coodr_of_field.append(field_name)
            list_coodr_of_field.append(field_step_x)
            list_coodr_of_field.append(field_step_y)

            # увеличение шага вправо на ширину поля
            field_step_x = field_step_x + field_width

            # увеличение шага вправо на ширину промежутка между полями
            field_step_x = field_step_x + gap_x

        # добавление шага вниз на промежуток между строками полей
        field_step_y = field_step_y + field_height + gap_y

        # добавление в главный список списка строки полей
        list_coodr_of_fields.append(list_coodr_of_field)

    return list_coodr_of_fields


if __name__ == '__main__':
    print()
    lst1 = get_list_fields_and_coords(5, 100, 20, 10, 20, 3)
    print(*lst1, sep='\n')

def get_list_coodr_of_fields(start_x, start_y, shift_x, shift_y, field_h, q_sportmen):
    # список всех полей и их координаты
    list_coodr_of_fields = []
    list_coodr_of_field = []

    # точка начала отчёта
    start_dot_x = start_x
    start_dot_y = start_y

    # растояние между объектами на форме
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

    for sportik in range(1, q_sportiks+1):
        field_step_x = start_dot_x
        list_coodr_of_field = []
        for field in fields:
            field_name = field[0] + str(sportik)
            field_width = field[1]

            # print(f'[{field_step_x},{field_step_y}] {field_name} ({field_width} {field_height})', end=' ')
            list_coodr_of_field.append(field_name)
            list_coodr_of_field.append(field_step_x)
            list_coodr_of_field.append(field_step_y)

            field_step_x = field_step_x + field_width
            # print(f'<{field_step_x},{field_step_y}>', end=' ... ')

            field_step_x = field_step_x + gap_x
            # print(f'{gap_x}', end=' ... ')

        # print(f'{field_step_x}', end='')

        field_step_y = field_step_y + field_height + gap_y

        list_coodr_of_fields.append(list_coodr_of_field)

        # print()
    return list_coodr_of_fields

print()
print(*get_list_coodr_of_fields(5, 100, 20, 10, 20, 4), sep='\n')

# функция считающая победителей в одном периоде
# на вход даётся таблица уловов и номер тура который нужно посчитать
# возвращать нужно сортированный список по убыванию уже с местами
# (место, ид участника, улов, количество очков за этот период)
def calc_period(p_catches: dict, n_period: int) -> list:
    # список id рыбаков с уловами в конкретном n_period туре
    catches_period = [[k, v[n_period - 1]] for k, v in p_catches.items()]

    # сортировка списка рыбаков по уловам с уменьшением
    catches_period_sort = sorted(catches_period, key=lambda nud: nud[1], reverse=True)

    # список только поимок в туре отсортированное с уменьшением
    catches = sorted((v[1] for v in catches_period_sort), reverse=True)

    # итоговая таблица с очками и местами тура
    # копирование отсортированной таблицы
    period_result = catches_period_sort[:]

    # переменная для сохранения предыдущего улова для
    prev_catch = None
    # переменная для хранения первого улова за которым пойдут повторяющиеся уловы, нужна для подсчёта очков
    first_repeat_catch = None
    # индекс улова
    catch_index = -1

    # алгоритм подсчёта мест и очков
    # иду по отсортированным уловам, смотрю их индекс и повтор уловов
    for catch in catches:
        # количество повторов уловов
        q_catch = catches.count(catch)
        # увеличение индекса
        catch_index += 1

        # место
        angler_place = catch_index + 1

        # очки
        # если текущий улов не равен предыдущему, то значит это первый элемент за которым пойдут повторные
        if catch != prev_catch:
            first_repeat_catch = catches.index(catch) + 1

        if q_catch == 1:  # ситуация когда повтора улова нет
            angler_score = calc_scores(angler_place, q_catch)
        else:  # ситуация когда повтор улова есть
            angler_score = calc_scores(first_repeat_catch, q_catch)

        # запоминание предыдущего улова
        prev_catch = catch

        # добавление места и очков в итоговую таблицу
        period_result[catch_index].append(angler_place)
        period_result[catch_index].append(angler_score)

    # формат вывода список из списков - ид спортика, улов в периоде, место, очки за улов
    return period_result


# функция подсчёта очков с известными - начальное место одинаковых уловов, количество одинаковых уловов
def calc_scores(index_start, index_quantity):
    scores = 0
    for x_q in range(index_start, index_start + index_quantity):
        scores = scores + x_q / index_quantity
    return scores

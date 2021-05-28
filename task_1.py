"""
Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import deque

num_of_enterprises = int(input('Укажите кол-во предприятий:'))
dct = {}

profit_all = 0

for i in range(num_of_enterprises):
    name = input(f'Введите название предприятия:')
    dct[name] = deque()
    dct[name].append({'profit_for_the_year': 0})

    for k in range(1, 5):
        q = float(input(f'Укажите прибыль за {k} квартал для "{name}": '))
        dct[name].append(q)
        dct[name][0]['profit_for_the_year'] += q
    else:
        profit_all += dct[name][0]['profit_for_the_year']

average = round(profit_all / num_of_enterprises, 2)
more = ''
less = ''

for key, val in dct.items():
    if val[0]['profit_for_the_year'] > average:
        more += f'"{key}" '
    else:
        less += f'"{key}" '
else:
    print(f'Средняя прибыль всех предприятий = {average}\n'
          f'Предприятия чья приыбыль выше средней {more}\n'
          f'Предприятия чья приыбыль ниже средней {less}')

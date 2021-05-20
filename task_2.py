"""
Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
второй массив надо заполнить значениями 0, 3, 4, 5, (индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""
import random

size = 7
min_item = -100
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(size)]

array_ind = [index for index in range(len(array)) if array[index] & 1 == 0]

print(array)
if len(array_ind) == 0:
    print('Все числа массива нечетные.')
else:
    print(f'{array_ind} индексы четных элементов массива')

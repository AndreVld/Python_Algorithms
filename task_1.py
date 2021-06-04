"""
Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
"""
import random

size = 10
min_item = -100
max_item = 100

array = [random.randint(min_item, max_item - 1) for _ in range(size)]


def bubble(data):
    _sorted = False
    for i in range(1, len(data)):
        if _sorted:
            break
        _sorted = True
        for j in range(len(data) - i):
            if data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                _sorted = False
    return data


print(f'Исходный массив {array}')
print(f'Отсортированный {bubble(array)}')

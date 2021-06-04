"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы.
"""

from random import random

size = 10
max_item = 50

array = [round(random() * max_item, 2) for _ in range(size)]


def merge(data):
    if len(data) < 2:
        return data

    mid = len(data) // 2

    left_list = merge(data[:mid])
    right_list = merge(data[mid:])

    result = []

    left = right = 0
    while left < len(left_list) and right < len(right_list):

        if left_list[left] < right_list[right]:
            result.append(left_list[left])
            left += 1

        else:
            result.append(right_list[right])
            right += 1

    while left < len(left_list):
        result.append(left_list[left])
        left += 1

    while right < len(right_list):
        result.append(right_list[right])
        right += 1

    return result


print(f'Исходный массив {array}')
print(f'Отсортированный {merge(array)}')

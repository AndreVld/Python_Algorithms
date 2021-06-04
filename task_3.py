"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""

import random

m = 4
size = 2 * m + 1
min_item = 0
max_item = 100

array = [random.randint(min_item, max_item - 1) for _ in range(size)]


def median(arr):
    mid = len(arr) // 2

    for i in range(len(arr)):
        left = 0
        right = 0

        for j in range(len(arr)):
            if arr[i] == arr[j]:
                continue

            elif arr[j] < arr[i]:
                left += 1

            else:
                right += 1

        if left <= mid and right <= mid:
            return arr[i]


print(f'Исходный массив {array}')
print(f'Медиана {median(array)}')


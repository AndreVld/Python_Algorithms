"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

size = 5
min_item = 1
max_item = 100

array = [random.randint(min_item, max_item) for _ in range(size)]
print(array)

ind_max = 0
ind_min = 0
for i in range(1, len(array)):
    if array[i] > array[ind_max]:
        ind_max = i
    if array[i] < array[ind_min]:
        ind_min = i

array[ind_max], array[ind_min] = array[ind_min], array[ind_max]

print(array)


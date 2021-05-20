"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

size = 12
min_item = -20
max_item = 50

array = [random.randint(min_item, max_item) for _ in range(size)]
print(array)

index = None
for i in range(len(array)):
    if array[i] < 0 and index is None:
        index = i
    elif array[i] < 0 and (array[i] > array[index]):
        index = i

if index is None:
    print('Все числа в массива положительные')
else:
    print(f'Максимальный отрицательный элемент массива {array[index]}'
          f' находится под индексом {index}')

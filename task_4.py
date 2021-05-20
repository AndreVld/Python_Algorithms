"""
Определить, какое число в массиве встречается чаще всего.
"""
import random

size = 17
min_item = 1
max_item = 50

array = [random.randint(min_item, max_item) for _ in range(size)]
print(array)

num = array[0]
amount_of_num = 1

for i in range(len(array) - 1):
    amount = 1
    for k in range(i + 1, len(array)):
        if array[i] == array[k]:
            amount += 1
    if amount_of_num < amount:
        amount_of_num = amount
        num = array[i]

result = f'В массиве чаще всего встречается число {num}'
if amount_of_num == 1:
    result = 'В массиве все числа уникальны'
print(result)

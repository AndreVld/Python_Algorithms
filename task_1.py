"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""

start_num = 2
end_num = 99
start_of_range = 2
end_of_range = 9

my_dict = {i: i * 0 for i in range(start_of_range, end_of_range + 1)}

for num in range(start_num, end_num + 1):
    for key in my_dict:
        if num % key == 0:
            my_dict[key] += 1

for key, value in my_dict.items():
    print(f'{key} - {value}')

print('Можно же просто поделить')

new_dict = {i: end_num // i for i in range(start_of_range, end_of_range + 1)}
for key, value in new_dict.items():
    print(f'{key} - {value}')



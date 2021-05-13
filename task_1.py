"""
https://drive.google.com/file/d/180J2Dl54N9VeudWX0ClV1oudXSLbdKMB/view?usp=sharing

Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

num = int(input('Введите любое число от 100 до 999 : '))

digit_1 = num // 100
digit_2 = num // 10 % 10
digit_3 = num % 10

s = digit_1 + digit_2 + digit_3
p = digit_1 * digit_2 * digit_3

print(f'Сумма всех цифр числа {num} = {s} \n'
      f'Произведение всех цифр числа {num} = {p}')

"""
Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
"""


def func(n):
    if n <= 1:
        return n
    else:
        return n + func(n - 1)


num = int(input('Введите натуратьное число :'))

print(func(num) == num * (num + 1) / 2)

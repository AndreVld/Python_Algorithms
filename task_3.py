"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
"""


def func(x, y=1):
    if x == 1:
        return y
    else:
        return y + func(x - 1, y / (-2))


n = int(input('Укажите количество элементов в последовательности : '))

print(func(n))

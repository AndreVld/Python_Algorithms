"""
https://drive.google.com/file/d/1KizXHgQtao8FKg8mJ8kHXFakNzMo7rXR/view?usp=sharing

Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def func(num, even=0, odd=0):
    if num == 0:
        return f'четных цифр {even}, нечетных цифр {odd}'
    else:
        if num & 1 == 0:
            even += 1
        else:
            odd += 1
        return func(num // 10, even, odd)


n = int(input('Введите натуральное число: '))

print(f'В числе {n} {func(n)}')

"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque


def sum_hex(first, second):
    first = deque(first)
    second = deque(second)

    list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
    len_first = len(first)
    len_second = len(second)

    # if len_first > len_second:
    #     first, second = second, first

    _sum = deque()
    k = 0
    for i in range(len_second):
        one = list_of_numbers.index(second.pop())

        if len(first):
            two = list_of_numbers.index(first.pop())
        else:
            two = k
        _sum.appendleft(list_of_numbers[(one + two + k) % 16])

        if (one + two) > 16:
            k = 1
        else:
            k = 0
    else:
        if k:
            _sum.appendleft('1')
    return list(_sum)


# print(sum_hex('A2', 'C4F'))


def multi_hex(first, second):
    deq = deque([deque() for _ in range(len(second))])
    result = deque()
    list_of_numbers = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']

    second = deque(second)
    for i in range(len(second)):
        m = list_of_numbers.index(second.pop())

        for j in first[::-1]:
            deq[i].appendleft(m * list_of_numbers.index(j))

        for _ in range(i):
            deq[i].append(0)

    num_1 = 0

    for _ in range(len(deq[-1])):
        num2 = num_1

        for i in deq:
            if i:
                num2 += i.pop()

        if num2 < 16:
            result.appendleft(list_of_numbers[num2])

        else:
            result.appendleft(list_of_numbers[num2 % 16])
            num_1 = num2 // 16
    else:
        if num_1 != 0:
            result.appendleft(list_of_numbers[num_1])
    return list(result)


# print(multi_hex('A2', 'C4F'))

print('Введите два числа в шестнадцатеричной системе ')
a = input('1 = ').upper()
b = input('2 = ').upper()

print(f'Сумма = {sum_hex(a, b)}\n'
      f'Произведение = {multi_hex(a, b)}')

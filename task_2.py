"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.

Второй — без использования «Решета Эратосфена».
"""

from timeit import timeit
from cProfile import run
from math import log

'''
С помощью алгоритма «Решето Эратосфена».
'''


def prime_er(n):
    if n == 1:
        return 2
    numbers = [i for i in range(int(round(log(n) * 2 * n)))]
    numbers[1] = 0
    p_list = [0 for _ in range(n)]
    m = 0
    l = len(numbers)
    for i in numbers:
        if i != 0 and m < n:
            p_list[m] = i
            m += 1
            for j in range(i, l, i):
                numbers[j] = 0
    return p_list[n - 1]


print(timeit('prime_er(10)', number=1000, globals=globals()))  # 0.0057391000000000005
print(timeit('prime_er(15)', number=1000, globals=globals()))  # 0.009179199999999998
print(timeit('prime_er(20)', number=1000, globals=globals()))  # 0.013097199999999996
print(timeit('prime_er(25)', number=1000, globals=globals()))  # 0.0169761
print(timeit('prime_er(30)', number=1000, globals=globals()))  # 0.0210804
print(timeit('prime_er(35)', number=1000, globals=globals()))  # 0.025366600000000003
print(timeit('prime_er(40)', number=1000, globals=globals()))  # 0.030532599999999993
print(timeit('prime_er(45)', number=1000, globals=globals()))  # 0.03619800000000001
print(timeit('prime_er(50)', number=1000, globals=globals()))  # 0.04646460000000002
print(timeit('prime_er(55)', number=1000, globals=globals()))  # 0.05027479999999998
print(timeit('prime_er(60)', number=1000, globals=globals()))  # 0.05481620000000004
print(timeit('prime_er(65)', number=1000, globals=globals()))  # 0.06085639999999998
print(timeit('prime_er(70)', number=1000, globals=globals()))  # 0.06616309999999997
print(timeit('prime_er(75)', number=1000, globals=globals()))  # 0.07964900000000003
print(timeit('prime_er(80)', number=1000, globals=globals()))  # 0.08083649999999998
print(timeit('prime_er(85)', number=1000, globals=globals()))  # 0.08324560000000003
print(timeit('prime_er(90)', number=1000, globals=globals()))  # 0.09714499999999993
print(timeit('prime_er(95)', number=1000, globals=globals()))  # 0.0960742
print(timeit('prime_er(100)', number=1000, globals=globals()))  # 0.1017016
print(timeit('prime_er(1000)', number=1000, globals=globals()))  # 1.6333609
print(timeit('prime_er(10000)', number=1000, globals=globals()))  # 28.4169632
print(timeit('prime_er(100000)', number=1000, globals=globals()))  # 490.69125809999997

# run('prime_er(1_000_000)')

#       9 function calls in 6.871 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.177    0.177    6.871    6.871 <string>:1(<module>)
#      1    5.733    5.733    6.694    6.694 task_5.py:22(prime_er)
#      1    0.928    0.928    0.928    0.928 task_5.py:25(<listcomp>)
#      1    0.033    0.033    0.033    0.033 task_5.py:27(<listcomp>)
#      1    0.000    0.000    6.871    6.871 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.round}
#      1    0.000    0.000    0.000    0.000 {built-in method math.log}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

'''
Без использования «Решета Эратосфена».
'''


def prime_num(ind):
    if ind == 1:
        return 2
    prime = [2]
    num = 3
    while True:
        for i in prime:
            if num % i == 0:
                break
        else:
            prime.append(num)

        num += 2

        if len(prime) == ind:
            return prime[ind - 1]


print(timeit('prime_num(10)', number=1000, globals=globals()))  # 0.0032223999999999586
print(timeit('prime_num(15)', number=1000, globals=globals()))  # 0.006156399999999951
print(timeit('prime_num(20)', number=1000, globals=globals()))  # 0.009637200000000012
print(timeit('prime_num(25)', number=1000, globals=globals()))  # 0.01482490000000003
print(timeit('prime_num(30)', number=1000, globals=globals()))  # 0.019817699999999938
print(timeit('prime_num(35)', number=1000, globals=globals()))  # 0.025813099999999922
print(timeit('prime_num(40)', number=1000, globals=globals()))  # 0.03189940000000013
print(timeit('prime_num(45)', number=1000, globals=globals()))  # 0.03838089999999994
print(timeit('prime_num(50)', number=1000, globals=globals()))  # 0.04891639999999997
print(timeit('prime_num(55)', number=1000, globals=globals()))  # 0.05721419999999999
print(timeit('prime_num(60)', number=1000, globals=globals()))  # 0.06397900000000001
print(timeit('prime_num(65)', number=1000, globals=globals()))  # 0.07371740000000004
print(timeit('prime_num(70)', number=1000, globals=globals()))  # 0.08567919999999996
print(timeit('prime_num(75)', number=1000, globals=globals()))  # 0.09628160000000019
print(timeit('prime_num(80)', number=1000, globals=globals()))  # 0.10978929999999987
print(timeit('prime_num(85)', number=1000, globals=globals()))  # 0.12862909999999994
print(timeit('prime_num(90)', number=1000, globals=globals()))  # 0.1333705999999999
print(timeit('prime_num(95)', number=1000, globals=globals()))  # 0.14724590000000015
print(timeit('prime_num(100)', number=1000, globals=globals()))  # 0.16505850000000022
print(timeit('prime_num(1000)', number=1000, globals=globals()))  # 15.742261100000064
print(timeit('prime_num(10000)', number=1000, globals=globals()))  # 1691.5782320000003

run('prime_num(100_000)')

#       749864 function calls in 172.916 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001  172.915  172.915 <string>:1(<module>)
#      1  172.862  172.862  172.915  172.915 task_5.py:68(prime_num)
#      1    0.000    0.000  172.916  172.916 {built-in method builtins.exec}
# 649860    0.042    0.000    0.042    0.000 {built-in method builtins.len}
# 100000    0.011    0.000    0.011    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



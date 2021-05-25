"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.

"""

from cProfile import run
from timeit import timeit
import random

size = 10
N = []
for i in range(4):
    N.append([random.randint(-100_000, 100_000) for _ in range(size)])
    size *= 10

for_run = [random.randint(-100_000, 100_000) for _ in range(100_000_000)]


def func(arr):
    index = None
    for i in range(len(arr)):
        if arr[i] < 0 and index is None:
            index = i
        elif arr[i] < 0 and (arr[i] > arr[index]):
            index = i
    return arr[index], index


for n in range(len(N)):
    print(timeit('func(N[n])', number=1000, globals=globals()), f'N = {len(N[n])}')
# 0.0008674000000000008 N = 10
# 0.001435800000000001  N = 20
# 0.002012400000000001  N = 30
# 0.002715000000000002  N = 40
# 0.0036856000000000007 N = 50
# 0.003977100000000001  N = 60
# 0.0051333             N = 70
# 0.0058099             N = 80
# 0.005741499999999997  N = 90
# 0.00733269999999997   N = 100
# 0.0128745             N = 200
# 0.019797500000000003  N = 300
# 0.0555161             N = 400
# 0.0846109             N = 500
# 0.08914549999999999   N = 600
# 0.0437612             N = 700
# 0.05605070000000001   N = 800
# 0.06415490000000001   N = 900
# 0.07632439999999996   N = 1000
# 0.7318214             N = 10000
# 7.1960783             N = 100000
# 83.28615470000001     N = 1000000


run('func(for_run)')  # N = 100_000_000


#       5 function calls in 8.168 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    8.168    8.168 <string>:1(<module>)
#      1    8.168    8.168    8.168    8.168 task_1.py:20(func)
#      1    0.000    0.000    8.168    8.168 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def func2(arr):
    for i in arr:
        if i < 0:
            ind = arr.index(i)
            el = i
            for k in range(ind + 1, len(arr)):
                if arr[k] < 0 and (arr[k] > arr[ind]):
                    ind = k
                    el = arr[k]
            else:
                return el, ind
    else:
        return None


for n in range(len(N)):
    print(timeit('func2(N[n])', number=1000, globals=globals()), f'N = {len(N[n])}')

# 0.0006796999999999984 N = 10
# 0.0010222000000000009  N = 20
# 0.0013516999999999973  N = 30
# 0.0018943999999999975  N = 40
# 0.0025077000000000016  N = 50
# 0.002734200000000006   N = 60
# 0.002997899999999998   N = 70
# 0.0035340000000000094  N = 80
# 0.0038780999999999954  N = 90
# 0.004278099999999993   N = 100
# 0.008976800000000007   N = 200
# 0.012109200000000042   N = 300
# 0.017384999999999984   N = 400
# 0.023198200000000058   N = 500
# 0.026595999999999953   N = 600
# 0.029530399999999957   N = 700
# 0.03645860000000001    N = 800
# 0.040018600000000015   N = 900
# 0.04320300000000543    N = 1000
# 0.44467109999999366    N = 10000
# 4.434508600000001      N = 100000
# 55.08326760000001      N = 1000000


run('func2(for_run)')  # N = 100_000_000

#       6 function calls in 5.489 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    5.489    5.489 <string>:1(<module>)
#      1    5.489    5.489    5.489    5.489 task_1.py:71(func2)
#      1    0.000    0.000    5.489    5.489 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}


def func3(arr):
    a = []
    for i in arr:
        if i < 0:
            a.append(i)
    m = max(a)
    ind = arr.index(m)
    return m, ind


for n in range(len(N)):
    print(timeit('func3(N[n])', number=1000, globals=globals()), f'N = {len(N[n])}')

# 0.0006203000000000042  N = 10
# 0.0010003999999999985  N = 20
# 0.0012347999999999942  N = 30
# 0.001901               N = 40
# 0.002576800000000004   N = 50
# 0.002702800000000005   N = 60
# 0.0026341000000000003  N = 70
# 0.003089599999999998   N = 80
# 0.003697699999999998   N = 90
# 0.00372119999999998    N = 100
# 0.008080899999999946   N = 200
# 0.012478800000000012   N = 300
# 0.014926299999999948   N = 400
# 0.019553399999999943   N = 500
# 0.025083899999999937   N = 600
# 0.028778199999999976   N = 700
# 0.029024300000000003   N = 800
# 0.0393                 N = 900
# 0.03775799999999996    N = 1000
# 0.5047486000000276     N = 10000
# 4.528820499999995      N = 100000
# 46.1521511             N = 1000000


run('func3(for_run)')  # N = 100_000_000

# 50008522 function calls in 11.076 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.209    0.209   11.076   11.076 <string>:1(<module>)
#         1    6.951    6.951   10.866   10.866 task_1.py:129(func3)
#         1    0.000    0.000   11.076   11.076 {built-in method builtins.exec}
#         1    0.452    0.452    0.452    0.452 {built-in method builtins.max}
#  50008516    3.462    0.000    3.462    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         1    0.001    0.001    0.001    0.001 {method 'index' of 'list' objects}



"""
Выводы :  
Во всех трех функциях сложность линейная О(n). 

В третьей функции использовался метод append() и функция max() функция отработала медленнее
двух предыдущих с массивом длинной в 100_000_000 чисел, но с меньшими массивами работала быстрее двух других.

Второй алгоритм использует два цикла для для одного прохода по массиву(первый обрывается на первом отрицательном числе,
а второй стартует со следующего числа идущего после первого отрицательного  ),но на удивление 
работает быстрее первого.(Вероятно из-за того что во втором выполняется меньше сравнений)

"""

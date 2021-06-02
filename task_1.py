"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

"""

from sys import getsizeof, version


# print(version)


def show_size(obj):
    size = getsizeof(obj)
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                size += show_size(key)
                size += show_size(value)
        elif not isinstance(obj, str):
            for item in obj:
                size += show_size(item)

    return size


def sum_memory(*args):
    sum_m = 0
    for el in args:
        sum_m += show_size(el)

    return f'Переменные в сумме заняли {sum_m} байт'


"""
В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию в массиве.
"""
array = [56, -234, 7665, 234, 6787, -34, 123, 678, 4353, -5, 234, 5, 3, -1, 453, 235, -6576, -23, 456, 876, -34]


def max_below_zero_ver1(arr):
    index = None
    for i in range(len(arr)):
        if arr[i] < 0 and index is None:
            index = i
        elif arr[i] < 0 and (arr[i] > arr[index]):
            index = i

    print('max_below_zero_ver1 ', sum_memory(arr, index, i))

    return arr[index], index


max_below_zero_ver1(array)


def max_below_zero_ver2(arr):
    for i in arr:
        if i < 0:
            ind = arr.index(i)
            el = i
            for k in range(ind + 1, len(arr)):
                if arr[k] < 0 and (arr[k] > arr[ind]):
                    ind = k
                    el = arr[k]
            else:
                print('max_below_zero_ver2 ', sum_memory(arr, i, ind, el, k))
                return el, ind
    else:
        return None


max_below_zero_ver2(array)


def max_below_zero_ver3(arr):
    a = []
    for i in arr:
        if i < 0:
            a.append(i)
    m = max(a)
    ind = arr.index(m)

    print('max_below_zero_ver3 ', sum_memory(arr, a, i, m, ind))

    return m, ind


max_below_zero_ver3(array)
print()




def max_below_zero_ver1_tuple(arr):
    arr = tuple(arr)
    index = None
    for i in range(len(arr)):
        if arr[i] < 0 and index is None:
            index = i
        elif arr[i] < 0 and (arr[i] > arr[index]):
            index = i

    print('max_below_zero_ver1_tuple ', sum_memory(arr, index, i))

    return arr[index], index


max_below_zero_ver1_tuple(array)

"""
OС: Win 10 Верися 2004
разрядность: 64 bit
Python 3.9.2

max_below_zero_ver1  Переменные в сумме заняли 892 байт
max_below_zero_ver2  Переменные в сумме заняли 948 байт
max_below_zero_ver3  Переменные в сумме заняли 1236 байт

max_below_zero_ver1_tuple  Переменные в сумме заняли 852 байт

По расходу памяти оптимальный вариант - max_below_zero_ver1_tuple 
Т.к используется меньшее кол-во переменных, и тип tuple не использует доп. память для указателей на 
зарезервированные ячейки в отличии от типа list в max_below_zero_ver1
"""

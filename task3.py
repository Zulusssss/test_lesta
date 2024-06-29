# Чаще всего использовать надо sorted(). У неё O(n*log(n)) временная сложность и в среднем, и в худшем случае.
# А если массив отсортирован, то O(n). Порядок, как в изначальном массиве, для элементов одинаковых тоже сохраняется.
# Но может выделять много памяти.

import random

def func_1(arr, n, i):
    larg_max = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        larg_max = left

    if right < n and arr[larg_max] < arr[right]:
        larg_max = right

    if larg_max != i:
        arr[i], arr[larg_max] = arr[larg_max], arr[i]
        func_1(arr, n, larg_max)


def func(arr):
    '''
    Это сортировка с кучей. И в худшем, и в лучшем, и в среднем случае временная сложность O(n*log(n)).
    И она не требует дополнительной памяти.
    Но порядок одинаковых элементов изначального массива не сохраняется.
    '''
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        func_1(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        func_1(arr, i, 0)

    return arr

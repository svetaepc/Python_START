"""
Задайте список случайных чисел. Выведите список чисел, которые не повторяются в заданном списке.
Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>
Пример:
[1, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7, 8, 9, 9]
[2, 4, 6, 8]
"""

from random import randint

def create_list(size, m, n):
    return [randint(m, n) for i in range(size)]

def get_unic_value(list):
    return [i for i in set(list)]

size = 10
m = 1
n = 10

origin = create_list(size, m, n)
print(origin)
print(get_unic_value(origin))

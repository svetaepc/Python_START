"""
Задайте список целых чисел. Верните список с произведениями его парных элементов.
Парой считаются первый и последний элемент, второй и предпоследний и т.д.
Если элементов нечетное количество – центральный элемент умножается сам на себя.
Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <list>
Пример:
[2, 3, 4, 5, 6]
[12, 15, 16]
[2, 3, 5, 6]
[12, 15]

autopep8 ON
"""
from random import randint

n = 9
first = 1
last = 10
[randint(first, last) for i in range(n)]

mylist = [randint(first, last) for i in range(n)]

print(mylist)


def pairs_mult(numbers):
    results = []
    while len(numbers) > 1:
        results.append(numbers[0] * numbers[-1])
        del numbers[0]
        del numbers[-1]
    if len(numbers) == 1: results.append(numbers[0] ** 2)
    return results


print(pairs_mult(mylist))

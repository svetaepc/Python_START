"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.
Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>
Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0

autopep8 ON
"""

from random import uniform

n = 5
first = 1
last = 10
mylist = [round(uniform(first, last), 2) for i in range(n)]


def find_diff(nums_in):
    nums = [round(x - int(x), 2) for x in (nums_in)]
    return max(nums) - min(nums)


mynums = [round(uniform(first, last), 2) for i in range(n)]

print(mynums)
print(find_diff(mynums))

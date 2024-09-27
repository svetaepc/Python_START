"""
Задайте список целых чисел. Найдите сумму элементов списка, имеющих нечетные индексы.
Ввод: значение типа <list> (либо значение типа <int> – размерность списка)
Вывод: значение типа <int>
Примеры:
[2, 3, 5, 9, 3]
12
[5, 1, 5, 2, 7, 11]
14

autopep8 ON
"""

from random import randint

n = 9
first = 1
last = 10
[randint(first, last) for i in range(n)]

mylist = [randint(first, last) for i in range(n)]

print(mylist)

print(sum(mylist[1::2]))

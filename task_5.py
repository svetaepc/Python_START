"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи
Ввод: значение типа <int>
Вывод: значение типа <list>
Пример:
8
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

autopep8 ON
"""

n = int(input('Введите число: '))

n = n + 1


def get_fibonacci(n):
    fibo_nums = []
    a, b = 1, 1
    for i in range(n - 1):
        fibo_nums.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n):
        fibo_nums.insert(0, a)
        a, b = b, a - b
    return fibo_nums


fibo_nums = get_fibonacci(n)
print(get_fibonacci(n))

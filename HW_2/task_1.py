"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Ввод: значение типа <float>
Вывод: значение типа <int>
Примеры:
6782.0
23
0.56
11
"""
n = input('Введите вещественное число: ')

def sum_digit_real_number(n):
    return sum(map(int, list(str(n).replace('.', ''))))


print(n)
print(sum_digit_real_number(n))

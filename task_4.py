"""
Написать программу по переводу целого числа из десятичной системы счисления в двоичную.
Ввод: значение типа <int>
Вывод: значение типа <int>
Примеры:
45
101101
3
11
2
10

autopep8 ON
"""
n = int(input('Введите число: '))


def conv_dec_to_bin(n):
    bin_num = ''
    while n > 1:
        bin_num += str(n % 2)
        n = n // 2
    return bin_num[::-1]


print(conv_dec_to_bin(n))

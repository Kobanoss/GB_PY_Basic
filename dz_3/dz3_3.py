"""
3.  Реализовать функцию my_func(), которая принимает три позиционных аргумента,
        и возвращает сумму наибольших двух аргументов.
"""


def my_func():
    arg_1, arg_2, arg_3 = map(int, input('Задайте три числа через пробел: ').split())
    my_list = [arg_1, arg_2, arg_3]
    my_list.remove(max(my_list))
    return sum(my_list)


print(my_func())


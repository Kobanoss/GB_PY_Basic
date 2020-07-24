"""
2.  Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
        имя, фамилия, год рождения, город проживания, email, телефон.
    Функция должна принимать параметры как именованные аргументы.
    Реализовать вывод данных о пользователе одной строкой.
"""


# Культурно:

def data_func():
    data_out = list(input('Введите свои: имя, фамилию, год рождения, город , email, телефон: ').split())
    return data_out


print(data_func()[:6])


# По заданию:

def true_data_func(func_name, func_surname, func_year, func_city, func_email, func_phone):
    true_data_out = [func_name, func_surname, func_year, func_city, func_email, func_phone]
    return true_data_out


try:
    print('Введите свои: имя, фамилию, год рождения, город , email, телефон: ')
    name, surname, year, city, email, phone = map(str, input().split())

    print(true_data_func(name, surname, year, city, email, phone))

except ValueError:
    print('Введите 6 значений!')

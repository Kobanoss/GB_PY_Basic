"""
1. Создать список и заполнить его элементами различных типов данных.
Реализовать скрипт проверки типа данных каждого элемента.
Использовать функцию type() для проверки типа.
Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
"""

list_1 = [1, 1.11, 'abc', {1, 2, 3}, (1, 'abc'), ['abcd'], True]
print(list_1)

for i in range(len(list_1)):
    print(type(list_1[i]))

'''
2. Для списка реализовать обмен значений соседних элементов, т.е. 
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д. 
При нечетном количестве элементов последний сохранить на своем месте. 
Для заполнения списка элементов необходимо использовать функцию input().
'''

input_string = input('Введите ваш список элементы отделяйте пробелом: ')
list_2 = input_string.split()

print(list_2)

for i in range(0, len(list_2) if (len(list_2)) % 2 else len(list_2) - 1, 2):
    temp = list_2[i]
    if i == len(list_2) - 1:
        break
    list_2[i] = list_2[i + 1]
    list_2[i + 1] = temp
print(list_2)

'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12. 
Сообщить к какому времени года относится месяц (зима, весна, лето, осень). 
Напишите решения через list и через dict.
'''

# Решение через list
try:
    month = int(input('Введите месяц: '))
except ValueError:
    print('Введите номер месяца!')
except NameError:
    print('Повторите ввод номера месяца')
list_3_winter = [1, 2, 12]
list_3_spring = [3, 4, 5]
list_3_summer = [6, 7, 8]
list_3_autumn = [9, 10, 11]

if month in list_3_winter:
    print('Зима')
elif month in list_3_spring:
    print('Весна')
elif month in list_3_summer:
    print('Лето')
elif month in list_3_autumn:
    print('Осень')
else:
    print('Введите существующий месяц')

# Решение через dict

try:
    month = int(input('Введите месяц: '))
except ValueError:
    print('Введите номер месяца!')
dict_1 = {'Зима': (1, 2, 12),
          'Весна': (3, 4, 5),
          'Лето': (6, 7, 8),
          'Осень': (9, 10, 11)
          }
for season, month_nu in dict_1.items():
    if month in month_nu:
        print(season)

'''
4. Пользователь вводит строку из нескольких слов, разделённых пробелами. 
Вывести каждое слово с новой строки. 
Строки необходимо пронумеровать. 
Если в слово длинное, выводить только первые 10 букв в слове.
'''

input_string_2 = input('Введите ваши слова, разделите пробелом: ')
list_4 = input_string_2.split()

for i in range(len(list_4)):
    print(f'{i + 1}. {list_4[i][0:10]}')

'''
5. Реализовать структуру «Рейтинг», 
        представляющую собой не возрастающий набор натуральных чисел. 
У пользователя необходимо запрашивать новый элемент рейтинга. 
Если в рейтинге существуют элементы с одинаковыми значениями, 
        то новый элемент с тем же значением должен разместиться после них.
'''

input_string_3 = input('Введите ваш список из невозрастаюих натуральных элеменов, отделяйте пробелом: ')
list_5 = input_string_3.split()
print(list_5)

try:
    list_5[0] = int(list_5[0])
    if list_5[0] < 0:
        print('Введите натуральное число(Целое и неотрицательное)')
        exit()

    for i in range(0, len(list_5) - 1, 1):
        list_5[i + 1] = int(list_5[i + 1])

        if list_5[i] < 0:
            print('Введите натуральное число(Целое и неотрицательное)')
            break
        if list_5[i] < list_5[i + 1]:
            print('Числа не должны возрастать')
            break
except ValueError:
    print('Требуются целые значения!')

n_element: int = 0

try:
    while True:
        n_element = int(input('Введите новый элемент \n'
                              'Введите любой не целочисленный символ для выхода из ввода: '))
        if n_element < 0:
            print('Введите натуральное число(Целое и неотрицательное)')
            break
        for i in range(len(list_5)):
            if n_element > max(list_5):
                list_5.insert(0, n_element)
                break
            elif n_element < min(list_5):
                list_5.append(n_element)
                break
            elif (n_element <= list_5[i - 1]) and (n_element > list_5[i]):
                list_5.insert(i, n_element)
                break
        print(list_5)

except ValueError:
    print('Вы ввели отличное от целочисленного значение')

'''
6. * Реализовать структуру данных «Товары». 
Она должна представлять собой список кортежей. 
Каждый кортеж хранит информацию об отдельном товаре. 
В кортеже должно быть два элемента — номер товара и словарь с параметрами 
        (характеристиками товара: название, цена, количество, единица измерения). 
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
'''

import copy

full_list = []
step_tuple = tuple()
step_dict = {}
n: int = 0
analytics_dict = {}
copy_dict = {}
run: int = 0
while True:

    run = run + 1
    step_dict.clear()

    print('Введите 1, чтобы заполнить данные о товаре;')
    print('Введите 2, чтобы вывести полную аналитику по товарам;')
    print('Введите 3, чтобы вывести список товаров;')
    print('Введите 0, чтобы выйти: ')
    check = int(input())
    if check == 1:
        step_dict['Название'] = input('Введите название нового товара ')
        step_dict['Цена'] = input('Введите стоимость нового товара ')
        step_dict['Количество'] = input('Введите количество нового товара ')
        step_dict['Ед'] = input('Введите единицы счета нового товара ')

        n = n + 1
        copy_dict = copy.deepcopy(step_dict)
        step_tuple = (n, copy_dict)
        full_list.append(step_tuple)

    elif check == 2:
        print(analytics_dict)
        continue

    elif check == 3:
        print(full_list)
        continue

    elif check == 0:
        break

    else:
        print('Введите 1, 2, 3 или 0')

    if run > 1:
        analytics_dict['Название'] = analytics_dict.get('Название') + ('; ') + copy_dict.get('Название')
        analytics_dict['Цена'] = analytics_dict.get('Цена') + ('; ') + copy_dict.get('Цена')
        analytics_dict['Количество'] = analytics_dict.get('Количество') + ('; ') + copy_dict.get('Количество')
        analytics_dict['Ед'] = analytics_dict.get('Ед') + ('; ') + copy_dict.get('Ед')
    else:
        analytics_dict['Название'] = copy_dict.get('Название')
        analytics_dict['Цена'] = copy_dict.get('Цена')
        analytics_dict['Количество'] = copy_dict.get('Количество')
        analytics_dict['Ед'] = copy_dict.get('Ед')
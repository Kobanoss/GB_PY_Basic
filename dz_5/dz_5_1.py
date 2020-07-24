"""
1.  Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
    Об окончании ввода данных свидетельствует пустая строка.
"""
from itertools import count

with open('test.txt', 'w+') as f:
    input_line = ' '
    while input_line != '':
        input_line = input('Введите новую строку: ')
        f.write(input_line + '\n')
    f.seek(0)
    print(f.read())


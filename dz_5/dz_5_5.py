"""5.  Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
with open('nu_list.txt', 'w+') as f:
    try:
        input_line = input('Введите список через пробел: ')
        input_nu_list = list(map(int, (input_line.split())))
        f.write(input_line)
        f.seek(0)
        print(f'Сумма всех чисел: {sum(input_nu_list)}')
    except ValueError:
        print('Введите числа!')

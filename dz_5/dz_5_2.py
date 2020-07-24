"""
2.  Создать текстовый файл (не программно), сохранить в нем несколько строк,
    выполнить подсчет количества строк, количества слов в каждой строке.
"""


with open('text.txt', 'a+') as f:
    input_line = ' '
    while True:
        input_line = input('Введите новую строку: ')
        if input_line != '':
            f.write(input_line + '\n')
        else:
            break
    f.seek(0)
    file = open('text.txt').read()
    print(f.read())
    run = 0
    f.seek(0)
    amount_lines = len(f.readlines())
    print(f'Кол-во строк: {amount_lines}')
    f.seek(0)
    while run != amount_lines:
        run = run + 1
        print(f'Кол-во слов в строке <{run}> :  {len(f.readline().split())}')


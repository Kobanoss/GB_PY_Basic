"""
4.  Создать (не программно) текстовый файл со следующим содержимым:
    One — 1
    Two — 2
    Three — 3
    Four — 4
    Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
    При этом английские числительные должны заменяться на русские.
    Новый блок строк должен записываться в новый текстовый файл.
"""
from googletrans import Translator

with open('en_translator_base.txt', 'a+') as f:
    while True:
        input_en_nu_name = input('Введите название цифры: ')
        input_en_nu = input('Введите цифру: ')
        if input_en_nu_name != '' and input_en_nu != '':
            f.write(input_en_nu_name.capitalize() + ' - ' + input_en_nu + '\n')
        else:
            break

    f.seek(0)
    amount_lines = len(f.readlines())
    run = 0
    translator = Translator()

    f.seek(0)
    nf = open('ru_translator_base.txt', 'w+')
    while run != amount_lines:
        run += 1
        translator_list = f.readline().split()
        argv = translator_list[0]
        input_ru_nu = translator_list[2]
        result = translator.translate(f'{argv}', src='en', dest='ru')
        nf.write(str(result.text).capitalize() + ' - ' + input_ru_nu + '\n')
    nf.seek(0)
    print(nf.read())
    nf.close()


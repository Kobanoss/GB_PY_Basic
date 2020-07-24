"""
6.  Необходимо создать (не программно) текстовый файл,
    где каждая строка описывает учебный предмет и наличие лекционных, практических и лабораторных занятий
    по этому предмету и их количество.
    Важно, чтобы для каждого предмета не обязательно были все типы занятий.
    Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
    Вывести словарь на экран.
"""


def subject_sort(subject):
    if int(subject) == 0:
        return 'Занятия отсуствуют'
    else:
        return subject


with open('university_base.txt', 'a+') as f:
    while True:
        input_name = input('Введите название предмета: ')
        input_lec_nu = input('Введите кол-во лекционных занятий, если их нет - пишите 0: ')
        input_practice_nu = input('Введите кол-во практических занятий занятий, если их нет - пишите 0: ')
        input_lab_nu = input('Введите кол-во лабораторных занятий, если их нет - пишите 0: ')
        if (input_name or input_lec_nu or input_practice_nu or input_lab_nu) == '':
            break
        else:
            f.write(input_name + ' :  ' + subject_sort(input_lec_nu) + ' (лек); '
                    + subject_sort(input_practice_nu) + ' (прак);  ' + subject_sort(input_lab_nu) + ' (лаб).\n')
    f.seek(0)
    print(f.read())
    f.seek(0)
    amount_lines = len(f.readlines())
    f.seek(0)
    run = 0
    subject_sum_dict = {}
    while run != amount_lines:
        sum_hours = 0
        subject_list = f.readline().split()
        for el in subject_list:
            try:
                sum_hours = sum_hours + int(el)
                # Переходим к следующей итерации, если это не число
                # Работает с любым файлом в котором есть число занятий, не обязательно, заданным программно
            except ValueError:
                continue
        subject_sum_dict[subject_list[0]] = sum_hours
        run += 1
    print(subject_sum_dict)


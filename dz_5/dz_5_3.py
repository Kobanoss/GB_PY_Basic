"""
3.  Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
    Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
    Выполнить подсчет средней величины дохода сотрудников.
"""

with open('salary_base.txt', 'a+') as f:
    while True:
        input_surname = input('Введите новую фамилию: ')
        input_salary = input(f'Введите зарплату (в тыс. руб) сотрудника с фамилией: <{input_surname}>: ')
        if input_surname != '' and input_salary != '':
            f.write(input_surname + ' ' + input_salary + '\n')
        else:
            break
    f.seek(0)
    amount_lines = len(f.readlines())
    run = 0
    employee_sum = 0
    less20 = []
    f.seek(0)
    while run != amount_lines:
        run += 1
        salary_list = f.readline().split()
        employee_sum = employee_sum + float(salary_list[1])
        if float(salary_list[1]) < 20:
            less20.append(salary_list[0])
    print(less20)
    print(employee_sum / run)


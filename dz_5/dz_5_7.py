"""
7.  Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
        название, форма собственности, выручка, издержки.
    Пример строки файла: firm_1 ООО 10000 5000.
    Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
    Если фирма получила убытки, в расчет средней прибыли ее не включать.
    Далее реализовать список.
    Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
    Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
    Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
    Итоговый список сохранить в виде json-объекта в соответствующий файл.
    Пример json-объекта:
    [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""
import json
with open('company_base.txt', 'a+') as f:
    while True:
        input_name = input('Введите название фирмы: ')
        input_type = input('Введите форму собственности: ')
        input_income = input('Введите выручку: ')
        input_costs = input('Введите издержки: ')
        if (input_name or input_type or input_income or input_costs) == '':
            break
        else:
            f.write(f'{input_name} {input_type} {input_income} {input_costs}\n')
    f.seek(0)
    print(f.read())
    f.seek(0)
    amount_lines = len(f.readlines())
    if amount_lines == 0:
        print('Введите компании!!!')
        exit()
    f.seek(0)
    run = 0
    average_income_sum = 0
    all_income_dict = {}
    average_income_dict = {}
    all_company_list = []
    average_counter = 0
    while run != amount_lines:
        run += 1
        result = 0
        company_list = f.readline().split()
        result = int(company_list[2]) - int(company_list[3])
        if int(company_list[2]) > int(company_list[3]):
            average_income_sum = average_income_sum + result
            average_counter += 1
            print(f'Компания {company_list[0]}: работает в плюс, '
                  f'прибыль - {int(company_list[2]) - int(company_list[3])}')
            all_income_dict[company_list[0]] = result

        elif int(company_list[2]) < int(company_list[3]):
            print(f'Компания {company_list[0]}: работает в минус, '
                  f'убыток - {-int(company_list[2]) + int(company_list[3])}, '
                  f' в итоговый список вносится, в подсчете среднего показателя не участвует ')
            all_income_dict[company_list[0]] = -result
        else:
            print(f'Компания {company_list[0]}: работает в 0, '
                  f'в итоговый список не вносится, в подсчете среднего показателя не участвует')
    average_income_dict['average_income'] = average_income_sum / average_counter

    all_company_list = [all_income_dict, average_income_dict]

    with open("company_base.json", "w") as write_file:
        json.dump(all_company_list, write_file)


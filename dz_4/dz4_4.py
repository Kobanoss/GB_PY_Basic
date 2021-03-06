"""
4.  Представлен список чисел. Определить элементы списка, не имеющие повторений.
    Сформировать итоговый массив чисел, соответствующих требованию.
    Элементы вывести в порядке их следования в исходном списке.
    Для выполнения задания обязательно использовать генератор.
    Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
    Результат: [23, 1, 3, 10, 4, 11]
"""


my_list = list(map(int, (input('Введите список через пробел: ').split())))

sorted_dict = {}

for el in my_list:
    sorted_dict[el] = sorted_dict.get(el, 0) + 1

sorted_list = [el for el, value in sorted_dict.items() if value == 1]
print(sorted_list)




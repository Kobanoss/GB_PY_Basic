"""
5.  Программа запрашивает у пользователя строку чисел, разделенных пробелом.
    При нажатии Enter должна выводиться сумма чисел.
    Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
    Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
    Но если вместо числа вводится специальный символ, выполнение программы завершается.
    Если специальный символ введен после нескольких чисел,
        то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

"""

sum_out = 0
while True:

    my_list = []
    temp = (input('Задайте числа через пробел, для выхода - любой символ: ').split())

    check_list = list(temp)
    print(check_list)
    i = 0

    try:

        for element in check_list:
            my_list.insert(i, int(element))
            i = i + 1

    except ValueError:
        print('Вы кажется вышли в окно')
        sum_out = sum_out + sum(my_list)
        print(sum_out)
        break

    sum_out = sum_out + sum(my_list)
    print(sum_out)
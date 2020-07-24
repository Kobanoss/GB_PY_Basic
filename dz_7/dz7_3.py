"""
3. Реализовать программу работы с органическими клетками.
Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
    сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
    Данные методы должны применяться только к клеткам
    и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение.
Объединение двух клеток.
При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание.
Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
    иначе выводить соответствующее сообщение.
Умножение.
Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
"""

from __future__ import print_function


class Multicellular:  # Раз у нас не одна клетка, то логичнее назвать класс - Многоклеточное
    def __init__(self, amount: int):
        self.amount = amount
        self.cells_amount = self.amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if type(value) != int or value < 0:
            print('Invalid input')
            exit()
        self._amount = value

    def __str__(self):
        return str(self.cells_amount)

    def __int__(self):
        return self.cells_amount

    def __add__(self, other):
        print(f'{self.cells_amount} cells + {other.cells_amount} cells: ', end='')
        return Multicellular(self.cells_amount + other.cells_amount)

    def __sub__(self, other):
        if self.cells_amount > other.cells_amount:
            print(f'{self.cells_amount} cells - {other.cells_amount} cells: ', end='')
            return Multicellular(self.cells_amount - other.cells_amount)
        else:
            return 'Amount cells in the first organism same or lower then in the second organism'

    def __mul__(self, other):
        print(f'{self.cells_amount} cells * {other.cells_amount} cells: ', end='')
        return Multicellular(self.cells_amount * other.cells_amount)

    def __truediv__(self, other):
        print(f'{self.cells_amount} cells // {other.cells_amount} cells: ', end='')
        return Multicellular(self.cells_amount // other.cells_amount)

    def out(self):
        return print(f'In this organism has about {self.cells_amount} cells\n')

    def make_order(self, str_size):
        cell_str = ''
        for cell in range(self.cells_amount):
            if cell % str_size == 0:
                cell_str = cell_str + '\n'
            cell_str = cell_str + '*'

        return cell_str


try:
    print()
    cell_mix_1 = Multicellular(40)
    cell_mix_1.out()

    cell_mix_2 = Multicellular(100)
    cell_mix_2.out()

    print(cell_mix_1 + cell_mix_2)

    q = cell_mix_1 + cell_mix_2
    print(q)

    print(cell_mix_1 - cell_mix_2)

    print(cell_mix_2 - cell_mix_1)

    print(cell_mix_1 * cell_mix_2)

    print(cell_mix_1 / cell_mix_2)

    print(cell_mix_2 / cell_mix_1)

    print(cell_mix_1.make_order(5) + '\n')

    cell_mix_1.out()

    new_cell_str = cell_mix_1.make_order(21)

    print(new_cell_str)

except (ValueError, NameError, TypeError) as err:
    print(err.args)

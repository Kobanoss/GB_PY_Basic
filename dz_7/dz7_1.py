"""
1.  Реализовать класс Matrix (матрица).
    Обеспечить перегрузку конструктора класса (метод __init__()),
        который должен принимать данные (список списков) для формирования матрицы.
    Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
    Примеры матриц вы найдете в методичке.
    Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
    Далее реализовать перегрузку метода __add__()
        для реализации операции сложения двух объектов класса Matrix (двух матриц).
    Результатом сложения должна быть новая матрица.
    Подсказка: сложение элементов матриц выполнять поэлементно —
        - первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
"""

from __future__ import print_function


class Matrix:
    def __init__(self, matrix_list: list = None):
        self.matrix = matrix_list
        self.buffer = []

    def __str__(self):
        print('-' * (len(self.matrix[1]) + (len(self.matrix[1]) + 1) * 5 + 2))
        for n_list in self.matrix:

            print('|     ', end='')
            for el in n_list:
                s = (str(el) + '     ')
                print(s[0:6], end='')
            print('|')
        print('-' * (len(self.matrix[1]) + (len(self.matrix[1]) + 1) * 5 + 2))
        return ''

    def same_type(self, other):
        for other_el_list in other.matrix:
            for matrix_el_list in self.matrix:
                while len(other_el_list) < len(matrix_el_list):
                    other_el_list.append(0)
        for other_el_list in other.matrix:
            for matrix_el_list in self.matrix:
                while len(other_el_list) > len(matrix_el_list):
                    matrix_el_list.append(0)
        for iq in range(len(self.matrix[1])):
            self.buffer.append(0)

        if len(other.matrix) < len(self.matrix):
            for i in range(len(self.matrix) - len(other.matrix)):
                other.matrix.append(self.buffer)
        if len(other.matrix) > len(self.matrix):
            for i in range(len(other.matrix) - len(self.matrix)):
                self.matrix.append(self.buffer)

    def __add__(self, other):
        self.same_type(other)
        self.buffer = []
        for el, elements in zip(self.matrix, other.matrix):

            self.buffer_small = []
            for nu, els in enumerate(el):
                self.buffer_small.append(int(els) + int(elements[nu]))

            self.buffer.append(self.buffer_small)

        return Matrix(self.buffer)


matrix = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix2 = Matrix([[1, 2, 3], [3, 4, 3], [5, 6, 3]])

print(matrix)
print(matrix2)
print(matrix + matrix2)

"""
2.  Реализовать проект расчета суммарного расхода ткани на производство одежды.
    Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
    К типам одежды в этом проекте относятся пальто и костюм.
    У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
    Это могут быть обычные числа: V и H, соответственно.
    Для определения расхода ткани по каждому типу одежды использовать формулы:
        для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
         Проверить работу этих методов на реальных данных.
    Реализовать общий подсчет расхода ткани.
    Проверить на практике полученные на этом уроке знания:
        реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""

from abc import ABC, abstractmethod


class ClothesABC(ABC):

    @abstractmethod
    def cloth(self):
        pass


class Clothes(ClothesABC):
    def __init__(self, size, type):
        self.type = type
        self._size = size

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if value == 'Coat' or value == 'Suit':
            self._type = value
        else:
            print('Invalid type of clothes')
            exit()
    def self_run(self):
        print(str(self.__str__()))
        print(id(self))

    def cloth(self):
        if self._type == 'Coat':
            return self._size / 6.5 + 0.5
        if self._type == 'Suit':
            return 2 * self._size + 0.3
        else:
            return 'Error clothes type '


try:

    coat = Clothes(4, 'Coat')

    print(coat.cloth())

    suit = Clothes(3, 'Suit')

    print(suit.cloth())

    coat.self_run()
    print(id(coat))
except (TypeError, SyntaxError, ValueError):
    print('Введите данные в формате: "<Показатель габаритов(Рост/Размер)>, <Тип(Coat/Suit>"')

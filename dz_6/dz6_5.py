"""
5.  Реализовать класс Stationery (канцелярская принадлежность).
    Определить в нем атрибут title (название) и метод draw (отрисовка).
    Метод выводит сообщение “Запуск отрисовки.”
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
    В каждом из классов реализовать переопределение метода draw.
    Для каждого из классов методы должен выводить уникальное сообщение.
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    def __init__(self):
        self.title: str  # Немного не понял, зачем этот title, как заглушка?

    def draw(self):
        self.title: str
        return print('Запуск отрисовки\n')


class Pen(Stationery):
    def draw(self):
        return print('А ручки то вот они\n')


class Pencil(Stationery):
    def draw(self):
        return print('Новая порция карандашей для Джона Уика\n')


class Handle(Stationery):
    def draw(self):
        return print('Мужик, у тебя есть маркер?\n'
                     'Нет?\n'
                     'Мужик, держи маркер\n')


draw = Stationery()
draw.draw()

draw = Pen()
draw.draw()

draw = Pencil()
draw.draw()

draw = Handle()
draw.draw()


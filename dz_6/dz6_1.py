"""
1.  Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
    Атрибут реализовать как приватный.
    В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
    Продолжительность первого состояния (красный) составляет 7 секунд,
        второго (желтый) — 2 секунды,
            третьего (зеленый) — на ваше усмотрение.
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
    Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
import time


class TrafficLight:
    def __init__(self):
        self.__color = ''

    def running(self):
        while True:
            self.__color = 'Red'
            self.get_color()
            time.sleep(7)
            self.__color = 'Yellow'
            self.get_color()
            time.sleep(5)
            self.__color = 'Green'
            self.get_color()
            time.sleep(15)

    def get_color(self):
        print(self.__color)


lighter = TrafficLight()
lighter.running()

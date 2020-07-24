"""
4.  Реализуйте базовый класс Car.
    У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
    А также методы: go, stop, turn(direction),
        которые должны сообщать, что машина поехала, остановилась, повернула (куда).
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
    Для классов TownCar и WorkCar переопределите метод show_speed.
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
    Создайте экземпляры классов, передайте значения атрибутов.
    Выполните доступ к атрибутам, выведите результат.
    Выполните вызов методов и также покажите результат.
"""

from itertools import cycle


class Car:

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.status = True  # True - двигается, False - нет
        self.side_list = ['север', 'запад', 'юг', 'восток']
        self.side_step = cycle(self.side_list)
        self.direction = next(self.side_step)
        self.__check_speed()

    def __check_speed(self):  # Скрытый метод для проверки скорости в начале

        if self.speed == 0:
            print('Машина изначально стоит\n')
            self.status = False

        elif self.speed > 0:
            print(f'Машина <{self.name}> изначально едет со скоростью {self.speed} км/ч на {self.direction}\n')
            self.status = True

        else:
            print('Задний ход не предусмотрен\n')  # Проверка на отрицательную скорость
            exit()

    def go(self):  # Машина начинает свое движение

        if not self.status:
            self.speed = 1
            self.status = True
            return print(f'Машина <{self.name}> пришла в движение и двигается на на {self.direction}\n')

        else:
            return print(f'Машина уже едет со скоростью {self.speed} км/ч на {self.direction}\n')

    def stop(self):  # Машина прекращает свое движение

        if self.status:
            self.speed = 0
            self.status = False
            return print(f'Машина <{self.name}> остановилась\n')

        else:
            return print('Машина стоит\n')

    def turn(self, direction):  # Машина поворачивает в определенную сторону
        if self.speed > 0:
            if direction == 'Направо':
                next(self.side_step)
                next(self.side_step)
                self.direction = next(self.side_step)
                return print(f'Вы повернули направо, теперь вы движитесь на {self.direction}\n')
            elif direction == 'Налево':
                self.direction = next(self.side_step)
                return print(f'Вы повернули налево, теперь вы движитесь на {self.direction}\n')
            else:
                print('Для поворота введите налево или направо\n')
        else:
            return print('Машина должна двигаться, чтобы поворачивать\n')

    def speed_up(self, bonus_speed: int):  # Увеличивает скорость машины на определенный показатель

        if bonus_speed > 0 and self.status == True:
            self.speed = self.speed + bonus_speed
            return print(f'Вы увеличили скорость своего передвижения на {bonus_speed} км/ч\n')

        elif not self.status:
            return print(f'Вы Должны для начала завести машину\n')

        elif bonus_speed <= 0:
            return print(f'Введите положительную скорость\n')

    def speed_reduce(self, bonus_speed: int):  # Уменьшает скорость машины на определенный показатель

        if 0 < bonus_speed < self.speed and self.status == True:
            self.speed = self.speed - bonus_speed
            return print(f'Вы уменьшили скорость своего передвижения на {bonus_speed} км/ч\n')

        elif not self.status:
            return print(f'Чтобы уменьшать свою скорость, вы должны ехать\n')

        elif bonus_speed > self.speed:
            return print(f'Вы не можете скинуть скорость ниже 0, введите другое значение\n')

        elif bonus_speed <= 0:
            return print(f'Введите положительную скорость\n')

    def show_speed(self):  # Выводит скорость машины

        print(f'Скорость машины <{self.name}>: {self.speed} км/ч\n')

    def menu_bar(self):
        print()
        case = int(input('Выберите пункт меню:\n'
                         '1. Проверить скорость\n'
                         '2. Начать движение\n'
                         '3. Оставиться\n'
                         '4. Увеличить скорость\n'
                         '5. Уменьшить скорость\n'
                         '6. Повернуть\n'
                         '7. Посмотреть характеристики своей машины\n'
                         '8. Выйти из программы\n'
                         'Выбранный пункт меню: '))
        print()
        if case == 1:
            return self.show_speed()
        elif case == 2:
            return self.go()
        elif case == 3:
            return self.stop()
        elif case == 4:
            return self.speed_up(int(input('На сколько км\ч вы хотите увеличить свою скорость: ')))
        elif case == 5:
            return self.speed_reduce(int(input('На сколько км\ч вы хотите уменьшить свою скорость: ')))
        elif case == 6:
            case_turn = int(input('Меню:\n'
                                  'Выберите куда повернуть:\n'
                                  '1. Повернуть налево\n'
                                  '2. Повернуть направо\n'
                                  'Выбранный пункт меню: '))
            print()
            if case_turn == 1:
                return self.turn('Налево')
            if case_turn == 2:
                return self.turn('Направо')
        elif case == 7:
            return print('Характеристики вашей машины:\n'
                         f'1. Классификация по канону: {self.__class__}:\n'
                         f'1. Название: {self.name}\n'
                         f'2. Цвет: {self.color}\n')
        elif case == 8:
            return exit()
        else:
            print('Введите доступный пункт меню.\n')


class TownCar(Car):

    def show_speed(self):

        if self.speed <= 40:
            print(f'Скорость машины <{self.name}>: {self.speed} км/ч, двигается на {self.direction}\n')

        else:
            print(f'Вы превысили скоростной лимит, ваша скорость: {self.speed} км/ч, а должна быть не больше  40')

    def speed_up(self, bonus_speed: int):
        super().speed_up(bonus_speed)
        if self.speed > 40:
            print(f'Вы превысили скоростной лимит, ваша скорость: {self.speed} км/ч, а должна быть не больше  40')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):

        if self.speed <= 60:
            print(f'Скорость машины <{self.name}>: {self.speed} км/ч\n'
                  f'Направдение движения: {self.direction}\n')

        else:
            print(f'Вы превысили скоростной лимит, ваша скорость: {self.speed} км/ч, а должна быть не больше  60')

    def speed_up(self, bonus_speed: int):
        super().speed_up(bonus_speed)
        if self.speed > 60:
            print(f'Вы превысили скоростной лимит, ваша скорость: {self.speed} км/ч, а должна быть не больше  60')


class PoliceCar(Car):
    pass


def input_car():
    case = int(input('Меню:\n'
                     'Выберите тип машины:\n'
                     '1. PoliceCar\n'
                     '2. SportCar\n'
                     '3. TownCar\n'
                     '4. WorkCar\n'
                     '5. Закрыть программу\n'
                     'Выбранный пункт меню: '))
    print()
    if case == 5:
        exit()

    argv1, argv2, argv3 = input('Введите скорость, цвет и марку машины\n'
                                'Все через пробел: ').split()
    argv1 = int(argv1)
    print()
    if case == 1:
        return PoliceCar(argv1, argv2, argv3, True)
    elif case == 2:
        return SportCar(argv1, argv2, argv3, False)
    elif case == 3:
        return TownCar(argv1, argv2, argv3, False)
    elif case == 4:
        return WorkCar(argv1, argv2, argv3, False)
    else:
        print('Введите доступный пункт меню.\n')


try:

    my_car = input_car()
    while True:
        my_car.menu_bar()

except (TypeError, ValueError, IndexError):
    print('Введите все в формате: \n'
          'Скорость - целое число,\n'
          'Цвет и название в формате строки\n')

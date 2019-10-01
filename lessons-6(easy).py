# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.


class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(self.name, 'is moving')

    def stop(self):
        print(self.name, 'is stoping')

    def turn(self, direction):
        print(self.name, 'is turning to the', direction)


class SportCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=False)


class WorkCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=False)


class PoliceCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=True)


car_1 = TownCar(150, 'red', 'audi R8')
car_1.turn('right')

car_2 = PoliceCar(180, 'white', 'bmw')
car_2.stop()

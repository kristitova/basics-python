import random


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Машина {self.name} поехала")

    def stop(self):
        print(f"Машина {self.name} остановилась")

    def turn_(self):
        if random.randint(1, 2) == 1:
            print(f"Машина {self.name} повернула направо")
        else:
            print(f"Машина {self.name} повернула налево")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name} : {self.speed}")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости!")
            print(f"Текущая скорость автомобиля {self.name} : {self.speed}")
        else:
            print(f"Текущая скорость автомобиля {self.name} : {self.speed}")


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости!")
            print(f"Текущая скорость автомобиля {self.name} : {self.speed}")
        else:
            print(f"Текущая скорость автомобиля {self.name} : {self.speed}")


class PoliceCar(Car):
    pass


a = TownCar(70, "black", "Mazda", False)
a.go()
a.show_speed()
a.turn_()
a.stop()

b = WorkCar(30, "blue", "Kamaz", False)
b.go()
b.show_speed()
b.turn_()
b.stop()

c = PoliceCar(50, "white-black", "Lada", True)
c.go()
c.turn_()
c.show_speed()
c.stop()

d = SportCar(90, "red", "Mercedes-Benz", False)
d.go()
d.show_speed()
d.stop()

from abc import ABC, abstractmethod


class Clothes_Abstract(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def raschet_(self):
        print(f"Количество ткани:")


class Palto(Clothes_Abstract):

    @property
    def raschet_(self):
        if self.param <= 180:
            f"Количество ткани для пальто: {round((self.param / 6.5) + 0.5, 2)}"
            return round((self.param / 6.5) + 0.5, 2)
        else:
            return f"Ограничения по росту"


class Costum(Clothes_Abstract):

    @property
    def raschet_(self):
        if self.param <= 180:
            f"Количество ткани для костюма: {round((2 * self.param) + 0.3, 2)}"
            return round((2 * self.param) + 0.3, 2)
        else:
            return f"Ограничения по росту"


P_1 = Palto(160)
P_2 = Palto(180)
C_1 = Costum(120)
try:
    print(f"Общая ткань: {P_1.raschet_ + P_2.raschet_ + C_1.raschet_}")
except:

    print("Измените параметры!")

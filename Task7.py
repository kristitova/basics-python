class complex_num:
    def __init__(self, act, mnim):
        self.act = act
        self.mnim = mnim

    def __str__(self):
        return f"Комплексное число: {self.act}+{self.mnim}i"

    def __add__(self, other):
        return f"Сумма комплексных чисел равна: {self.act + other.act}+" \
               f"{self.mnim + other.mnim}i"

    def __mul__(self, other):
        return f"Произведение комплексных чисел равно:" \
               f"{(self.act * other.act - self.mnim * other.mnim) + (self.act * other.mnim + other.act * self.mnim)}i"


z_1 = complex_num(3, 4)
print(z_1)
z_2 = complex_num(5, 6)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)

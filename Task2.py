class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


data_1 = input("Введите 1-е число: ")
data_2 = input("Введите 2-е число: ")

try:
    data_1 = int(data_1)
    data_2 = int(data_2)
    if data_2 == 0:
        raise OwnError("Делитель не должен быть равен нулю!")
    division = int(data_1 / data_2)
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Деление двух чисел: {division}")

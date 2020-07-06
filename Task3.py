class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


list_ = []
while True:
    a = input("Введите число: ")
    try:
        a = int(a)
        list_.append(a)
        if a == "q":
            break
    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        print(f"Введенный список: {list_}")

    print("Хотели бы вы добавить числа?")
    answer = input("Да - y, Нет - n: ")
    if answer == "y":
        continue
    else:
        break

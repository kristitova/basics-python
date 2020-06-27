from functools import reduce

try:
    with open("text_5.txt", 'x', encoding="utf-8") as file_:
        a = list(map(int, input("Введите числа: ").split()))
        print(f"{a}", file=file_)
        print(f"Сумма чисел равна: {reduce(lambda x, y: x + y, a)}", file=file_)
        print(f"Сумма чисел равна: {reduce(lambda x, y: x + y, a)}")
except:
    print("Файл уже создан")

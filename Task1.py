file_ = open("file_1.txt", 'x', encoding="utf-8")
while True:
    element = input("Введите данные: ")
    if element != "":
        file_.write(element + '\n')
    else:
        print("Вы ничего не ввели")
        break
file_.close()

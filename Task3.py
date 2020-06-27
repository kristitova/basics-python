with open("text_3.txt", 'r', encoding="utf-8") as file_:
    oklad = []
    print(f"Сотрудники с окладом меньше 20 тыс.: ")
    for line in file_:
        l_ = line.split()
        oklad.append(float(l_[1]))
        if float(l_[1]) < 20000:
            print(f"{l_[0]} : {l_[1]}")
    sum_ = 0
    for i in oklad:
        sum_ += i
print(f"Средняя величина дохода сотрудников: {sum_ / len(oklad)}")

with open("file_1.txt", 'r', encoding="utf-8") as file_:
    i = 0
    for line in file_:
        words = 0
        if not line.isspace():
            i += 1
            print(line.replace('\n', ''))
            for word in line:
                if word.isspace():
                    words += 1
            print(f"Количество слов в {i} строке: {words}")
    print(f"Количество строк: {i}")

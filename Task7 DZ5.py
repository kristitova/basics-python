import json

with open("text_7.txt", 'r', encoding="utf-8") as file_:
    with open("text_77.json", 'w', encoding="utf-8") as file_1:
        pribyl = 0
        info = {}
        result_ = []
        for line in file_:
            l_ = line.split()
            pribyl = (int(l_[2]) - int(l_[3]))
            info[l_[0]] = pribyl
        result_.append(info)
        average_pribyl = sum([int(i) for i in info.values() if int(i) > 0]) / \
                         len([int(i) for i in info.values() if int(i) > 0])

        result_.append({"Средняя прибыль": average_pribyl})
        json.dump(result_, file_1, ensure_ascii=False, indent=4)

from functools import reduce

with open("text_6.txt", 'r', encoding="utf-8") as file_:
    info_ = {}
    for line in file_:
        num = []
        num_ = 0
        while num_ < len(line):
            s_int = ''
            a = line[num_]
            while '0' <= a <= '9':
                s_int += a
                num_ += 1
                if num_ < len(line):
                    a = line[num_]
                else:
                    break
            num_ += 1
            if s_int != '':
                num.append(int(s_int))
        sum_ = reduce(lambda x, y: x + y, num)
        l_ = line.split()
        info_.update({l_[0]: sum_})
    print(f"{info_}")

from translate import Translator

with open("text_4.txt", 'r', encoding="utf-8") as file_:
    with open("f__4.txt", 'x', encoding="utf-8") as f_4:
        num_eng = []
        num_rus = []
        for line in file_:
            l_ = line.split("-")
            num_eng.append(l_[0])
            translator = Translator(to_lang="Russian")
            translation = translator.translate(l_[0])
            num_rus.append(translation)
            f_4.write(str(num_rus[-1]) + ' -' + l_[1])

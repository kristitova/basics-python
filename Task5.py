class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки методом: {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки c помощью ручки методом: {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки c помощью карандаша методом: {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки c помощью маркера методом: {self.title}")


a = Pen("underlined")
a.draw()

b = Pencil("cursive")
b.draw()

b = Handle("bold")
b.draw()

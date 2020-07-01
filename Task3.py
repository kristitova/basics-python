class Worker:
    oklad = 0
    bonus = 0
    _income = {"dohod": oklad, "bonus": bonus}

    def __init__(self, name, surname, position, oklad, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"dohod": oklad, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, oklad, bonus):
        super().__init__(name, surname, position, oklad, bonus)

    def full_name(self):
        print(f"Имя сотрудника: {self.name}")
        print(f"Фамилия сотрудника: {self.surname}")

    def total_income(self):
        total = self._income["dohod"] + self._income["bonus"]
        print(f"Доход сотрудника с учетом премии: {total}")


a = Position("Ivan", "Ivanov", "manager", 40000, 2000)
a.full_name()
a.total_income()

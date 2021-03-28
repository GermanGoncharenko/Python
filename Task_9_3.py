class Worker:

    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wages": w, "bonus": b}


class Position(Worker):
    def __init__(self, n, s, p, w, b):
        super().__init__(n, s, p, w, b)
    def get_full_name(self):
        print(f"Сотрудник: {self.surname} {self.name}\nДолжность: {self.position}")
    def get_total_income(self):
        print(f"Доход: {self._income['wages'] + self._income['bonus']}")

worker_1 = Position("Иван", "Иванов", "Электрик", 5, 3)
worker_1.get_full_name()
worker_1.get_total_income()
print()
worker_2 = Position("Андрей", "Сергеев", "Администратор", 1, 2)
worker_2.get_full_name()
worker_2.get_total_income()
print()
worker_3 = Position("Даниил", "Соколов", "Водитель", 5, 5)
worker_3.get_full_name()
worker_3.get_total_income()



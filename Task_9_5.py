class Stationery:
    def __init__(self, t="чего-то"):
        self.title = t

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} ручкой")

class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} карндашом")

class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} маркером")


a = Pen()     # указать в скобках что-то
a.draw()
b = Pencil()  # указать в скобках что-то
b.draw()
c = Handle()  # указать в скобках что-то
c.draw()

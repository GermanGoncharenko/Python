import random
class Car:
    def __init__(self, s, c, n):
        self.speed = s
        self.color = c
        self.name = n
        self.in_police = {"Yes": True, "No": False}

    def go(self):
        print(f"Go")

    def stop(self):
        print("Stop")

    def turn(self):
        direction = ["север", "северо-восток", "восток", "юго-восток", "юг", "юго-запад", "запад", "северо-запад"]
        print("Поворот на", random.choice(direction))

    def show_speed(self):
        print(f"Текущяя скорость автомобиля: {self.speed}")

class TownCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n)

    def show_speed(self):
        if self.speed > 60:
            print("Внимание! Привышение скорости!")
        else:
            print(f"Текущяя скорость автомобиля: {self.speed}")

class SportCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n)

class WorkCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n)

    def show_speed(self):
        if self.speed > 40:
            print("Внимание! Привышение скорости!")
        else:
            print(f"Текущяя скорость автомобиля: {self.speed}")


class PoliceCar(Car):
    def __init__(self, s, c, n):
        super().__init__(s, c, n)

car_1 = Car(100, "синий", "Audi")
car_1.show_speed()
car_2 = TownCar(61, "синий", "Audi")
car_2.show_speed()
car_3 = WorkCar(39, "синий", "Audi")
car_3.show_speed()
#car_1.turn()
#car_1.show_speed()

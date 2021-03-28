import time


class TrafficLight:
    def __init__(self, c):
        self.__color = c

    def running(self):
        time.sleep(7)
        print("red")
        time.sleep(2)
        print("yellow")
        time.sleep(7)
        print("green")
        time.sleep(2)
        print("yellow")


t = TrafficLight("color")
t.running()



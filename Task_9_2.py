class Road:
    def __init__(self, l, w):
        self._length = l
        self._width = w

    def running(self):
        time.sleep(7)
        print("red")
        time.sleep(2)
        print("yellow")
        time.sleep(7)
        print("green")
        time.sleep(2)
        print("yellow")
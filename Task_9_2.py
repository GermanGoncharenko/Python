class Road:

    def __init__(self, l, w):
        self._length = l
        self._width = w

    def calculation(self, layer):
        a = self._length * self._width * 25 * 0.001 * layer
        print(f"Расчёт массы асфальта, необходимого для покрытия всей дороги: {a} т.")


calcul = Road(20, 5000)
calcul.calculation(5)

x = [[31, -32, 56], [-37, 43, 11], [51, 45, -86]]
y = [[9, 32, -6], [37, 7, 39], [-1, 5, 36]]

class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        return '\n'.join(map(str, self.lists))

    def __add__(self, other):
        z = []
        for i in range(len(self.lists)):
            z.append([])
            for j in range(len(self.lists[0])):
                z[i].append(self.lists[i][j] + other.lists[i][j])
        return '\n'.join(map(str, z))


matrixX = Matrix(x)
matrixY = Matrix(y)
print(f'\n X matrix:\n\n{matrixX}\n')
print(f'Y matrix:\n\n{matrixY}\n')
print(f'Z = X * Y:\n\n{matrixX + matrixY}')


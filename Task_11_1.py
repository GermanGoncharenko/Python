class Data:
    def __init__(self, d, m, y):
        self.data = f"{d}-{m}-{y}"

    def work(self):
        q = self.data.split("-")

    @classmethod
    def work_1(cls):
        return cls.work

    #@staticmethod
    #def

a = Data(5, 1, 1995)
print(a.work)
print(a.data)
print(type(a.data))



class Fraction():
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def display(self):
        return str(self.num) + "/" + str(self.denom)


f1 = Fraction(8, 5)
print(f1)                        # <__main__.Fraction instance at 0x03987C10>
print(f1.display())              # 8/5


class Fraction():
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom

    def __str__(self):
        return str(self.num) + "/" + str(self.denom)


f1 = Fraction(8, 5)
print(f1)                         # 8/5
class fractional:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        c = self.a.split('/')
        d = self.b.split('/')
        num = int(c[0])*int(d[1])
        den = int(c[1])*int(d[0])
        res = str(num)+'/'+str(den)
        print(res)
f = fractional(input('enter 1st fractional number'),input('enter 2nd fractional number'))
f.addition()

class fractional:
    def __init__(self,a,b,c,d):
        self.num1 = a
        self.denom1 = b
        self.num2 = c
        self.denom2 = d
    def __str__(self):
        self.dennom = self.denom1*self.denom2
        self.num = self.num1*self.denom2 + self.num2*self.denom1
        return str(self.num)+'/'+str(self.denom)

f = fractional(input('enter numenater of 1st fractional number'),input('enter denominater of 1st fractional number'),input('enter numenater of 2nd fractional number'),input('enter denominater of 2nd fractional number'),)
f.addition()
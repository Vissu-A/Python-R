# Ways to achive polymorphism

    # 1.Method over loading      # To impliment over loading inheritance is not mandatory,we can do overloading in the same class

             # 1. changing number of arguments to the method
             # 2. changing type of arguments to the method

    # 2.Method over riding       # To impliment over raiding inheritance is mandatory/must and should




# Method over loading

# NOTE: # python doesn't supports 'Method over loading', We may overload the methods but can only use the latest defined method

# Case:1                          changing number of arguments to the method

class overload:
    def product(self,a, b):
        p = a * b
        print(p,'\n')

    def product(self,a, b, c):
        p = a * b * c
        print(p,'\n')

o = overload()
#o.product(4,5)                            # TypeError: product() missing 1 required positional argument: 'c'
o.product(4,5,6)                          # 120


# Case:2                          changing type of arguments to the method

   # this over loading is not possible in python,because in python arguments types are defind by the given value implicitly


# NOTE:   Indirect way to achive method over loading by using 'Arbitary arguments'

# EX:1
class overload1:
    i = None
    def product(self,*a):
        for x in a:
            if self.i == None:
                self.i = x
            else:
                self.i = self.i *x

        print(self.i,'\n')
        self.i = None
o1 = overload1()
o1.product(5,6,7)
o1.product(5,6)
o1.product(5)

# EX:2
class overload2:
    def addition(self,*b):
        print(sum(b),'\n')

o2 = overload2()
o2.addition(5,6,7)
o2.addition(5,6)
o2.addition(5)



# Method over riding

# python supports 'Method over riding', to impliment method over riding inheritance is must and should


class Account():
    def __init__(self, bal, acc):
        self.bal = bal
        self.acc = acc
    def deposit(self, amount):
        self.bal += amount
    def withdrawl(self, amount):
        self.bal -= amount
    def interest(self):
        interest =  (self.bal*0.01)/100
        self.bal += interest
class SavingAccount(Account):
    def interest(self):
        interest = (self.bal*0.04)/100
        self.bal += interest
o = SavingAccount(500, 25)

# interest() method is presented in both account/parent class and savingaccount/child class , But functionality/interest rates are different
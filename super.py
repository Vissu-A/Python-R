# super() is used to call parent class method from the child class
# super() is points to immediate parent class of a child class

# syntax:

   # in 2.x
              # super(child class name,self).method name(arguments to method)
   # in 3.x
              # super().method name(arguments to method)


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
        return interest
        self.bal += interest
class SavingAccount(Account):
    def interest(self):
        interest = (self.bal*0.04)/100
        print(interest)                    # 20.0(savingaccount class/child class interest)

        inte = super().interest()          # calling parent class interest() method from the child class using super() keyword
        print(inte)                        # 5.0(account class/parent class interest)

        self.bal += interest
o = SavingAccount(50000, 25)
o.interest()
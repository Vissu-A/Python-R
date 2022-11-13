# Ways to achive Encapsulation
  # 1.Data hiding
  # 2.Abstraction

# Data hiding
class datahiding():
    __a = 11               # private variable(Accessing scope is within the class)
    __b = 7                # private variable(Accessing scope is within the class)
    _c = 5                 # protected variable((Accessing scope is within the class and it's sub-classes)
    def addition(self):
        print(self.__a+self.__b+self._c)
class child(datahiding):
    def subtraction(self):
        #print(self.__a - self.__b)          # AttributeError: 'child' object has no attribute '_child__a' and '_child__b'
        print(self._c)                       # 5

d = child()
d.addition()
d.subtraction()
print()

# NOTE: private variables __a,__b are converted as '_datahiding__a' and '_datahiding__b' internally. this is called 'name mangling'


# Example for 100% encapsulated class
class encap():
    __a = 5
    def __init__(self):
        self.__b = 7
    def getval(self):
        return self.__a,self.__b
    def setval(self,val1,val2):
        self.__a = val1
        self.__b = val2

e = encap()
#print(e.__a)                     # AttributeError: 'encap' object has no attribute '__a'
#print(e.__b)                     # AttributeError: 'encap' object has no attribute '__b'
print(e.getval())
e.setval(15,17)
print(e.getval())
print(e._encap__a)                # 15(name mangling concept)
print(e._encap__b)                # 17(name mangling concept)
print()


class Myclass():
    __username = "nag"
    __password = "nag"
    def __init__(self):
        self.__var = 15
    def __authenticate(self, username, password):
        if self.__username == username and self.__password == password:
            return True
        return False
    def getVar(self, username, password):
        #if authentication is ok then return var
        if self.__authenticate(username, password):
            return self.__var
        return "please login with admin to perform this action"
    def setVar(self, username, password, val):
        if self.__authenticate(username, password):
            self.__var = val
        return "please login with admin to perform this action"
o = Myclass()
print(o.getVar("nag", "nag"))
o.setVar("nag", "nag", 25)
print(o.getVar("nag", "nag"))
print()
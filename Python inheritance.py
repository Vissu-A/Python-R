# syntax:
     # class <derived/child class name> (base class/parent class name):


class parent:
    a = 5
    b = 2
    def myfun(self):
        print('i am from parent class')

    @classmethod
    def subtract(cls):
        print(cls.a - cls.b)

    @staticmethod
    def multiply(p, q):
        print(p * q)

class child(parent):
    def addition(self):
        print(self.a+self.b)       # a,b are class variables,so they can be inherited to child class

c = child()
c.addition()
c.myfun()
c.subtract()
c.multiply(5,7)     # myfun,subtract,multiply functions are not defined in child class,they are inherited from parent class

# Note: we can inherite 'class variables',but we cann't inherite 'instance variables'

# type-1:
class parent:
    a = 5
    b = 2
    def myfun(self):
        print('i am from parent class')
        self.x = 7
class child(parent):
    def addition(self):
        print(self.a+self.b+self.x)               #AttributeError: 'child' object has no attribute 'x',Bcz 'x' is instance variable

c = child()
#c.addition()
c.myfun()

# type-2:
class parent:
    a = 5
    b = 2
    def __init__(self,c):
        self.x = c

    def myfun(self):
        print('i am from parent class')
        self.y = 7
class child(parent):
    def addition(self):
        print(self.a+self.b+self.x+self.y)

#c = child()             # TypeError: __init__() missing 1 required positional argument: 'c',there is no __init__ in child class,but__init__
                        # is inherited from parent class and that takes 1 required positional argument
#c.addition()
#c.myfun()


class parent:
    a = 5
    b = 2
    def __init__(self,c):
        self.x = c

    def myfun(self):
        print('i am from parent class')
        self.y = 7
class child(parent):
    def __init__(self):pass

    def addition(self):
        print(self.a+self.b+self.x+self.y)    # AttributeError: 'child' object has no attribute 'x' and attribute 'y'

c = child()
c.addition()
c.myfun()
print()


# Types of inheritances

# 1.single inheritance
# 2.multi-level inheritance
# 3.multiple inheritance
# 4.hierarchical inheritance
# 5.hybrid inheritance

# single inheritance

class Base:
    pass
class Derived(Base):
    pass

# multi-level inheritance

class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Derived1):
    pass

# multiple inheritance

class Base1:
    pass
class Base2:
    pass
class MultiDerived(Base1, Base2):
    pass

# hierarchical inheritance

class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Base):
    pass
class Derived3(Base):
    pass

# hybrid inheritance ---> it's a combination of any two other inheritances

class Base:
    pass
class Derived1(Base):
    pass
class Derived2(Derived1):
    pass
class D(Derived1,Derived2):
    pass


# MRO(method resolution order)

# in python every class is derived from the class called " object ".so,technicaly all other classes either built-in and user-defined are
# derived from 'object' class and all objects are instances of object class

# NOTE: Any specified attribute is searched first in the current class. If not found, the search continues into parent classes in
# depth-first, left-right fashion(in case of multiple inheritance)

# we can see MRO of a class by using ' __mro__' or 'mro()'
   # syntax:
        # class name.__mro__/class name.mro()

print(Derived2.__mro__)     #(<class '__main__.Derived2'>, <class '__main__.Derived1'>, <class '__main__.Base'>, <class 'object'>)
print()
print(Derived1.mro())       #(<class '__main__.Derived1'>, <class '__main__.Base'>, <class 'object'>)
print()

print(MultiDerived.mro())   # [<class '__main__.MultiDerived'>, <class '__main__.Base1'>, <class '__main__.Base2'>, <class 'object'>]





# multiple inheritance
class parent1:
    a = 5
    b = 2
    def addition(self):
        print(self.a+self.b)
class parent2:
    a = 7
    b = 3
    def addition(self):
        print(self.a+self.b)
class child(parent1,parent2):
    c = 10
    d = 7
    def subtraction(self):
        print((self.c - self.d) - (self.a - self.b))  # a,b values are taken from parent1 class,if a,b are not there,then it's go to parent2

c = child()
c.subtraction()
c.addition()       # the addition()method in parent1 class is executed,if that method is not there then it will go to parent2 class
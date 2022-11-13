# For instance methods the 1st argument is 'self' always (i.e, object/instance)
# Instance methods are bounded to instance(i.e,object) only, any changes in the instace methods will effect to that instance(i.e,object) only

# For class methods the 1st argument is 'cls' always (i.e, cls points to current classname)
# class methods are bounded to class, any changes in the class methods will effect to all the class instances(i.e, objects)

# we cann't change the value of a class variable in instance method until and unless we use the class name, but we can change the value of a
# instance variable in instance method

# When should we go for class methods?
       # when there is a change in the class that should effect to all the class instances(i.e, objects)
           # example: there is a class called 'car drawing sheet',initially we are taken car colour as 'red' in the class,but after designing
           # some objects to the class we changed the car colour 'red' to 'blue',so this colour change should effect to all the class objects
           # in this senario we use class method.

# For static methods no 'self' (or) no 'cls' arguments
# static methods are also bounded to class.
# When should we go for static methods?
       # when we want a method to process some data without respecting to the class (or) instance(i.e, without passing 'cls'/'self' as 1st arg)
       # in this senario if we use class method/instance method unnecessarly we are increasing the load on interpreter by passing the
       # cls/self as 1st argument to the method,so to avoid this we use static methods
# we can change static method to class method/instance method at any time we want
class meth:
    a = 1
    b = 2

    def __init__(self,firval,secval):
        self.x = firval
        self.y = secval

    def adding(self):

        print(self.x + self.y + self.a + self.b)   # a,b are class variables, we can call class variables with instance (self.a == instance.a)
        self.x = 57  # changing instance variable 'x' value  in instance method using instance(i.e,object)

        # changing the class variable value in instance method
             # Case1:
                  # self.a = 50  # this will create a instance variable 'a' with the value 50
             # Case2:
                  # meth.a = 47  # this will change the class variable 'a' value from previous value to 47

    @classmethod
    def subtract(cls):
        print(cls.a - cls.b - m.x - m.y)


    @staticmethod
    def multiply(p,q):
        print(p*q)*(m.x*m.y*meth.a*meth.b)



m = meth(5,7)           # creating object

m.adding()              # calling instance method
meth.adding(m)

m.subtract()            # calling class method
meth.subtract()

m.multiply(5,7)         # calling static method
meth.multiply(5,7)
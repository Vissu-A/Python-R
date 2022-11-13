# class is a template or blueprint to build a specific type of object

# object is an instance or specimen or snippet of a class

       # Each object has 2 charecteristics
            # 1. state         state is defind by the attributes or variables
            # 2. behavior      behavior is defind by the methods


# Creating a class in python

    # class <classname>:
          # '''doc string about the class'''
          # attributes (or) variables + methods


class demo:
    ''' This class is designed to demonistrate creating a class in python'''
    a = 2
    b = 5
    def addition(self):
        return self.a+self.b
    def subtraction(self):
        return self.a - self.b

# Creating Object for the class

d = demo()   # Creating Object for the class is called " Instantiation "
             # 'd' is called as " instance "
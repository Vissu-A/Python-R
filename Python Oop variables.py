a = 10
b = 15     # a,b,c are global varibles they are not bounded to any class,method or instance(i.e, object), they are totally indipendent variables
c = 20

class variables:
    d = 25
    e = 30    # d,e,f are class variables, bounded to class
    f = 35

    global g   # 'global' is the keyword used to define global variables inside the class/method
    g = 40     # g is global variable

    def __init__(self,firval,secval,thival):

        self.x = firval     # Nothing but v.x(i.e, object.x) = firval
        self.y = secval     # Nothing but v.y(i.e, object.y) = secval
        self.z = thival     # Nothing but v.z(i.e, object.z) = thival ,  x,y,z are instance variables, bounded to instance(i.e, object)

    def add(self,m):
        l = int(input('Enter 2nd number to add'))        # l,m are local variable, bounded to that perticular method/function only
        print(m+l)


v = variables(int(input('Enter 1st number')),int(input('Enter 2nd number')),int(input('Enter 3rd number')))
v.add(int(input('Enter 1st number to add')))

# NOTE:-
# 1. global variables are called directely
# 2. class variables are called with classname (or) instance(i.e, object)
# 3. instance variables are called with instance(i.e, object) only
# 4. local variables are not called outside of the code where they are initialized




print(a,b,c,g)                # Accessing global variables
print(v.d,v.e,variables.f)    # Accessing class variables
print(v.x,v.y,v.z)            # Accessing instance variables

                              # Accessing local variables
# print(v.l)                  AttributeError: 'variables' object has no attribute 'l'
# print(variables.l)          AttributeError: type object 'variables' has no attribute 'l'
# print(v.m)                  AttributeError: 'variables' object has no attribute 'm'
# print(variables.m)          AttributeError: type object 'variables' has no attribute 'm'
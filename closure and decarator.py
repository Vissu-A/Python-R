# Closure

# Case1: argument to outer function is 'not a function'

def print_msg(msg):

    def printer():

        print(msg)

    return printer

print(print_msg("Hello"))      #<function print_msg.<locals>.printer at 0x0000016952687C80> inner function " printer()" object
another = print_msg("Hello")   #assigning returned inner function " printer()" object to variable to "another"
another()                      #calling the inner function " printer()"

#The print_msg() function was called with the string "Hello" and the returned function("printer()") was assigned to the name another.On calling
#another() is nothing but calling"printer()"the msg was still remembered although we had already finished executing the print_msg() function.
# This concept is called " Closure "


def adder(outer_argument): # outer function

  def adder_inner(inner_argument): # inner function, nested function

    return outer_argument + inner_argument # Notice outer_argument

  return adder_inner

add5 = adder(5) # this adds 5 to outer_argumnet of adder,add5 points towards "adder_inner()" function

add7 = adder(7) # this adds 7 to outer_argumnet of adder,add7 points towards "adder_inner()" function

print(add5(3)) # prints 8   [outer_argument(5) + inner_argument(3)]

print(add7(3)) # prints 10  [outer_argument(7) + inner_argument(3)]
print()

# Case2: argument to outer function is 'a function'

#Note:- argument to the outer function can be another function also,in this case we have to return that function (which is passed as an
# argument to outer function) in inner function,we must use paranthesis['()'] while returning it,otherwise it won't execute

def out(func):
    def add(u,v):             #Arguments of each function are local to that function only we can use x,y as arguments to function 'add()',
                              # Because x,y in 'mul()'are local to that function only,But it's not a good programming
        print(u+v)
        #return func          #this will simply prints function object address <function mul at 0x0000019D21C87EA0>,never execute
        return func(u,v)      #nothing but return mul(u,v) now control goes to mul(x,y) function
    return add
def mul(x,y):
    return x*y

c = out(mul)                  #the function "mul()" is passed to argument "func"
print(c(5,7))                 #c(5,7) nothing but add(5,7)
print()


# Decarator


def out(func):
    def add(x,y):
        print(x+y)
        return func(x,y)
    return add
@out
def mul(x,y):
    return x*y

print(mul(5,7))
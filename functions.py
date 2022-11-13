b = [2,3,4]
def myfun(a):
    c = [5,6,7]
    a.append(5)
    print(a)
myfun(b)
print(b)
#print(c)             NameError: name 'c' is not defined
#print(a)            NameError: name 'a' is not defined
print()


b = [2,3,4]
def myfun(a):
    b =[10, 11, 12]
    a = [6,7,8]
    a.append(5)
    print(b)
myfun(b)
print(b)
print()

b = [2,3,4]
def myfun(a):
    global b             #specifying that take 'b' as golbal not local to function
    b =[10, 11, 12]
    a = [6,7,8]
    a.append(5)
    print(b)
myfun(b)
print(b)
print()

#return statement
def arth(x,y):
    return x+y,x-y,x*y       #returning multiple values/results at a time by using "packing" concept
x = arth(10,20)
print(x)

def arth(x,y):
    return x+y,x-y,x*y       #returning multiple values/results at a time by using "packing" concept
z = arth(10,20)              #catchinmg function o/p into a varible by assigning function call to a variable
a,b,c = z                    # "un-packing"
print(a,'\n',b,'\n',c)
print()

# returning a function from another function( By using " Closure "  concept)

def print_msg(msg):

    def printer():

        print(msg)

    return printer

print(print_msg("Hello"))      #<function print_msg.<locals>.printer at 0x0000016952687C80> inner function " printer()" object
another = print_msg("Hello")   #assigning returned inner function " printer()" object to variable to "another"
another()                      #calling the inner function " printer()"

#The print_msg() function was called with the string "Hello" and the returned function("printer()") was assigned to the name another.On calling
#another() is nothing but calling"printer()"the msg was still remembered although we had already finished executing the print_msg() function.
# This concept is called " Closure " in python

def adder(outer_argument): # outer function
  def adder_inner(inner_argument): # inner function, nested function
    return outer_argument + inner_argument # Notice outer_argument
  return adder_inner
add5 = adder(5) # this adds 5 to outer_argumnet of adder,add5 points towards "adder_inner()" function
add7 = adder(7) # this adds 7 to outer_argumnet of adder,add7 points towards "adder_inner()" function

print(add5(3)) # prints 8   [outer_argument(5) + inner_argument(3)]
print(add7(3)) # prints 10  [outer_argument(7) + inner_argument(3)]
print()

def f1(a):
    def f2(b):
        return b + 5
    return f2
fun = f1(10)
print(fun(3))
print()

def f1(a):
    def f2(b):
        return a + b + 5
    return f2
fun = f1(10)
print(fun(3))
print()


def func1(x, y):
    def func2(p, q):
        return (x + p) * (y + q)
    return func2
x = func1(1, 2)
print(x(3, 4))
r = x(3, 4)
print(r)
print()

#when no separate arguments for inner function
def func1(x, y):
    def func2():           #x and y are non-local variables for this inner function(func2) But,it can access them (by default read only)
        return x * y
    return func2()
x = func1(1, 2)
print(x)
print()

def print_msg(msg):
    def printer():
        print(msg)     #argument "msg" is non-local to "printer()" function but,it can access because it's a nested function to print_msg()
    return  printer
print_msg("enter your message here\n")
print()

import timeit
print(timeit.timeit(stmt='lambda x,y:x+y', number=10))
#print(timeit.timeit(stmt=arth(10,20), number=10))      #ValueError: stmt is neither a string nor callable
print(timeit.timeit(stmt='def add(d,e): return(d+e)', number=10))

#Types of arguments
#1.Required/mandatory arguments
#2.Default arguments
#3.Keyword arguments
#4.*args(arbitary/variable length arguments)
#5.**kwargs(arbitary/variable length keyword arguments)

(a, *rest, b) = range(5)            #This sets a to 0, b to 4, and rest to [1, 2, 3]
print(a)
print(*rest)
print(b)

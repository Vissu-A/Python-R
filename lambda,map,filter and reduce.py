# lambda function : it's nothing but creating a function without any name(i.e,anonymous function) to use short period of time
# lambda functions are also called as anonymous functions
# lambda functions are created by using " lambda " keyword

# syntax:
    # lambda arguments : expression
    # we can have any number of arguments but we should have only one expression and the expression should be (or) include return statement
    # but,we can have print statement

square = lambda x: print(x**2)
square(2)

#square = lambda x: return x**2   # error: because expression for lambda doesn't includes 'return" statement

multi = lambda a,b: a*b
print(multi(5,7))

# map() function in python
# map() function must have atleast 2 arguments, 1st argument must be a function, 2nd agrument must be iterable(sequence)

#syntax:
     # map(x,y)
        # x ----> must be a function
        # y ----> must be a iterable(i.e, sequence)
# map() function iterate over the iterable(i.e,sequence) gets each value from sequence and passed to 1st argument(i.e, function())

l1 = list(input('Enter elements for 1st list \n'))
print(l1)
l2 = list(input('Enter elements for 2nd list \n'))
print(l2)

r = map(lambda a,b: int(a)+int(b),l1,l2)
print(r)
print([v for v in r])   #list comprehension

print(list(map(lambda a,b: int(a)+int(b),l1,l2)))

# getting charecter of the given ASCII value
li = input('Enter list of values separated by ",":\n')
print(li)
print(type(li))
print(list(map(chr,[int(val)for val in li.split(",")])))

# filter() function in python
# filter() function takes exactely 2 arguments

#syntax:
     # filter(x,y)
          # x ---> must be a "function or None"
          # y ---> must be iterable

# filter() ---> filters the elements in the iterable based of the function(if function returns True for element then,that element is added to o/p)
# return value of filter() is an iterator(i.e, filter object) in 3.x But,in 2.x it's a list

c = filter(lambda l: l%2,[1,2,3,4,5,6,7,8,9,10])
print(c)                     # gives filter object <filter object at 0x7f....> in 3.x

print(list(filter(lambda l: l%2,[1,2,3,4,5,6,7,8,9,10])))

print(list(filter(None,[1,2,3,4,5,6,7,8,9,10])))


#print(list(filter(lambda n: n%2,[1,2,3],[4,5,6])))              #error: TypeError: filter expected 2 arguments, got 3
print(list(filter(lambda n: n%2)))                               #error: TypeError: filter expected 2 arguments, got 1
print(list(filter(None)))                                        #error: TypeError: filter expected 2 arguments, got 1
print(list(filter([1,2,3,4,5,6,7,8,9,10])))                      #error: TypeError: filter expected 2 arguments, got 1



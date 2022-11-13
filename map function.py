#syntax: map() function takes at-least two arguments, 1st argument must be a function, 2nd argument must be a sequence(or)iterable object
                          #map(x,y)-----> x = should be function, y = should be iterable
l = [58,59,71,72]
x = list(map(chr,l))
print(x)
print()

li = [':', ';', 'G', 'H']
y=list(map(ord,li))
print(y)
print()

n = input('enter the numbers with space separated \n')
a = n.split(" ")
l1=[]
for x in a:
    l1.append(int(x))
print(l1)

z = list(map(lambda x:int(x),n.split(" ")))
print(z)

m = map            #assigning pre-defind map() function to a variable,not only pre-defind functions you can assign userdefind functions also
z = list(m(lambda x:int(x),n.split(" ")))
print(z)
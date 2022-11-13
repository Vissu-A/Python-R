a = [4,5,6]
def myfun(b):
    for x in b:
        print('before yield')
        yield x
        print('after yield')
c = myfun(a)
print('Generator function:',c)
print(next(c))
print()
print(next(c))
print()
print(next(c))
print()
#print(next(c))
print()
#print(c.__next__())
#print(c.__next__())
#print(c.__next__())
#print(c.__next__())

a  = [4,5,6]
def myfun(b):
    for x in b:
        return x
c = myfun(a)
print('Normal function:',c)
#print(next(c))                    #TypeError: 'int' object is not an iterator
#finding subset or not using set method
a = input('enter elments for set a\n')
b = input('enter elements for set b\n')
print(a)
print(b)
if set(b).issubset(set(a)):
    print('each element in set b exists in set a\nb is subset of a')
else:
    print('b is not a subset of a')

#finding subset or not without using set method
c = input('enter elments for set a\n')
d = input('enter elements for set b\n')
count=0
for x in set(d):
    if x in set(c):
       count +=1
if count == len(d):
    print('b is subset of a')
else:
    print('b is not a subset of a')
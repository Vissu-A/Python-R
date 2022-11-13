x=0
if x == 1:
    print('x is 1')
else: print('x is not 1')

#true statement (if condition) else else statement
print('x is 1') if x==1 else print('xis not 1')

l = [1,2,3,4,5,6,7,8,9]

print([( x**2 if x %2==0 else x**3)for x in l if x%3!=0])

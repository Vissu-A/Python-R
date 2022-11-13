x=int(input('enter first number\n'))
y=int(input('enter second number\n'))
z=int(input('enter third number\n'))

if(x>y and x>z):                      #compound condition = condition with (relational operators+logical operators)
    print(x,'is greater')
if(y>z and y>x):
    print(y,'is greater')
if(z>x and z>y):
    print(z,'is greater')

#in the above program we used only if statement, we write like this it's not a good programming practice,because all the if conditions are checked
# one by one,eventho the 1st condition satisfied it will terminated program,it will also check remaing two conditions so,unnecessarly
# we are wasting some time(cpu cycles) so speed decreases, to overcome this we use 'elif' and 'else'


x=int(input('enter first number\n'))
y=int(input('enter second number\n'))
z=int(input('enter third number\n'))
if(x>y and y>z):
    print(x,'is greater')
elif(y>z):
    print(y,'is greater')
else:
    print(z,'is greater')

#here when the 1st condition is satisfied(True) it terminates the program,it wonn't check the remaimg conditions so,speed increases


#read 3 numbers from user,find biggest number amoung it,if 1st number is zero print'first number is zero'

x=int(input('enter first number\n'))
y=int(input('enter second number\n'))
z=int(input('enter third number\n'))

if x == 0 or (x > y and x > z):
    print('first number is greater')
if (y > z and y > x) and x != 0:
    print('second number is greater')
if (z > x and z > y) and x != 0:
    print('third number is greater')

#read 4 numbers from user and find smallest number

a = int(input('enter first number\n'))
b = int(input('enter second number\n'))
c = int(input('enter third number\n'))
d = int(input('enter fourth number\n'))
if (a == b) | (a == c) | (a == d) | (b == c) | (b == d) | (c == d):
    print('you have given  an invalid number')
if a < b and a < c and a < d:
    print(a, 'is smaller')
if b < a and b < c and b < d:
    print(b,'is smaller')
if c < a and c < b and c < d:
    print(c,'is smaller')
if d < a and d < b and d < c:
    print(d,'is smaller')

#read 4 numbers from user and find smallest number

a = int(input('enter first number\n'))
b = int(input('enter second number\n'))
c = int(input('enter third number\n'))
d = int(input('enter fourth number\n'))
if (a == b) or (a == c) or (a == d) or (b == c) or (b == d) or (c == d):
    print('you have given  an invalid number')
if a < b and a < c and a < d:
    print(a, 'is smaller')
if b < c and b < d:
    print(b,'is smaller')
if c < a and c < b and c < d:
    print(c,'is smaller')
if d < a and d < b and d < c:
    print(d,'is smaller')



#read age from user,if age is not an integer print 'invalid age'

age = input('enter your age\n')
if(age.isdigit()):
    a=int(age)
    if a < 18:
        print('he/she is lucky')
    elif 18 <= a <= 21:
        print('enjoying his/her life')
    elif 21 <= a <= 30:
        print('difficulties are started')
    else:
        print('understood the life')
else:
    print('invalid age')

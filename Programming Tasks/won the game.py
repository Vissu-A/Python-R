import random
x = int(input('enter your number\n'))
while x != random.randint(0,x):
    print('you lose')
else:
    print('you won')


''' import random
x = int(input('enter your number\n'))
y = random.randint(0,x)
while x != y:                          # Infinate loop, because y value is fixed for every iteration
    print('you lose')
else:
    print('you won') '''


import random

y = input('do you want to continue: yes/no\n')
while y in ('yes','y'):
    x = int(input('enter your number\n'))
    while x != random.randint(0,x):
        print('you lose')
    else:
        print('you won')
        y = input('do you want to continue: yes/no\n')
else:
    print('comming out from the program')
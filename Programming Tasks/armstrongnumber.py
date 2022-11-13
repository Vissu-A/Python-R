n = int(input('enter your number'))
sum = 0
v = n
while n != 0:
    r = n % 10
    sum = sum + r**len(str(v))
    n = n // 10

if sum == v:
    print('armstrong number')

else:
    print('not armstrong')
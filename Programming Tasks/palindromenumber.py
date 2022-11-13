n = int(input('enter your number\n'))
sum = 0
v = n
while n != 0:
    r = n % 10
    sum = sum*10+r
    n = n // 10
if sum == v:
    print('palindrome')
else:
    print('not palindrome')
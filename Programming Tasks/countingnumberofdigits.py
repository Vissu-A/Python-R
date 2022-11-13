n = int(input('Enter your number'))
count = 0
while n > 0:
    count += 1
    n //= 10
print('number of digits in the given number are:',count)
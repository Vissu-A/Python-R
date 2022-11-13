n = int(input('enter your number to check prime or not'))

factors = 0
for i in range(2,n//2+1):
    if n % i == 0:
        factors += 1

print('not a prime number') if factors > 0 else print('prime number')




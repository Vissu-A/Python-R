# with recursion
def factorial(n):
    # return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

    if n in (0, 1):
        return 1

    else:
        return n * factorial(n-1)


print(factorial(int(input('enter your number to find factorial\n'))))


# without recursion
def factor(n):
    if n in (0, 1):
        return 1

    else:
        fact = 1
        while n > 0:
            fact = fact * n
            n = n - 1
        return fact


print(factor(int(input('enter your number\n'))))
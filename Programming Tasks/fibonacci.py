def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print('you have entered negative number')

    elif n == 0:
        print(a)

    elif n == 1:
        print(b)

    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        print(b)


fibonacci(int(input('enter your number')))



def fibonacci1(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci1(n-1) + fibonacci1(n-2))

n = int(input("Enter your number"))
# for i in range(n+1):
#     print(fibonacci1(i))
print(fibonacci1(n))
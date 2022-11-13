lr = int(input('enter starting of the range'))
ur = int(input('enter ending of the range'))

for num in range(lr,ur+1):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            break
    else:
        print(num)
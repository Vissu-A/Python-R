def bubblesort(l):
    for i in range(len(l)):                            # len(l) = 7   0-6    l = [1,3,4,2,7,6,8]
        for j in range(len(l)-1):                      # len(l)-1 =6  0-5
            if l[j] > l[j+1]:
                l[j], l[j + 1] = l[j + 1], l[j]

    print(l)


lst = []
size = int(input('enter size of list'))
for i in range(size):
    element = int(input('enter element'))
    lst.append(element)


bubblesort(lst)
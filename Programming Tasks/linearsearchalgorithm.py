def linearsearch(l,v):
    for i in range(len(l)):
        if l[i] == v:
            print('value matched at index', i)
        else:
            print('value not found')


linearsearch([1,5,2,3,4,6,7,8,9,10],int(input('enter the value to be search')))
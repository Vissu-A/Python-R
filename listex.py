#2nd occarnce of an element in a list
l = [1,2,3,'python',11.5,'avengers',1,5,6,[1,2,3]]
print(l.index(1,(l.index(1))+1,len(l)))
print()

a = [4,5,6,4,5,7,8,4,6,5,7,8,9,1,2,1,10,11,12]
nr=[]
rl=[]
for x in a:
    if x not in rl:
        if a.count(x) > 1:
            rl += (x,a.count(x))
        else:
            nr.append(x)
print(rl)
print(nr)
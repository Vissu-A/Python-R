i=input('enter any string')
print(i[::-1])
print()

print(i[-1::-1])
print()

print(''.join(reversed(i)))
#explanation
b=reversed('avengers')
print(b)                 #gives <reversed object at (0x000001641741CF28) number not fix,changes for execution>
rs=''
for x in b:
    print(x)
    rs +=x
    print(rs)
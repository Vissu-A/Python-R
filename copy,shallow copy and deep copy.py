#copying list using '=' operator,(hard copy)

a = [[1,2,3],[4,5,6]]
print(a)                        #[[1,2,3],[4,5,6],[7,8,9]]
print(id(a))                    #1653412157192    not fix it's changes for every execution
print()                         #just printing a line space

b = a
print(b)                        #[[1,2,3],[4,5,6],[7,8,9]]
print(id(b))                    #1653412157192    not fix it's changes for every execution
print()                         #just printing a line space

b.append(4)
print(b)                        #[[1,2,3],[4,5,6],4]
print(a)                        #[[1,2,3],[4,5,6],4]
print()                         #just printing a line space

#there is a drawback with this type of copy,if we made changes to newlist(b) those will reflect in oldlist(a),because both will point/refer
#same memory location
#some times we need to make changes to newlist without effecting the old list,in that case we use shallow copy,deep copy


#shallow copy

#to do shallow copy we need to import python's pre-defind "copy" module\
#shallow copy creates a new and independent object for original object not for nested objects but,it stores the reference of nested objects
import copy
a1 = [[1,2,3],[4,5,6],[7,8,9]]
print(a1)                       #[[1,2,3],[4,5,6],[7,8,9]]
print(id(a1))                   #2572751291976  not fix it's changes for every execution
print(id(a1[1][1]))
print()

b1 = copy.copy(a1)                #[[1,2,3],[4,5,6],[7,8,9]]
print(b1)
print(id(b1))                   #2572751291912  not fix it's changes for every execution
print(id(b1[1][1]))
print()                         #just printing a line space

b1.append([10,11,12])
print(b1)
print(a1)
print()                         #just printing a line space

b1.append(13)
print(b1)
print(a1)
print()                         #just printing a line space


old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

new_list[1][1] = 'AA'

print("old list:", old_list)        #[[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
print("New list:", new_list)        #[[1, 1, 1], [2, 'AA', 2], [3, 3, 3]]
print()                             #just printing a line space
#disadvantage in this copy is,if we made changes in new list's nested objects then,they will reflect in old list's nested objects also
#because both list's nested objects will point/referce same memory location

#deep copy

#we will do deep copy by using "copy.deepcopy()"
#deep copy will create a new and independent object for original and nested objects also
import copy
a2 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(a2)
print(id(a2))
print(id(a2[1][1]))
print()                         #just printing a line space
b2 = copy.deepcopy(a2)
print(b2)
print(id(b2))
print(id(b2[1][1]))
print()                          #just printing a line space

b2[1][0] = 'BB'
print(b2)
print(a2)
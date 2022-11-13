#List is a collection of elements (or) objects.the elements may be a homogenious/hetrogenious and it may contain another list as an item,this's
#called 'nested-list'

#creating List:

       #1. By using square brackets "[]"
L = [1,2,3,10.5,11.7,'sequence','i like python']
print(type(L))
       #2. By using function "list()" ,this function will take only one element/object, we use this to covert any sequence into List
#Li = list(7) #error:int object is not iterable,Note:- argument to list() function must be iterable(i.e sequence(list,set,tuple,string,dict)
s={1,2,3}
Li=list(s)
print(type(Li))

#li = list(7,11.5,'python') #error :list() takes at most 1 argument (3 given)

L1 = [1,3,5,7,11.5,1.7,'python',[2,4,6,8,10.4,2.8,'hi i am Robo']]   #nested-list with hetrogenious elements
L2 = [[1,3,5],[2,4,6],[1,2,3,4,5,6]]                                 #nested-list with homogenious elements

L3 = []            #empty list
print(bool(L3))    #Returns "False"
print(dir(L3))     #Gives all the functions and methods in List

L4 = range(5,30,5)  #creating list using 'range()' function
print(L4)           #[5,10,15,20,25] in 2.x,but in 3.x range(5, 30, 5)
print(type(L4))     #type is <class 'list'> in 2.x,but in 3.x <class 'range'>---> but internally it's treated as list like[5,10,15,20,25]

#List indexing:

     # we can access elements in the list by using 'indexing',python supports '+ve indexing' and '-ve indexing' also
L5=[3,5,7,9,10.5,11.5,'python',2,4,'Avengers']
print(L5[8])
print(L5[9])
print(L5[-1])
#print(L5[9.0])       #error :list indices must be integers or slices, not float

L6=[[1,2,3],[4,'python',10.5],[5,7,11.7]]
print(L6[1][-1])
print(L6[1][-2])

#List sclicing:

       #By using list sclicing we can access range of items in a list(i.e from specified start index to specified end index) using sclicing
       #operator colon ":"
L7 = [2,4,3,5,'python',11.7,'avengers',10.5]
print(L7[2:5])
print(L7[2:7:2])   #sclicing takes 3 parameters,1.starting index(default value=0) 2.ending index(default=len(List)) 3.step value(default=1)
print(L[:])        #gives entire list

L8 = range(21,41)
print(L8[::1])    #entire list in 2.x,but range(21, 41) in 3.x
print(L8[:-1:])   #total list in 2.x,but range(21,40) in 3.x
print(L8[2:5:-1]) #gives empty list [] : because 2 -1=1 -1=0 -1=-1 so,it's never reach end index 5
                  #we have to use '-ve step value' when start index value > end index value(but,both indexes +ve)
print(L8[10:-1:2])
print(L8[5:2:-1])

#updating/changing list elements:
a=[2,3,5,8,1]
a[0]=20           #updating single element at a time[20,3,5,8,1]
a[1:3]=[30,50]    #updating multiple elements at a time[20,30,50,8,1], a[1:3]=(1,2) index 1 to index 3-1=2 so,index 1=30 ,index 2=50
a[2:]=[20,30]     #[20,30,20,30] from index 2 to end index so,index 2=20 and index3,index4=30
a[2:]=[4,5,6]     #[20,30,4,5,6] from index 2 to end index so,index 2=4 index 3=5 and index 4 is created and equal to 6
a[1:4]=[40]       #[20,40,6] index 1,index2,index3=40
#a[:2]=40         #error : can only assign iterable,but 40 is int type
a[:2]=[40]        #[40,6]from index 0 to index 2-1=1 value is 40

#List operators
a = [4, 5, 6]
b = [4, 5, 7]
print(a>b)         #false,15>16(sum of elements in list a < sum of elements in list b)
print(a<b)         #true,15<16

print([7,1,1]>[5,4,3])
print([7,1,1]>[5,1,1])

#List functions
l=[1,2,3]
dir(l)            #gives all the functions in List[append(),extend(),insert(),pop(),remove(),index(),count(),sort(),reverse(),copy(),clear()

#append()

#List.append(x): append will add 'x' to end of the list l.the 'x' may be a element or another sequence(list,set,tuple,string,dictionary)
l.append(4)       #[1,2,3,4]
print(l)
#l.append(5,6,7)  #error : append takes exactly one argument at a time
#adding another list to an existing list
l.append([5,6,7]) #[1,2,3,4,[5,6,7]] entire sequence[5,6,7] is added as single element
#adding set to an existing list
l.append({8,9})   #[1,2,3,4,[5,6,7],{8,9}]
l.append((11,13)) #[1,2,3,4,[5,6,7],{8,9},(11,13)]

#extend()

#List.extend(x):  extend takes exactly one argument,the argument must be iterable(i.e sequence(list,set,tuple,string,dictionary)) and it will iterate over
#the given argument(sequence) get value by value and adds at end of the list
l2 = [1,2,3]
#l2.extend(4)  #error : int object is not iterable,'argument must be iterable'
l2.extend([4]) #[1,2,3,4]
l2.extend('python') #[1,2,3,4,'p','y','t','h','o','n']
l2.extend([6,7,8])
l2.extend({9.10})
l2.extend((11,13))

#insert()

#List.insert(x,y): insert takes exactly two arguments,x=index in new list y=element to be added at specified index(x) in the new list
l3=[1,2,3,5]
l3.insert(3,4) #[1,2,3,4,5]
vowels = ['a', 'e', 'o', 'u']
vowels.insert(2,'i')            #['a', 'e', 'i', 'o', 'u']
l3.insert(5,[6,7])
l3.insert(7,{8,9})
l3.insert(6,(10.5,11.7))
print(l3)

#pop()

#List.pop(): pop without index will delete last element in the list and returns the deleted element
#List.pop(x): pop with index will delete element at the specified index  and returns the deleted element
l4=[1,2,3,'python',10.4,11.7,'avengers',[7,11,13],{3,5,7},(2,4,6)]
print(l4.pop())  #this will delete (2,4,6) and returns it
v=l4.pop(6)      #this will delete the element at index 6(avengers) and returns it,we are saving the deleted element in a variable(v)

#remove()

#List.remove(x): remove takes exactly one argument(x) at a time,x=value to be remove/delete,it will remove the specified value from the list
#it returns 'value error' when given value is not present in the list
l5=[1,2,3,'python',10.4,11.7,'avengers',[7,11,13],{3,5,7},(2,4,6)]
print(l5)
print(l5.remove((2,4,6)))     #None,remove doesn't return any value
print(l5.remove('python'))    #None,remove doesn't return any value
print(l5)
#print(l5.remove('hello'))  #error: value error,because 'hello' is not in list

#index()

#List.index(x): index takes exactly one argument(x) at a time.index will serach for the element(x) in the given list and returns it's 1st
#occurence index number.if element(x) is not in the given list returns 'value error'
l6=[1,2,3,4,5,3,7,5,3]
print(l6.index(3))
print(l6.index(5))
#print(l6.index(11))   #error: value error

#count()

#list.count(x): count takes exactly one argument(x) at a time.count method will count how many times an element(x) occured/repeated in the
#given list and return it

l7=[1,2,3,5,4,3,6,8,5,7,3,9,5,1]
print(l7.count(1))   #2
print(l7.count(3))   #3
print(l7.count(5))   #3

#sort()

#list.sort(): sort method will arrange all the elements in the list an oreder.by default order is asccending(asc)
l8=[9,8,7,6,5,1,2,3,4,5,6,7]
l8.sort()    #by default is ascending order,if we want descending order first use sort()-->will get 'asc' order-->reverse()-->'desc' order
print(l8)

#reverse()

#list.reverse():reverse function will reverse the elements in the given list
l9=[1,2,3554,6,5,4,555,14,25,7,5,6,51]
print(l9)
l9.reverse()
print(l9)
os = ['Windows', 'macOS', 'Linux']
print(os)
os.reverse()
print(os)


# list comprehesion
a = [1,2,3,4,5,6,7,8,9,10]
[x**2 if x%2 == 0 else x**3 for x in a]
[x**2 for x in a if x%2 == 0]
a = [[4,5,6],[1,2,3]]
l=[]
[l.append(y) for x in a for y in x]
[l.append(y) for x in a for y in x if y!=3]     # [4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2]
a = [[1,2,3],[4,5,6]]
[[y**2 if y%2 == 0 else y**3 for y in x] for x in a if isinstance(x,list)]

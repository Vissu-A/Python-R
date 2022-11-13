#NOTE:- 'for' loop in python is used to iterate over a sequence(list,tuple,string) or other iterable objects

# adding numbers in range(0,10)
a=[0,1,2,3,4,5,6,7,8,9]
sum=0
for v in a:
    sum=sum+v
print(sum)
print()

#adding even numbers in range(0,10)
sum=0
for v in range(0,10,2):
    sum=sum+v
print(sum)
print()

#adding odd numbers in range(0,10)
sum=0
for v in range(1,10,2):
    sum=sum+v       #1+3+5+7+9=25
print(sum)
print()

genre = ['pop', 'rock', 'jazz','bass','live','club','theater']
print(len(genre))

for i in genre:
    print(i)
print()

# iterate over the list using index
genre = ['pop', 'rock', 'jazz','bass','live','club','theater']
print(len(genre))
for i in range(len(genre)):
    print(genre[i])
print()


# iterate over the list using index to get elements b/w specified indexes
genre = ['pop', 'rock', 'jazz','bass','live','club','theater']
print(len(genre))
for i in range(1,len(genre)-1):
    print(genre[i])
print()



# iterate over the list using index to get even index elements
genre = ['pop', 'rock', 'jazz','bass','live','club','theater']
print(len(genre))
for i in range(0,len(genre),2):
    print(genre[i])
print()


# iterate over the list using index to get odd index elements
genre = ['pop', 'rock', 'jazz','bass','live','club','theater']
print(len(genre))
for i in range(1,len(genre),2):
    print(genre[i])
print()
#tuple is one of the sequence datatypes in python,used to represent group of elements as a single entity
#the elements may be homogenious/hetrogenious or other sequences(list,set,dictionary,string)

#Diff b/w List and Tuple:
a=[10,12,15,'python','avengers',11.7]
b=(10,12,15,'python','avengers',11.7)
import sys
print(sys.getsizeof(a))
print(sys.getsizeof(b))
#size of a(list) > size of b(tuple)

import timeit
print(timeit.timeit(stmt='[2,3,4,5,6,7,8,9,10,11]', number=10))
print(timeit.timeit(stmt='(2,3,4,5,6,7,8,9,10,11)', number=10))
#time for creating list > time for creating tuple

#From the above example we can say that
#1.tuple is more memory efficient than the list
#2.tuple is more time efficient than the list
#3.iterating over the tuple takes less time than the list so,performance is boosted slightly
#4.tuple uses immutable memory,where as list uses mutable memory


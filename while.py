i=0
while(i<10):
    print(i)

#when we run the above program it will leads to infinate loop, Because there is no chance to fail the condition, Because for every iteration the 'i' value
#is zero(0), Because we are not incrementing the 'i' value

#NOTE:- so,when we are working with 'while' loop we have to takecare/check about occurrence of infinate loop


i=0
while(i<10):
    print(i)
    #i++    # this will not work in python
    i+=1
#'BREAK','CONTINUE','TRY','EXCEPT' AND 'PASS'

#We can use 'break'/'continue' with loops(while,for) only,we cann't use 'break'/'continue' with conditional statements(if,elif,else),But inside the loops
#we write 'break'/'continue' with conditional statements

#'break' statement
a=[0,1,2,3,4,5,6,7,8,9]
for i in a:
    print(i)
    if(i==5):
        break
print()

b='string'
for val in b:
    if val == "n":
        break
    print(val)
print()                 #just printing a line space


b='vissu'
for val in b:
    if val == "s":
        break
    print(val)
print()                 #just printing a line space


#we cann't use 'break'/'continue' with conditional statements(if,elif,else) directely,(i.e without using loops/without writing them in loop)
i=0
if(i<7):
    i+=1
    print(i)
    if(i==5):pass         #here 'pass' will create empty if without body
        #break/continue   #error
print()                   #just printing a line space


#but we can use 'break' or 'continue' with loop's nested-if
i=int(input('enter any number'))
while(i!=0):
 if(i<7):
    i-=1
    print(i)
    if(i==5):
        break
print()


#'continue' statement
b='string'
for val in b:
    if val == "n":
        continue
    print(val)
print()                 #just printing a line space

b='vissu'
for val in b:
    if val == "s":
        continue
    print(val)
print()

#'try' and 'catch' are used to handle exceptions,we learn more about these statements in exception handiling

#'pass' statement is used to create an empty class,method,loop or conditional statement without body

x=range(10)
n=10
class a:pass       #empty class
def add(x,y):pass  #empty method
for i in x:pass    #empty loop
if(i>x):pass       #empty conditional statement
if(i>n):pass       #empty conditional statement
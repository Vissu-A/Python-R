#CONVERTING INTO int

#Case: float to int
a=10.5
print(a)
print(type(a))
b=int(a)
print(b)
print(type(b))
#Case: string to int

#Type:1
ab='10'
print(ab)
print(type(ab))
ac=int(ab)
print(ac)
print(type(ac))

#Type:2
c='11.5'
print(c)
print(type(c))
#d=int(c)              #error: invalid literal for int()with base 10:'11.5'
#solution
e=int(float(c))
print(type(e))

#Case: complex to int
f=5+7j
print(f)
print(type(f))
#g=int(f)               #error: can't convert (complex - int),NOTE:- reverse(int - complex) is possible


#Case: binary integer to decimal integer
print(int('0100',2 ))                         #(0*2**0+0*2**1+1*2**2+0*2**3)=(0+0+1*4+0=0+0+4+0)=4
print(int('0101',2))
print(int('1000',2))

#Case: octal integer to decimal integer
print(int('777',8))                          #(7*8**0+7*8**1+7*8**2)=(7*1+7*8+7*64)=(7+56+448)=511
print(int('76543210',8))

#case: hexadecimal integer to decimal integer
print(int('37Af',16))
print(int('7Af',16))
print(int('3A',16))                   #a=10 in hexadecimal---(10*16**0+3*16**1)=(10*1+3*16)=(10+48)=58
print(int('0954a',16))
print(int('034689AF',16))

#Case: fuctions(bin,oct,hex)
i=10
print(i)
print(type(i))

bi=bin(i)           #Gives i in binary form(converts integer(i) into binary string)
print(bi)
print(type(bi))     #type is 'str'

oc=oct(i)           #Gives i in octal form(converts integer(i) into octal string)
print(oc)
print(type(oc))     #type is 'str'

he=hex(i)           #Gives i in hexadecimal form(converts integer(i) into hexadecimal string)
print(he)
print(type(he))     #type is 'str'


#CONVERTING INTO float

#Case: int to float
print(float(15))        #o/p: 15.0

#Case: str to float
print(float('57'))
print(float('27.5'))

#Case: complex to float
u=3+2j
print(u)
print(type(u))

#v=float(u)                 #error: can't convert (complex - float),NOTE:- reverse(float - complex) is possible


#CONVERTING INTO string(str)
#Case: int to str
n=10
print(n)
print(type(n))

m=str(n)
print(m)
print(type(m))

#Case: float to str
p=11.7
print(p)
print(type(p))

q=str(p)
print(q)
print(type(q))

#Case: complex to str
co=5+3j
print(co)
print(type(co))

cs=str(co)
print(cs)
print(type(cs))

#CONVERTING INTO complex=(real+imag*1j),imag is optional and default value of imag is '0'
#Case: int to complex
c1=5
c2=7
c3=complex(c1,c2)
print(c3)
print(type(c3))
c4=complex(c2)    #2nd argument is optional,if not specified default value '0' will be taken
print(c4)
print(type(c4))

#Case: float to complex
print(complex(11.5))
print(complex(11.5,3.5))
print(complex(10,5j))
print(complex(5,10j))


#CONVERTING INTO bool
#Case: int to bool
b1=10
print(b1)
print(type(b1))

b2=bool(b1)
print(b2)
print(type(b2))
if(b2):
    print('Hello')
print(b2)
print(type(b2))
if(b1):
    print('Hi')
print(b1)

#Case: float to bool
f1=15.7
print(f1)
print(type(f1))

f2=bool(f1)
print(f2)
print(type(f2))

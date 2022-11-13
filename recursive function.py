#recursive function is nothing but a function that calls itself with in the function body one or more number of times

#Example 1: finding factorial of the give number
import time
import sys

def fact(n):
    if n == 1:
        return 1
    else:
        return (n * fact(n-1))

t1 = time.time()
print('Time before calling the function:',t1)
print()

r = fact(int(input('Enter your number\n')))

print('Default maximum recursion limit in python3:',sys.getrecursionlimit())

print()

print('Time after calling the function:',time.time())
print()

print('Time taken to complete the function:',time.time()-t1)
print()

print(r)
print()



#Example 2:checking given string is a pallendrome or not " using recursion "
def palindrome(s):
    print(s)
    length = len(s) if s else 0
    if length <= 1:
        return True
    elif length == 2:
        if s[0] == s[1]:
            return True
        else:
            return False
    elif s[0] == s[-1]:
        print(s)
        return palindrome(s[1:-1])
    else:
        return False

st = time.time()
print('Time before calling the function:',st)
print()

print('Overwriting the default recursion limit:',sys.setrecursionlimit(10))

res = palindrome(input('Enter your string\n'))
print('Default maximum recursion limit',sys.getrecursionlimit())
print()

print('Time after calling the function:',time.time())
print()

print('Time taken to complete the function:',time.time() - st)
print()

print(res)
print()



#Example 3:checking given string is a pallendrome or not " without using recursion "
def pal(x):
    if x == x[-1::-1]:
        return True
    else:
        return False

sta = time.time()
print('Time before calling the function:',sta)
print()

z = pal(input('Enter your string\n'))
print()

print('Time after calling the function:',time.time())
print()

print('Time taken to complete the function:',time.time() - sta)
print()

print(z)

# NOTE-1 : recursive function takes less execution time rather than the normal function

# NOTE-2 : when ever we use recursion we should have clear idea about terminating the recursion otherwise it's leads to infinate recursion
# which is nothing but (stack overflow: the space needed to store the variables and information associated with each function call is more
# than can fit on the stack)


# simple example to infinate recursive function
import sys
print(sys.getrecursionlimit())
def add(a):
    return add(a+1)     #RecursionError: maximum recursion depth exceeded
b = add(0)
print(b)

# NOTE-3 : when ever we use recursion size of the code is increased but,execution time is less as seen in above examples 2 and  3

# NOTE-4 :Debugging/tracing the recursive functions is difficult
import threading
import time

# creating thread:
     # syntax:
         # threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)

t = threading.Thread()# thread 't' is created with all arguments triggered with default value 'None',because we didn't pass any arguments while creating it
                      # Thread is nothing but a class,'Thread()' means creating object for the Thread class. while creating object for the class in python
                      # '__init__' constructor/function will be called

    # constructor in Thread class
               # def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):



# starting a thread:
      # synatx:
            # thread.start()

t.start()       # we can call start() at most once per one thread object/thread, otherwise it will raise "RuntimeError"
#t.start()      # RuntimeError: threads can only be started once

# Note: when ever we call the "start()" method, internally Thread class object's(i.e, t) "run()" method will be invoked


def addition(x,y):
    print(time.time(),threading.currentThread().name,'going to sleep for 1sec')
    time.sleep(1)
    print(time.time(),'addition result:',x+y)

def subtraction(x,y):
    print(time.time(),threading.currentThread().name,'is picked up')
    print(time.time(),'subtraction result:',x-y)

def multipcation(x,y):
    print(time.time(),threading.currentThread().name,'going to sleep for 2sec')
    time.sleep(2)
    print(time.time(),'multipication result:',x*y)


t1 = threading.Thread(target=addition,args=(5,7),name='Thread-add')
t2 = threading.Thread(target=subtraction,args=(5,7),name='Thread-sub')
t3 = threading.Thread(target=multipcation,args=(7,5),name='Thread-mul')

t1.start()
t2.start()
t3.start()
t3.join()
print()
print('\n')


# Note: if we don't want to start a new thread until the current thread is terminated then,use "join()" method
# join():
     # syntax:
          # join(x)
               # x = time to be wait upto

def addition1(x,y):
    print(time.time(),threading.currentThread().name,'going to sleep for 1sec')
    time.sleep(1)
    print(time.time(),'addition result:',x+y)

def subtraction1(x,y):
    print(time.time(),threading.currentThread().name,'is picked up')
    print(time.time(),'subtraction result:',x-y)

def multipcation1(x,y):
    print(time.time(),threading.currentThread().name,'going to sleep for 2sec')
    time.sleep(2)
    print(time.time(),'multipication result:',x*y)


t4 = threading.Thread(target=addition1,args=(5,7),name='Thread-add')
t5 = threading.Thread(target=subtraction1,args=(5,7),name='Thread-sub')
t6 = threading.Thread(target=multipcation1,args=(7,5),name='Thread-mul')

t4.start()
t4.join()
t5.start()
t5.join()
t6.start()
t6.join()

print('\n','\n')


# creating a daemon thread

# type1:
th1 = threading.Thread(daemon=True)
print(th1.isDaemon())                    # True

# type2: making a non-daemon thread as daemon thread
th2 = threading.Thread()
print(th2.isDaemon())                    # False
th2.setDaemon(True)
print(th2.isDaemon())                    # True
import threading

# synchronizing threads: in python thread synchronization is achived by using Lock,Condition

# Using Lock():

# lock = threading.Lock()  # creating lock object

# lock.acquire()           # locking the thread/making the thread as synchronized thread

# lock.release()           # releasing the thread


def myfun(x,y):

    while y < 10:
        print(threading.currentThread().name, 'non-sync code', y)
        y += 1
    while x < 10:
        lock.acquire()
        print(threading.currentThread().name,'sync code',x)
        x += 1
        lock.release()


lock = threading.Lock()                           # creating lock object

thr1 = threading.Thread(target=myfun,args=(1,1))
thr2 = threading.Thread(target=myfun,args=(1,1))
thr1.start()
thr2.start()

print('\n','\n')



# Using Condition():

# con = threading.Condition()             # creating Condition object

# Consumer function:

# con.acquire()                           # locking the thread/synchronizing the thread
# while not an_item_is_available():       # checking wather item is available or not to consume by the consumer
# con.wait()                              # waiting if item is not available to consume
# consume an available item               # consuming the item produced by the producer
# con.release()                           # releasing the lock/thread


# Producer function:

# con.acquire()                           # locking the thread/synchronizing the thread
# make an item available                  # producing item to consume by the consumer
# con.notifyAll()                         # notifying to all consumers after producing the item
# con.release()                           # releasing the lock/thread



li = []
def consumer(cv):
    print(threading.currentThread().name, 'started')
    cv.acquire()
    print(threading.currentThread().name,'acquired the lock')
    if len(li) == 0:
        print(threading.currentThread().name,'wating for the item to consume')
        cv.wait()
    print(threading.currentThread().name,'consumed the item:',li.pop())
    cv.release()


def producer(cv):
    print(threading.currentThread().name,'started')
    cv.acquire()
    print(threading.currentThread().name, 'acquired the lock')
    for i in range(10):
        print('producing',i,'to consume')
        li.append(i)

    cv.notify()          # notifies only one thread
    cv.notifyAll()       # notifies all threads
    cv.release()


con = threading.Condition()

cs1 = threading.Thread(name='consumer1', target=consumer, args=(con,))
cs2 = threading.Thread(name='consumer2', target=consumer, args=(con,))
pd = threading.Thread(name='producer', target=producer, args=(con,))

cs1.start()
cs2.start()
pd.start()
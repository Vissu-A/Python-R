i=0
while(i<10):
    print('inside while')
    i+=1
else:
    print('inside else\n')


i=0
while(i<10):
    print('inside while')
    i+=1
    print(i)
    break
else:
    print('inside else')


#NOTE:- else block is executed when 'while' loop is terminated by itself(i.e by faliing the condition)
#else block is not execute if we terminate 'while' loop by using 'break' statement
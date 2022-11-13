import sys
import time

file1 = sys.argv[1]
file2 = sys.argv[2]
outfile = sys.argv[3]

t1 = time.time()
with open(file1, 'r') as f1:
    list1 = f1.readlines()
with open(file2, 'r') as f2:
    list2 = f2.readlines()

def minus(*args):
    dic1 = dict.fromkeys(args[0], 'dummy')
    dic2 = dict.fromkeys(args[1], 'dummy')
    
    rs = []
    
    if(args[3] == 1):
        rs = [email for email in dic1.keys() if email not in dic2.keys()]
    
    elif(args[3] == 2):
        rs = [email for email in dic2.keys() if email not in dic1.keys()]
    
    with open(args[2], 'w') as f3:
        [f3.write(str(line).strip('\n')+'\n')  for line in rs]

    print(file1+':'+str(len(args[0])) + ' emails'+', ' + file2+':'+str(len(args[1])) + ' emails' + ', ' + outfile +':' + str(len(rs)) + ' emails' + ',' + ' Time taken: '+str(round(time.time()-t1)) + ' seconds')


choise = ''

while True:
    print('1. Enter 1 for L1 - L2'+'\n'+'2. Enter 2 for L2 - L1')
    choise = int(input('Please Enter your option:'+'\n'))
    
    if(choise in [1, 2]):
        break
    else:
        print('Invalid choice!')
        continue
minus(list1, list2, outfile, choise)
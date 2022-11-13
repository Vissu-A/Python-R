import sys
import time

file1 = sys.argv[1]
file2 = sys.argv[2]
outfile = sys.argv[3]

def union(*args):
    t1 = time.time()
    with open(args[0], 'r') as f1:
        l1 = f1.readlines()
    with open(args[1], 'r') as f2:
        l2 = f2.readlines()
        
    dic = dict.fromkeys((l1 + l2), 'dummy')
    
    with open(args[2], 'w') as f3:
        [f3.write(str(line).strip('\n')+'\n')  for line in dic.keys()]
        # for line in dic.keys():
            # f3.write(str(line).strip('\n')+'\n')     

    print(file1+':'+str(len(l1)) + ' emails'+', ' + file2+':'+str(len(l2)) + ' emails' + ', ' + outfile +':' + str(len(dic)) + ' emails' + ',' + ' Time taken: '+str(round(time.time()-t1)) + ' seconds')
    
union(file1, file2, outfile)
import sys
import time

file1 = sys.argv[1]
file2 = sys.argv[2]
outfile = sys.argv[3]

def interset(*args):
    t1 = time.time()
    with open(args[0], 'r') as f1:
        l1 = f1.readlines()
    with open(args[1], 'r') as f2:
        l2 = f2.readlines()
        
    dic1 = dict.fromkeys(l1, 'dummy')
    dic2 = dict.fromkeys(l2, 'dummy')
    
    inli = [email for email in dic1.keys() if email in dic2.keys()]
    
    with open(args[2], 'w') as f3:
        [f3.write(str(line).strip('\n')+'\n')  for line in inli]

    print(file1+':'+str(len(l1)) + ' emails'+', ' + file2+':'+str(len(l2)) + ' emails' + ', ' + outfile +':' + str(len(inli)) + ' emails' + ',' + ' Time taken: '+str(round(time.time()-t1)) + ' seconds')
    
interset(file1, file2, outfile)
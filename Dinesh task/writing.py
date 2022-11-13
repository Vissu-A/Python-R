import random
import time
t1 = time.time()

emli1 = ['abc@gmail.com', 'xyz@gmail.com', 'pqr@gmail.com', 'zmr@gmail.com', 'xuv@gmail.com']
emli2 = ['abc@gmail.com', 'xyz@gmail.com', 'tuv@gmail.com', 'hornet@gmail.com', 'xuv@gmail.com']

with open("L1.txt", "w") as f:
  for i in range(200000):
    for email in emli1:
      f.write(email+'\n')

with open("L2.txt", "w") as f:
  for i in range(200000):
    for email in emli2:
      f.write(email+'\n')
      
print(time.time() - t1)
digits = [0,1,2,3,4,5,6,7,8,9]

for i in digits:
    print(i)
    #if(i==1):
     # break
else:
    print("No items left.\n")


for i in digits:
    print(i)
    if(i==3):
      break
else:
    print("No items left.")

#NOTE:-the else block is executed only when 'for' loop is terminated itself without using the break statement inside the loop
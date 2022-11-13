f = open(r'c:\Users\Vissu\Desktop\fi ope files.txt','w') #This will opens file for writing,if file not exists it creates a new one,if file exists
                                                                                                                            #overwrites it
f.write("hi")
f.close()

f = open(r'c:\Users\Vissu\Desktop\fi ope files.txt','w')
f.write('hello')
f.close()

f = open(r'c:\Users\Vissu\Desktop\fi ope files.txt','w')
f.write('Hello World\n')    #\n ---> New line
f.write('I am Chitti\n')
f.write('Speed 1 terahertz'+ "\t" +'memory 1 zitabyte \n')  #\t ---> Tab space
f.flush()                                                   #This will flush the data present in the buffer to the file
f.close()

lines = ['I am an Andro Humanoid Robot\n','I can do what man can do\t','also what man cann\'t do\n']

f = open(r'c:\Users\Vissu\Desktop\fi ope files.txt','a')  #opening file with append mode,old content is not vanished
#f.write(l for l in lines)                                #TypeError: write() argument must be str, not generator
f.writelines(l for l in lines)                            #writing lines by iterating over the generator
f.flush()                                                 #This will flush the data present in the buffer to the file
f.close()

f = open(r'c:\Users\Vissu\Desktop\fi ope files.txt','r')
print(f.read())                                           #Reads total line in the file at a time
f.close()

f = open(r'c:\Users\Vissu\Desktop\fi ope files.txt','r')
print(f.readline())                                       #Hello World ( Reads one line only at a time )
print(f.readline())                                       #I am Chitti
f.close()

f = open(r'c:\Users\Vissu\Desktop\fi ope files.txt','r')
print(f.readlines())                          #Read all lines at atime and gives the output in a list,iterate over the list to get line by line
f.close()
print()

#tell() and seek()

#tell() ---> tell() will not take any arguments
    #syntax:
         #file.tell() ---> returns the current position of the file pointer within the file.
f = open(r'c:\Users\Vissu\Desktop\fi ope files.txt','r')
print(f.tell())                                          # 0
print(f.readline())                                      #Hello World(12 includes \n)
print(f.tell())                                          #13
print(f.readline())                                      #I am Chitti

# To reset file pointer position we use seek() function
#seek() ---> seek() will take two arguments
    #syntax:
        #file.seek(x,y)
            # x = position to set file pointer
            # y = if 0(starting of the file), if 2(ending of the file), if 1(current position)

print(f.seek(0,0))
print(f.readline())
print(f.seek(6,0))
print(f.readline())
print(f.seek(0,2))
print(f.readline())    # Empty because end of the file
print(f.tell())
print(f.seek(0,0))
print(f.readline())

#closed ---> returns 'True' if file is closed,otherwise returns 'False'
print(f.closed)    # False
f.close()
print(f.closed)    # True
print()

print(f.name)      # Gives the file name
print()

print(f.mode)      # Gives mode of the file
print()

# Another way to open a file using 'With'
with open(r'c:\Users\Vissu\Desktop\fi ope files.txt','r') as f:
    print(f.read())

# File copying in python
with open(r'c:\Users\Vissu\Desktop\fi ope files.txt','r') as f:
    with open(r'c:\Users\Vissu\Desktop\fi ope files copy.txt','w') as f1:
        f1.writelines(f.readlines())
        #f1.write(f.readlines())             #TypeError: write() argument must be str, not list
f1.close()
f.close()

# Reading and Writing image files using 'rb' mode
with open('Iron man.png','rb')as png:
    with open ('iron man copy.png','wb')as png1:
        png1.write(png.read())
    png1.close()
png.close()

with open('SPACE.JPG','rb') as jpg:
    with open('space copy.jpg','wb') as jpg1:
        jpg1.write(jpg.read())
    jpg1.close()
jpg.close()
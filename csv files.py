import csv

# csv.writer() ---> used to write a csv file, csv.writer() will take 3 arguments

    # syntax:

         # csv.writer(csv file object, dialect='dialect name(Default is "excel")', **fmtparams)

            # csv file object = file to be write
            # dialect name = dialect to be used while writing the file (By default dialect is " excel ")
            # **fmtparams = format parameters, that will overwrites those specified in the dialect

# Note:- While we are opening the file with ' W ' mode we must use " newlines='' "


# csv.register_dialect() ---> used to define custom dialect

     #syntax:

           # csv.register_dialect('dialect name', delimiter, lineterminator, escapechar, doublequote, quotechar, quoting, skipinitialspace)

               # delimiter = 'delimiter to be use'             (Default value is ',')
               # lineterminator = 'lineterminator to be use'   (Default value is '\r\n')
               # escapechar = 'escapechar to be use'           (Default value is 'None')  i.e, escapechar=''
               # doublequote = True/False                      (Default value is 'True')
               # quotechar -------------->                     (Default value is '"')
               # quoting ---------------->                     (Default value is 'QUOTE_MINIMAL')
               # skipinitialspace = True/False                 (Default is 'False')


# csv.reader() ---> used to read a csv file, csv.reader() will take 3 arguments

     # syntax:

            # csv.reader(csv file object, dialect='dialect name', **fmtparams)

                 # csv file object = file to be read
                 # dialect name = dialect to be used while reading the file (By default dialect is " excel ")
                 # **fmtparams = format parameters, that will overwrites those specified in the dialect



# Writing a csv file

            # Case:1 using default dialect 'excel'

data = [['roll no','stu name','course','fee'],[1,'vissu','python',3000],[2,'kiran','python',3000],[3,'kumar','bigdata',5000],
        [4,'harika','java',2000],[5,'suresh','python',3000],[6,'charan','bigdata',5000],[7,'harshita','python',3000]]

with open('stu.csv','w',newline='') as f:
    w =csv.writer(f)
   #w.writerow(data)    # writerow() ---> will write entire data as one line
    w.writerows(data)
f.close()


            # Case:2 using custom defined dialect

data = [['roll no','stu name','course','fee'],[1,'vissu','python',3000],[2,'kiran','python',3000],[3,'kumar','bigdata',5000],
        [4,'harika','java',2000],[5,'suresh','python',3000],[6,'charan','bigdata',5000],[7,'harshita','python',3000]]

csv.register_dialect('mydialect',delimiter='\t',lineterminator='\r\n',escapechar='',doublequote=False,quotechar='#',quoting=csv.QUOTE_ALL,skipinitialspace=False)

with open('stu copy.csv','w',newline='') as f:
    w =csv.writer(f,dialect='mydialect')
    w.writerows(data)
    f.close()
print()



# Reading a csv file

           # Case:1 having default dialect 'excel'

with open('stu.csv','r',newline='') as f:
    r = csv.reader(f)
    for x in r:
        print(x)
print()

          # Case:2 having custom defined dialect 'mydialect'

with open('stu copy.csv','r',newline='') as f:
    r = csv.reader(f,'mydialect')
    for x in r:
        print(x)
print()




# get_dialect()                                  Return the dialect object associated with name

print(csv.get_dialect('mydialect'))              # <_csv.Dialect object at 0x0000017A966BE110>
print()

# list_dialects()                                Return a list of all know dialect names

print(csv.list_dialects())                       # ['excel', 'excel-tab', 'unix', 'mydialect']
print()
#print(csv.list_dialects('mydialect'))           # TypeError: list_dialects() takes no arguments (1 given)

# field_size_limit()              # Sets an upper limit on parsed fields,and also Returns old limit [ If limit is not given, no new limit is
                                                                                                     #set and the old limit is returned]
print(csv.field_size_limit())       # 131072
#print(csv.field_size_limit(100))    # sets limit to 100 ans returns old limt = 131072
print(csv.field_size_limit())       #100
print()
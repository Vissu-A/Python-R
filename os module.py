import os

print(dir(os))            # This displays all functions in os module
print()

print(os.getcwd())        # E:\Pro\Python  ( gives current working directory)
print()

#print(os.chdir('C:\Users\Vissu\Desktop'))    #SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

print(os.chdir(r'C:\Users\Vissu\Desktop'))    #changes the current working directory path to the specified directory path and returns 'None'
print(os.getcwd())                            #C:\Users\Vissu\Desktop ( changed directory path )
print(os.chdir(r'E:\Pro\Python'))
print(os.getcwd())
print()

print(os.mkdir('test'))                         #creates 'test' directory in current working directory and returns None
print(os.mkdir(r'C:\Users\Vissu\Desktop\test')) #creates 'test' directory in specified path and returns None
                                                #FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'test'

print(os.makedirs('test\demo\osmodule'))        #creates test\demo\osmodule directiories in current working directory
print(os.makedirs(r'C:\Users\Vissu\Desktop\test\demo\osmodule')) #creates test\demo\osmodule directiories in specified path location


print(os.listdir())                             #gives [all files in current working directory] i.e,['.idea', 'for.py', 'datatypes.py',.........]
print(os.listdir(r'C:\Users\Vissu\Desktop'))    #gives list of all files in specified path
print()

print(os.rename('test','practice'))             #changes the name of a file/directory from old name to new name
print(os.renames('test','newdir/practice'))    #changes name of file/directory from old name to new name and moves it into'newdir' directory
print()

print(os.remove('test'))     #PermissionError: [WinError 5] Access is denied: 'test', because remove() can delete files only not directories
print()

print(os.remove('abc.txt'))  #Deletes abc.txt file ,remove() will deletes only files
print()                      #if file is not there returns FileNotFoundError: [WinError 2] The system cannot find the file specified: 'abc.txt'

print(os.rmdir('test'))      #rmdir() will delete 'test' directiory, But it should be empty directory otherwise error
print()                      #if file is not there returns FileNotFoundError: [WinError 2] The system cannot find the file specified: 'test'

print(os.rmdir('test\demo\osmodule'))  #removes only 'osmodule' directory if it is empty,otherwise OSError:The directory is not empty
print(os.removedirs('test\demo\osmodule')) #removes all directories recursively if they are empty,otherwise OSError:The directory is not empty
print()

# To delete non-empty directory
import shutil
print(shutil.rmtree('test'))     #Deletes non-empty directory 'test'
print()

#os.walk()
#syntax:
    #os.walk(top,topdown=True,onerror=None,followlinks=False)
        #top = directory path to be walk(must and should we have to pass this argument while calling walk() function)
        #if topdown is set to True directories are scanned from 'Top-Down'
        #if topdown is set to False directories are scanned from 'Bottom-up'
        #onerror by default set to 'None'
        #followlinks by default set to 'False'

c = os.walk('.')   # '.' Dot means current working directory
print(c)           #<generator object walk at 0x000001DE2731B0A0>
print(next(c))


#os.path methods

#os.path.commompath() ---> takes sequence of paths (i.e, [paths]/(paths)) and returns the common path in the sequence of paths
os.path.commonpath([r'C:\Users\Vissu\Desktop\test1',r'C:\Users\Vissu\Desktop\test2\demo2'])   #'C:\\Users\\Vissu\\Desktop'
os.path.commonpath((r'C:\Users\Vissu\Desktop\test1',r'C:\Users\Vissu\Desktop\test2\demo2'))   ##'C:\\Users\\Vissu\\Desktop'

#os.path.curdir
os.chdir(r'C:\Users\Vissu\Desktop')
os.path.curdir                          # '.'
os.getcwd()                             # 'C:\\Users\\Vissu\\Desktop'
os.path.abspath(os.path.curdir)         # 'C:\\Users\\Vissu\\Desktop'
os.path.abspath('.')                    # 'C:\\Users\\Vissu\\Desktop'

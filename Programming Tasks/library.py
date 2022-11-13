class library:
    def __init__(self,books):
       self.books = books.split(',')
    def addbook(self,book):
        self.books.extend(book.split(','))
    def display(self):
        print(self.books)
    def rmbook(self,book):
        for x in book.split(','):
            self.books.remove(x)
class customer(library):
    def __init__(self):
        pass
    def barbook(self,book):
        self.takenbooks = book.split(',')
    def subbook(self,book):
        self.books = book.split(',')
lib = library(input('Enter the book names you want to include \n'))
con = input('Do you want to continue:yes/no')

while con in ('yes','y'):
    choice = int(input('Enter 1 for barrow a book\nEnter 2 for submit a book\n'))
    if choice == 1:
        if len(lib.books) != 0:
            cus = customer()
            lib.display()
            book = input('Enter the books what do you want \n')
            cus.barbook(book)
            print('selected books:',cus.takenbooks)
            lib.rmbook(book)
            lib.display()
            con = input('Do you want to continue:yes/no \n')
        else:
            print('No books are availabile right now \n please contact after some time')
            con = input('Do you want to continue:yes/no \n')
    elif choice == 2:
        book = input('Enter the books what do you want to submit \n')
        cus.subbook(book)
        print('submited books',cus.books)
        lib.addbook(book)
        lib.display()
        con = input('Do you want to continue:yes/no \n')
    else:
        print('Invalid choice')
import cx_Oracle as co
class library:
    def __init__(self,books):
       self.books = books.split(',')
       con = co.connect('system/vissu@localhost')
       cur = con.cursor()
       sql = 'insert into lib values(\'{0}\')'
       for x in self.books:
           #cur.execute('insert into lib values(\'%s\')'%x)
           sql1 =sql.format(x)
           cur.execute(sql1)
       con.commit()
       con.close()

    def fetchdata(self):
        con = co.connect('system/vissu@localhost')
        cur = con.cursor()
        cur.execute('select *from lib')
        return cur.fetchall()
        #for y in cur:
            #return y
lib = library(input('Enter the books want to include \n'))
data = lib.fetchdata()
print(data)
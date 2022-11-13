import cx_Oracle as co

con = co.connect('system/vissu@localhost')
print(con.version)
cur = con.cursor()
cur.execute('create table student(rno int,name varchar2(17),course varchar2(17),fee int)')
#for x in cur:
    #print(x)
#con.close()
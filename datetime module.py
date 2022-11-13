from datetime import datetime

#strptime ('given date','format of the given date')
    # converts 'string type date' into 'datetime type'

    # strptime = string parse time

d = '30-06-93'
print(type(d))
c = datetime.strptime(d, "%d-%m-%y")
print(c)
print(type(c))


#strftime ('given date','in which format to be convert')
    # converts the given date format into specified date format
    # given date should be 'datetime.date' object but not a 'str'

d = '06-30-93'
#e = datetime.strftime(d,'%d:%m:%y')    # TypeError: descriptor 'strftime' requires a 'datetime.date' object but received a 'str'
#print(E)

e = datetime.strftime(datetime.strptime(d,'%m-%d-%y'),'%d:%m:%y')
print(e)
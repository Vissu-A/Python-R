import json         # json = java script object notation


# Converting python objects into Json objects

 # 1.dump()
    # json.dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)

 # 2.dumps()
    # json.dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, default=None, sort_keys=False, **kw)



# dump(): dump is used whenever we want to write converted Json object into a file
    # dump(x,y)
          # x = python object
          # y = file to write


data = {'user1': '1629','user3': '1675','user4': '2042','user2':'1256','user5':'1236','user7':'5845','user6':'2358'}
f = open('result.json','w')
#json.dump(data)                                # TypeError: dump() missing 1 required positional argument: 'fp'
json.dump(data,f)
f.close()
        #(or)
with open('resultcopy.json', 'w') as f1:
    json.dump(data, f1)


# writing converted Json object into a file with sorting the keys

data = {'user1': 1629,'user3': 1675,'user4': 2042,'user2':1256,'user5':1236,'user7':5845,'user6':2358}
f_key_ord = open('result sortedkey.json','w')

json.dump(data,f_key_ord, sort_keys=True)
f_key_ord.close()


# dumps(): dumps is used whenever we want to write converted Json object into a variable/not want to write into a file
    #dumps(x)
       # x = python object


data = {'user1': 1629,'user3': 1675,'user4': 2042,'user2':1256,'user5':1236,'user7':5845,'user6':2358}
print(type(data),'\n')

#rdata = json.dumps(data,f)                     # TypeError: dumps() takes 1 positional argument but 2 were given
rdata = json.dumps(data)
rdatacopy = json.dumps(data,sort_keys=True)     # sorting the keys

print(rdata,'\n')
print(rdatacopy,'\n')

print(type(rdata),'\n')
print(type(rdatacopy),'\n')


#Converting Json objects into python objects

 # 1.load()
   # json.load(fp, *, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

 # 2.loads()
   # json.loads(s, *, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)




# load(): whenever we want to convert Json object which is stored in a file into python object then,we will use load()

with open('result.json','r') as rf:

    po = json.load(rf)
    print(po)
    print(type(po))



# loads(): whenever we want to convert Json object which is stored in a variable into python object then,we will use load()
po1 = json.loads(rdata)
print(po1)
print(type(po1))
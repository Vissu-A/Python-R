#string functions
a = 'hello'

#capitalize:
#string.capitalize() ----->returns a copy of string making 1st letter of string as uppercase remaing letters as lowercase
print(a.capitalize())
print(a)
print()

#casefold:
#string.casefold() ------->returns a version (or) copy of string suitable for caseless comparision(i.e it ignores the case when comparing)
b = 'HELLO'
print(a == b)
print(b.casefold())
print(a.casefold() == b.casefold())
print()

#center:
#string.center(width,'fillchar') fillchar is optional,by default fillchar is space
#this will gives a copy of string by moving it to the center of the specified width and starting and ending of the string is filled by fillchar
print(len(a))
print(a.center(11))
print(a.center(11,'@'))
print(len(a.center(11,'@')))
#NOTE:- if your actual string width(or)length is greaterthan or equal to specified width then,ther won't be any change
print(a.center(3,'@'))
print(a.center(5,'@'))
print()
import re

a = "my name is nageswararao and fax is +91-1243234 and my phone is +91-8148586071 I am teaching python"



# 1. findall() ---> findall(pattern, string, flags=0), Return a list of all non-overlapping matches in the string.

print(re.findall(r'is',a,flags=re.I))        # ['is', 'is', 'is']
print('\n')



# 2. finditer() ---> finditer(pattern, string, flags=0), Return an iterator object

print(re.finditer(r'is',a,flags=re.I))       # <callable_iterator object at 0x00000242F167C550>

ito = re.finditer(r'is',a,flags=re.I)
print(ito.__next__())      # <_sre.SRE_Match object; span=(8, 10), match='is'>
print(ito.__next__())      # <_sre.SRE_Match object; span=(32, 34), match='is'>
print(next(ito))           # <_sre.SRE_Match object; span=(60, 62), match='is'>
#print(ito.__next__())     # StopIteration
print('\n')



# 3. match() ---> match(pattern, string, flags=0), Try to apply the pattern at the start of the string, returning a match object, or None if no match was found.

print(re.match(r'dog', 'dog cat dog',flags=re.I))             # <_sre.SRE_Match object; span=(0, 3), match='dog'>

print(re.match(r'is', 'my name is vissu',flags=re.I))         # None

print(re.match(r'is','is my name vissu',flags=re.I))          # <_sre.SRE_Match object; span=(0, 2), match='is'>

m = re.match(r'is','is my name vissu',flags=re.I)
print(m.group(0))                                             # is
print('\n')



# 4. serach() ---> search(pattern, string, flags=0), Scan through string looking for a match to the pattern, returning a match object of 1st occurence, or None if no match was found

print(re.search(r'is',a,flags=re.I))    # <_sre.SRE_Match object; span=(8, 10), match='is'>
print('\n')



# 5. split() ---> split(pattern, string, maxsplit=0, flags=0), Split the source string by the occurrences of the pattern, returning a list

print(re.split(r'is',a,flags=re.I))     # ['my name ', ' nageswararao and fax ', ' +91-1243234 and my phone ', ' +91-8148586071 I am teaching python']
print(re.split(r'is',a,maxsplit=2,flags=re.I)) # ['my name ', ' nageswararao and fax ', ' +91-1243234 and my phone is +91-8148586071 I am teaching python']
print('\n')



# 6. sub() ---> sub(pattern, repl, string, count=0, flags=0), Return a copy of string by replacing the "pattren" with "repl" in the string

print(re.sub(r'91-\d{10}','91-7032176793',a,flags=re.I))
print('\n')



# 7. subn() ---> subn(pattern, repl, string, count=0, flags=0), Return a tuple containing (new_string, number).number = number of replacements we made

print(re.subn(r'91-\d{10}','91-7032176793',a,flags=re.I))
print('\n')
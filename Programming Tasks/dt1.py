d = {'a':10,'b':34,'A':7,'Z':3}
nd={k.lower():d.get(k.lower(),0)+d.get(k.upper(),0) for k in d.keys()}
print(nd)
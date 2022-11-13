arr = [1,9,60,7,-20,-30,5,7,9,-11,4]

sumarr = []
pa = []
for i in arr:
    if i > 0:
        pa.append(i)

    else:
        sumarr.append(sum(pa))
        # if sum(pa) != 0:
        #     sumarr.append(sum(pa))
        pa = []

sumarr.append(sum(pa))

sumarr.sort()
print(sumarr)
print('max sum is: ', sumarr[-1])
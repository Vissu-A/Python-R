def binarysearch(l,v,start,end):
    l.sort()
    if end >= start:
        mid = start+(end-start)//2

        if l[mid] == v:
            print('value founded at index:',mid)
        elif l[mid] > v:
            end = mid - 1
            binarysearch(l,v,start,end)
        elif l[mid] < v:
            start = mid + 1
            binarysearch(l,v,start,end)



l = [1,3,4,5,2,6,8,9,7,10]
binarysearch(l,7,0,len(l)-1)
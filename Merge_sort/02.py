def merges(a,b):
    i=0
    j=0
    res=[]
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            res.append(a[i])
            i+=1
        else:
            res.append(b[j])
            j+=1
    while i<len(a):
        res.append(a[i])
        i+=1
    while j<len(b):
        res.append(b[j])
        j+=1
    return res
a=[10,15]
b=[5,6,6,30,40]
print(merges(a,b))

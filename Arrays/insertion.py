def inserts(l, ele, pos):
    l.append(0)
    n=len(l)
    for i in range(n-1, pos, -1):
        l[i]=l[i-1]
    l[pos]=ele

l = [1,2,3,4,6]
inserts(l,5,4)
print(l)

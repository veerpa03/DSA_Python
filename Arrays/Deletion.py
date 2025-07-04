def dele(l, ele):
    for i in range(0, len(l)):
        if l[i]==ele:
            pos=i
    for i in range(pos, len(l)-1):
        l[i]=l[i+1]
    l.pop()




l = [1,2,3,4,6]
dele(l,1)
print(l)

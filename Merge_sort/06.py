# a = [2,20,20,40,60]
# b = [10,20,20,20]
# o/p => 20
def intersection(a,b):
    m=len(a)
    n=len(b)
    i=j=0
    while i<m and j<n:
        if (i>0 and a[i]==a[i-1]):
            i+=1
        if a[i]<b[j]:
            i+=1
        elif a[i]>b[j]:
            j+=1
        elif a[i]==b[j]:
            print(a[i])
            i+=1
            j+=1
    
a=[2,20,20,40,60]
b=[10,20,20,20]
intersection(a,b)
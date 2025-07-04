# l=[1,3,8,9,5,4]
# o/p -> l[1,3,4,9,5,8]
def part(a, l, h):
    pivot=a[h]
    j=l-1
    for i in range(l,h):
        if a[i]<pivot:
            j+=1
            a[j],a[i]=a[i],a[j]
    a[j+1],a[h]=a[h],a[j+1]

a=[1,3,8,9,5,4]
part(a, 0, 5)
print(a)
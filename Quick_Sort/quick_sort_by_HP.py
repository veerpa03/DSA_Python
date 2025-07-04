def partition(arr, l, h):
    pivot=arr[l]
    i=l-1
    j=h+1
    while True:
        i+=1
        while arr[i]<pivot:
            i+=1
        j-=1
        while arr[j]>pivot:
            j-=1
        if i>=j:
            return j
        arr[i],arr[j]=arr[j],arr[i]

def qs(arr, l, h):
    if l<h:
        p =partition(arr, l, h)
        print(p)
        qs(arr, l, p)
        qs(arr, p+1, h)
l=[8,4,7,9,3,10,5]
qs(l, 0, 6)
print(*l)
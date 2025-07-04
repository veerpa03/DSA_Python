def partition(arr, l, h):
    pivot = arr[h]
    i=l-1
    for j in range(l,h):
        if arr[j]<pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    
    arr[i+1],arr[h]=arr[h],arr[i+1]
    return i+1


def  qs(arr, l, h):
    if l<h:
        p=partition(arr,l,h)
        qs(arr, l, p-1)
        qs(arr,p+1,h)

l=[2,4,1,7,3,6,5]
qs(l, 0, 6)
print(l)
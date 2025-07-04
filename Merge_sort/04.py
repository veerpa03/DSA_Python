def merge(a,low,mid,high):
    left=a[low:mid+1]
    right=a[mid+1:high+1]
    m=len(left)
    n=len(right)
    i=0
    j=0
    k=low
    while i<m and j<n:
        if left[i]<=right[j]:
            a[k]=left[i]
            k+=1
            i+=1
        else:
            a[k]=right[j]
            k+=1
            j+=1
    while i<m:
        a[k]=left[i]
        k+=1
        i+=1
    while j<n:
        a[k]=right[j]
        k+=1
        j+=1
    

def mergeSort(a, l, r):
    if r>l:
        m = (r+l)//2
        mergeSort(a,l,m)
        mergeSort(a,m+1,r)
        merge(a, l, m, r)

a=[10,5,30,15,7]

mergeSort(a,0,4)

print(a)
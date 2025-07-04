# Merge subarrays
# Example:
# I/P = > a =[10,15,20,11,13]
# given low =0, high -4, mid=2
# O/P => a[10,11,13,15,20]
# def merge(a,low,high,mid):
def merge(a,low,mid,high):
    left=a[low:mid]
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
    return a

a = [10,15,20,40,8,11,55]
print(merge(a,0,3,6))
            
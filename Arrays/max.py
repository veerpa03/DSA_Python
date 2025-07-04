# l =[1,5,3,4,22,7,6,8] -> 22
# l =[] => none
# l =[1] => 1
def max2(a,b):
    if a>b:
        return a
    else:
        return b
def maximum(l):
    n=len(l)
    if n == 0:
        return "list is empty"
    if n == 1:
        return l[n-1]
    maxi=l[0]
    for i in range(1, n):
        maxi = max2(maxi,l[i])
    return maxi
    

print(maximum([1,5,22,4,22,7,6,13])) 

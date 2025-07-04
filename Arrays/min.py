def minimum (l):
    n = len(l)
    if n==0:
        return "list is empty"
    elif n==1:
        return l[n-1]
    mini=l[0]
    for i in range(1,n):
        if l[i]<mini:
            mini=l[i]
    return mini

print(minimum([2,6,8,1,9,4]))

def sums(n):
    if n==1:
        return 1
    return n+sums(n-1)
print(sums(5))
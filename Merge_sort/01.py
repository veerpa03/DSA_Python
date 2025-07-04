a = [10,15,20]
b = [5,6,6,30]
res = []

res = a+b
res.sort()
print(res)
# Time complexity is (m+n)xlog(m+n)
# let len(a) => m
# let len(b) => n
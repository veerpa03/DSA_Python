# l = [3,8,6,12,10,7]
# p = 5
# o/p l=[3,6,7,8,12,10]

left =[]
right=[]
p=5
l = [3,8,6,12,10,7]
i=0
while i<len(l):
    if l[i]<=l[p]:
        left.append(l[i])
        i+=1
    else:
        right.append(l[i]) 
        i+=1

print(left+right)


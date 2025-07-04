a =[5,4,3,2,1]
count=0
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if i<j and a[i]>a[j]:
            count+=1
print(count)
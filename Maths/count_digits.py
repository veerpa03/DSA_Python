# 1234   -> 4
# 123412 -> 6
def counts(n):
    count = 0
    while n>0:
        n=n//10
        count+=1
    return count

print(counts(53251243))



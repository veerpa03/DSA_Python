#Print 1 to N using recursion
#Input: 5 → Output: 5 4 3 2 1
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
fun(5)
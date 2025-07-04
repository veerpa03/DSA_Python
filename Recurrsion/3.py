#Print 1 to N using recursion
#Input: 5 → Output: 1 2 3 4 5
def fun(n):
    if n==0:
        return
    fun(n-1)
    print(n)
fun(5)
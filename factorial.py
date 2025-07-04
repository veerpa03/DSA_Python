# 4! => 4x3x2x1 =>24
# 1! => 1
# 0! => 1
# 5! => 5x4x3x2x1 =>120

def factorial(n):
    if n<=1:
        return 1
    fact =1
    for i in range(2,n+1):
        fact = fact*i
    return fact
print(factorial(6))

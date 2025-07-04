# def gcd(a,b):
#     if a%b==0:
#         return b
#     elif b%a==0:
#         return a
#     mini = min(a,b)
#     curr_gcd=1
#     for i in range(1, mini+1):
#         if a%i==0 and b%i==0:
#             curr_gcd=max(curr_gcd,i)
    
#     return curr_gcd

# def gcd(a,b):
#     while a!=b:
#         if a>b:
#             a=a-b
#         else:
#             b=b-a
#     return a

def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

print(gcd(4,6))
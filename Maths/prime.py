# def prime(n):
#     if n==1:
#         return False
#     i=2
#     while (i*i<=n):
#         if n%i==0:
#             return False
#         i+=1
#     return True

# print(prime(70))

def prime_fact(n):
    num=n
    for i in range (2, n):
        if n%i==0:
            curr=i
            curr=min(curr,i)
            num=num//curr
prime_fact(100)



1 2 3 6 4 2 0
4 3 2 1 0
1 2 3 4 5 7 
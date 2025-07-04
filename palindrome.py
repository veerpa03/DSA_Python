# 121 -> yes
# 1211 -> no
# 78987 -> yes

# def palindrome(n):
#     n=str(n)
#     for i in range(len(n)):
#         if n[i]!=n[-(i+1)]:
#             return False
#     return True
# print(palindrome(121))



def palindrome(n):
    rev=0
    temp =n
    while temp>0:
        rev = (rev*10) + temp%10
        temp=temp//10
    return rev==n

print(palindrome(121))


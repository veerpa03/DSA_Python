# Without recussriosn
# def fun1(n):
#     l=[]
#     for i in range(1, n+1):
#         if(i%2==0):
#             l.append(i-1)
#         else:
#             l.append(i+1)
#     return l
# print(fun1(10))

def fun(n):
    if n<1:
        return 
    fun(n-1)
    fun(n-3)
    print(n)

fun(6)
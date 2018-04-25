# def f(n):
#     return n*n
# def foo(a,b,func):
#     res =func(a)+func(b)
#
#     return res
#
#
# foo(1,2,f)
# print(foo(1,2,f))


# def fact(n):
#
#     if n==1:
#         return 1
#     return n*fact(n-1)
#
# print(fact(5))

# 0 1 1 2 3 5 8 13 21 34 55

# def fibo(n):
#     # if n<=2:    # 34
#     if n==0 or n==1:    # 21
#         return n
#
#
#     return fibo(n-1)+fibo(n-2)
#
#
# print(fibo(8))


def fat(n):
    # 这里设定从1开始
    ret=1
    # 循环1到n+1之间的数字
    for i in range(1,n+1):
        # 
        ret=ret*i

    return ret

print(fat(5))   # 120,5*4*3*2*1





def tst(a,b,c=33,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

A = [44,55,66,77]
B = {"name":"lisi","age":18}
tst(1,22,3,*A,**B)
# 如果A前面的参数少传了，从A列表里补上

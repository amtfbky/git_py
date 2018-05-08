def tst(a,b,func):

    #res = a+b
    res = func(a,b)
    return res

num = tst(11,22,lambda x,y:x+y)
print(num)

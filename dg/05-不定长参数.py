def tst(a,b,*args):
    print("----------")
    print(a)
    print(b)
    print(args)

    res = a+b
    for i in args:
        res += i
    print("%d" % res)

tst(1,22,33,44,55)
tst(1,22,33)
tst(1,22)

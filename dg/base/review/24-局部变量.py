def demo1():
    # 局部变量从下面的语句出生
    num = 10
    print("这是函数内部的局部变量：%d" % num)
    # 在函数内这个局部变量在使用完成之后就被系统回收，从而结束生命

def demo2():
    #print(num)
    pass
#print(num)
demo1()
#demo2()


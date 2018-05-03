#a = 100
a = [100]
def tst(num):

    #num += num # --->[100, 100]不等价于下句
    num = num + num #--->[100]
    print(num)

tst(a)
print(a)

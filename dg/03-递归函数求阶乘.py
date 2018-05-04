‘’‘这是一个计算阶乘的递归函数，一定要有出口’‘’
def getNum(num):

    if num>1:
        return num*getNum(num-1)
    else:
        # 这里就是出口
        return num


res = getNum(4)
print(res)

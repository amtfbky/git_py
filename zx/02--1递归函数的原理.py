def getNum(num=4):
    res = num * getNum(num-1)
    return res

def getNum(num=3):
    res = num * getNum(num-1)
    return res

def getNum(num=2):
    res = num * getNum(num-1)
    return res

def getNum(num=1):
    return 1


res2 = getNum()
print(res2)

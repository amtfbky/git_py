def getNum(num):
    if num>1:
        return num*getNum(num-1)
    else:
        return 1

res = getNum(3)
print(res)

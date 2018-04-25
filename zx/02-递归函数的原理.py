# 阶乘的递归函数
'''
i = 1
res = 1
while i <= 4:
    res *= i
    i += 1

print(res)

def getN4(num=4):
    res = getN3(num-1)  # getN3(num-1)=3*2*1
    return num * res
def getN3(num=3):
    res = getN2(num-1)  # getN2(num-2)=2*1
    return num * res
def getN2(num=2):
    res = getN1(num-1)  # getN1(num-1)=1
    return num * res
def getN1(num=1):
    return 1

rs = getN4()
print(rs)
'''

def getN1(num=1):
    return 1
def getN2(num=2):
    res = getN1(num-1)  # getN1(num-1)=1
    return num * res
def getN3(num=3):
    res = getN2(num-1)  # getN2(num-1)=2*1
    return num * res
def getN4(num=4):
    res = getN3(num-1)  # getN3(num-1)=3*2*1
    return num * res
def getN5(num=5):
    res = getN4(num-1)  # getN2(num-1)=4*3*2*1
    return num * res
rs = getN5()
print(rs)


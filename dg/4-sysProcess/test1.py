import pdb

def getAverage(a,b):
    res = a+b
    print("res=%d"%res)
    return res

a = 100
b = 200
c = a+b
# 埋点调试
#pdb.set_trace()
ret = getAverage(a,b)
print(ret)
# 很多网站不允许停止运行来调试，只能通过一些

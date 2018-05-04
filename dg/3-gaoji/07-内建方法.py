"""
# 说是面试必考
# 底下是在Python2实现的
In [1]: range(0,5)
Out[1]: [0, 1, 2, 3, 4]

In [2]: xrange(0,5)
Out[2]: xrange(5)
"""
# map是让一个可迭代对象生成新的可迭代对象

l1 = map(lambda x:x*x, [1,2,3])
#print(list(l1))
for tmp in l1:
    print(tmp)

l2 = map(lambda x,y:x+y, [1,2,3], [4,5,6])
#print(list(l2))
for tmp in l2:
    print(tmp)


def f1(x,y):
    return (x,y)

# 这个可以用在彩票中奖号摇号
a1 = [0,1,2,3,4,5,6]
a2 = ['sun', 'M', 'T', 'W', 'T', 'F', 'S']
a3 = map(f1, a1, a2)
print(list(a3))

print("*********************************")

# 过滤，取余为0的滤掉
ret = filter(lambda x:x%2, [1,2,3,4])
print(list(ret))

# None就不滤了
ret = filter(None, "she")
print(str(ret))

print("*********************************")



# 这里是前一个私有化类“01-私有化.py”的进阶
class Test(object):
	def __init__(self):
		self.__num = 100

	def setN(self, newNum):
		self.__num = newNum

	def getN(self):
		return self.__num

        # 这里property是设置方便调用属性值的一个内置函数？
	num = property(getN, setN)

t = Test()
# 这里也可以直接给类属性赋值，否则就直接打印类里面的属性值
t.num = 200
print(t.num)

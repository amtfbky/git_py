class Test(object):
	def __init__(self):
		self.__num = 100

	def setN(self, newNum):
		self.__num = newNum

	def getN(self):
		return self.__num
	num = property(getN, setN)

t = Test()
#t.num = 200
print(t.num)

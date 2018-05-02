def func(functionName):
	print("-----func--1---")
	def func_in():
		print("---func_in---1---")

		# functionName()就是test函数
		ret = functionName()
		print("---func_in---2---")

		# 这里应该再次返回test函数的返回值
		return ret
	print("-----func--2---")
	return func_in

# 在没有装饰前可以得到返回值haha，而装饰后却得到None
@func
def test():
	print("------test------")
	return "haha"


ret = test()
print("test return value is %s"%ret)

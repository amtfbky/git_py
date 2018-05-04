def func(functionName):
	def func_in(*args, **kwargs):
		print("----记录日志----")
		# functionName()就是test函数
		ret = functionName(*args, **kwargs)

		# 这里应该再次返回test函数的返回值，这里有返回值不影响test2没有return
		return ret
	print("-----func--2---")
	return func_in

# 在没有装饰前可以得到返回值haha，而装饰后却得到None
@func
def test():
	print("------test------")
	return "haha"

@func
# 虽然test2没有返回数据，但照样可以装饰带有返回的装饰器
def test2():
	print("------test2------")

@func
# 这里有参数，把func_in里的参数写成不定长参数，就是通用的装饰器
def test3(a):
	print("------test3-a=%d-----"%a)

ret = test()
print("test return value is %s"%ret)

a = test2()
print("test return value is %s"%a)

#test3([11,22],{"name":"lisi","age":44})
test3(11)

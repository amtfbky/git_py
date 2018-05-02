# 定义test函数
def test(number):
	print("--1--")

	# 在test函数里又定义一个test_in函数
	def test_in(number2):
		print("--2--")

		# number是test函数的形参，number2是test_in的形参
		print(number+number2)

	print("--3--")

	# 这句是核心，test_in指向它指向的函数体
	return test_in


# test_in函数体里调用了test的参数，ret保留着这个参数值，不会删除
ret = test(100)
print("*" * 30)
ret(1)
ret(100)
ret(200)

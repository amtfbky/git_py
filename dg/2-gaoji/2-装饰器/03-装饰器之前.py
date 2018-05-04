# 现在这里的func就是f1
def w1(func):
	
	# 这个嵌套函数里面因为有个func()构成了闭包
	def inner():
		
		# 这是嵌套函数里的功能代码
		print("---正在验证权限---")

		# 这是让功能调用者执行自己的f1方法
		func()

	# 这里返回嵌套函数的值，就是上面两句代码的结果即print和f1
	return inner

# 功能调用者自己的代码，我们要做的是尽量不修改这里的代码而是修改w1的
def f1():
	print("---f1---")
	

def f2():
	print("---f2---")
# f1作为一个地址被w1当做参数传到w1方法里
innerFunc = w1(f1)
#innerFunc = w1(f2)
# 执行
innerFunc()

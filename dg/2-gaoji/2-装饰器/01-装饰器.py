def w1(func):
	def inner():
		print("---正在验证权限---")

		func()
	return inner

# f1 = w1(f1)
# 装饰器的作用是让调用者不用修改自己的代码而可以调用w1的方法
@w1
def f1():
	print("---f1---")

# f2 = w1(f2)
@w1
def f2():
	print("---f2---")

f1()
f2()

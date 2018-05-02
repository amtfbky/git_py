def test():
	print("-----1-----")


test()
print(test)

# test块在ipython3里的操作结果
# <function __main__.test>
# __main__是这个test功能块的内置系统方法
# 让b=test，则b的结果也是上面的显示，所以b()=test()
# 实际上test就是test这个函数体的一个变量名而已
# 而b=test就是b也指向test这个函数体





class Test(object):
    # 初始化里有一个num属性，设成私有
    def __init__(self):
        self.__num = 100

    # 这是设置数据的方法，添加一个形参让实例对象传实参
    def setNum(self, newNum):
        # 这里设置私有属性=传参进来的数据
        self.__num = newNum

    # 这里设置获取数据的方法，返回上面设置数据的函数里面的属性值
    def getNum(self):
        return self.__num


# 创建一个类对象
t = Test()
# 这里直接给类里面的属性赋值，覆盖类里面的属性值
#t.__num = 200
#print(t.__num)

# 先打印类里面的属性值
print(t.getNum())
# 再给类里面的setNum方法传实参，重新赋值
t.setNum(50)
# 再打印新赋值的属性值
print(t.getNum())

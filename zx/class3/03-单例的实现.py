"""回收站,游戏窗口等程序不管怎么创建只有一个实例
"""


class Dog(object):
    
    # 定义一个?变量为None值
    __instance = None

    def __new__(cls):

        # 判断类对象引用的变量值(属性值?)为空
        if cls.__instance == None:
            # 让父类调用__new__方法,并让类对象引用的变量引用
            cls.__instance = object.__new__(cls)
            # 再返回类对象引用的值
            return cls.__instance
        else:
            # 如果不为空,则返回上一次创建的对象的引用
            return cls.__instance


a = Dog()
print(id(a))
b = Dog()
print(id(b))

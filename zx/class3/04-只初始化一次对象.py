"""回收站,游戏窗口等程序不管怎么创建只有一个实例
"""


class Dog(object):
    
    # 定义一个?变量为None值
    __instance = None
    __init_flag = False

    def __new__(cls, name):

        # 判断类对象引用的变量值(属性值?)为空
        if cls.__instance == None:
            # 让父类调用__new__方法,并让类对象引用的变量引用
            cls.__instance = object.__new__(cls)
            # 再返回类对象引用的值
            return cls.__instance
            #return object.__new__(cls)
            
        else:
            # 如果不为空,则返回上一次创建的对象的引用
            return cls.__instance

    # 定义让init只初始化一次的方法
    def __init__(self, name):
        # 判断创建对象调用__init_flag属性是否为假
        if Dog.__init_flag == False:
            # 如果为假,则初始化,即将创建对象的实参传给self.name
            self.name = name
            # 紧接着就把__init_flag值变为真,当再创建对象时__init_flag就不是假了
            # 也就不再给self.name传参了
            Dog.__init_flag = True

a = Dog("旺财")
print(id(a))
print(a.name)
b = Dog("哮天犬")
print(id(b))
print(b.name)

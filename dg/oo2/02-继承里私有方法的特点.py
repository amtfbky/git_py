class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def test1(self):
        print("-------test1-------")

    def __test2(self):
        print("-------test2---------")

    def test3(self):
        """如果调用的是继承的父类中的公有方法，可以在这个方法中访问
        父类中的私有方法和私有属性"""
        self.__test2()
        print(self.__num2)

class B(A):
    """如果在子类中实现了一个公有方法，那么这个方法是不能够调用父类中
    私有方法和私有属性"""
    def test4(self):
        self.__test2()
        print(self.__num2)


b = B()
#b.test1()
#b.__test2()  # 私有方法不会被继承
#print(b.num1)
#print(b.num2)   # 父类里也有小秘密，不会被...
b.test3()   # 该方法没有设为私有，可以...
b.test4()






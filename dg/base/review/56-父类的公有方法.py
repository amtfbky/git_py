class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

    def test(self):
        # 父类的公有方法可以调用自己的私有属性和方法
        # 子类就可以通过调用父类公有方法间接调用父私
        print("父类的公有方法 %d" % self.__num2)
        self.__test()

class B(A):
    def demo(self):
        # 子类不能方位父类的私有属性
        #print("访问父类的私有属性 %d" % self.__num2)

        # 子类不能调用父类的私有方法
        #self.__test()

        # 访问父类的公有属性
        print("子类方法 %d" % self.num1)

        # 调用父类的公有方法
        self.test()


b = B()
print(b)

print(b.num1)
b.test()
b.demo()

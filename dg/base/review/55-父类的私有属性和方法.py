class A:
    def __init__(self):
        self.num1 = 100
        self.__num2 = 200

    def __test(self):
        print("私有方法 %d %d" % (self.num1, self.__num2))

class B(A):
    def demo(self):
        # 子类不能方位父类的私有属性
        #print("访问父类的私有属性 %d" % self.__num2)

        # 子类不能调用父类的私有方法
        #self.__test()

b = B()
print(b)
#print(b.__num2)
#b.__test
b.demo()

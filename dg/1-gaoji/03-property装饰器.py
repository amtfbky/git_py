# 这是前一个“02...”的进阶
class Test(object):
    def __init__(self):
        self.__num = 100

    # 这里property成了装饰器
    @property
    # 不用再写setNum，？
    def num(self):
        return self.__num

    # 不用再写getNum，？
    def num(self, newNum):
        self.__num = newNum

t = Test()

t.num = 200
print(t.num)


class Dog(object):
    def __init__(self):
        print("-----init------")

    def __del__(self):
        print("-----del------")
    
    def __str__(self):

        print("------str-----")
        return "direction"
    
    """相当于要做3件事:
        1.调用__new__方法来创建对象,然后找了一个变量来接收__new__的返回值,这个返回值表示创建出来的对象的引用
        2.__init__(刚刚创建出来的对象的应用
        3.返回对象的引用"""
    def __new__(cls):
        print(id(cls))

        print("-----new------")
        return object.__new__(cls)


print(id(Dog))
xtq = Dog()






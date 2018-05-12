class Dog(object):

    @staticmethod
    def eat():
        # 不访问实例属性/类属性
        print("-----eat-----")


# 类名.静态方法，不需要创建对象
Dog.eat()

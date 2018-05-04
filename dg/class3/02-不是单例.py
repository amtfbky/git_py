"""回收站,游戏窗口等程序不管怎么创建只有一个实例
"""


class Dog(object):
    pass

a = Dog()
print(id(a))
b = Dog()
print(id(b))

class Base(object):
    """新式类"""
    def test(self):
        print("----Base")

class A(Base):
    def test(self):
        print("--------A")

class B(Base):
    def test(self):
        print("--------B")

class C(A,B):
    pass
    #def test(self):
    #   print("--------C")

c = C()
c.test()    # 如果C类里有相同的方法（尽可能不要写相同的方法名？），先调用C类中的方法
print(C.__mro__)
"""类名.__mro__决定这调用一个方法的时候，搜索的顺序，如果在某个类中找到了就停止搜索"""

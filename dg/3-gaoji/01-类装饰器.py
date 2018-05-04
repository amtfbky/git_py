"""
In [4]: class Test(object):
   ...:     def __init__(self, func):
   ...:         print("---初始化---")
   ...:         print("func name is %s"%func.__name__)
   ...:         self.__func = func
   ...:     def __call__(self):
   ...:         print("---装饰器中的功能---")
   ...:         self.__func()
   ...:         

In [5]: def test():
   ...:     print("-----test------")
   ...:     

In [6]: 

In [6]: test()
-----test------

In [7]: @Test   # test=Test(test)
   ...: def test():
   ...:     print("------test-------")
   ...:     
---初始化---
func name is test

In [8]: test()
---装饰器中的功能---
------test-------

"""

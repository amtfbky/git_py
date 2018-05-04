"""
In [2]: class Test:
   ...:     pass
   ...: 

In [3]: t1 = Test()

In [4]: Test2 = type("Test2", (), {})

In [5]: t2 = Test2()

In [6]: type(t1)
Out[6]: __main__.Test

In [7]: type(t2)
Out[7]: __main__.Test2

In [8]: class Person:
   ...:     num = 0
   ...:     

In [9]: Person2 = type("Person2", (), {"num":0})

In [10]: p1 = Person()

In [11]: p1.num
Out[11]: 0

In [12]: p2 = Person2()

In [13]: p2.num
Out[13]: 0

*********************************************************
# 实际上class就是type创建出来的，而type更灵活，class一般就写死了

In [14]: def printNum(self):
   ....:     print("-----num  %d----"%self.num)
   ....:     

In [15]: Test3 = type("Test3", (), {"printNum":printNum})

In [16]: t = Test3()

In [17]: t.num = 100

In [18]: t.printNum()
-----num  100----

In [19]: class printNum2:
   ....:     def printNum(self):
   ....:         print("----num %d----"%self.num)
   ....:         

In [20]: t2 = printNum2()

In [21]: t2.num = 200

In [22]: t2.printNum()
----num 200----
"""

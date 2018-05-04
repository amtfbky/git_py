"""
In [9]: def test():
   ...:     i = 0
   ...:     while i<5:
   ...:         temp = yield i
   ...:         print(temp)
   ...:         i+=1
   ...:         

In [10]: t = test()

In [11]: t.__next__()
Out[11]: 0

In [12]: t.__next__()
None
Out[12]: 1

In [13]: t.__next__()
None
Out[13]: 2

In [14]: t.send("haha")
haha
Out[14]: 3

In [15]: t.send("a")
a
Out[15]: 4

In [16]: t.send("b")
b
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-16-638e2c6f3d09> in <module>()
----> 1 t.send("b")

StopIteration:
"""

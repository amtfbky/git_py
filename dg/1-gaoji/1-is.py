"""
In [1]: a = [1,2,3]

In [2]: b = [1,2,3]

In [3]: a == b
Out[3]: True

In [4]: a is b
Out[4]: False

In [5]: c = a

In [6]: c
Out[6]: [1, 2, 3]

In [7]: id(a)
Out[7]: 140224251260872

In [8]: id(b)
Out[8]: 140224251296008

In [9]: id(c)
Out[9]: 140224251260872
这是is判断，a==b，但a not is b
"""
# c is a，True

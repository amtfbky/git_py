# Garbage collection(GC垃圾回收)
# python引用计数机制为主，标记-清除和分代收集两种机制为辅的策略
"""
char    1
int     4
float   4
double  8

In [1]: import gc

In [2]: gc.get_count()
Out[2]: (355, 7, 5)

In [3]: gc.get_count()
Out[3]: (414, 7, 5)
In [6]: gc.get_threshold()
Out[6]: (700, 10, 10)

"""
"""
导致引用计数+1的情况：
    对象被创建，如a=23
    对象被引用，如b=a
    对象被作为参数，传入到一个函数中，如func(a)
    对象作为一个元素，存储到容器中，如list=[a,a]

导致引用计数-1的情况：
    对象的别名被显示销毁，如del a
    对象的别名被赋予新的对象，如a=24
    一个对象离开它的作用域，如f函数执行完毕时，func函数中的局部变量（全局变量不会）
    对象所在的容器被销毁，或从容器中删除对象

查看引用计数：

In [1]: import sys

In [2]: a = "hello world"

In [3]: sys.getrefcount(a)
Out[3]: 2

In [4]: b = a

In [5]: sys.getrefcount(a)
Out[5]: 3

In [6]: c = a

In [7]: sys.getrefcount(a)
Out[7]: 4


"""

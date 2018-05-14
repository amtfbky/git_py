1.标识符、关键字
    if/else/elif/break/continue/for/while/and/or/not/in/True/False/try/except/finally/as/import/from/def/class/return/None/global/lambda/pass/yield/with/del/is

2.变量、输入、输出
    c=a
    a=b
    b=c

    b=a+b
    b=a-b
    a=a-b

    a,b=b,a

    python2:raw_input() 3+4 ---> 7
    python3:3+4 ---> "3+4"

3.字符串、列表、元组、字典
    元组只读
    {1,2,3,1,1,1} ---> {1,2,3}集合不重复

    可变：列表、字典、集合
    不可变：数字、字符串、元组

    什么都可以当value
    [{"name":"小明","family":[{"七姑":"巧玲", "family":[{"姑父":"xxx","a": "b"}]}]}]

4.切片

5.if

6.while
        i = 100
        while i>0:
            print(i)
            i -= 1
7.for
8.各种嵌套
9.函数、参数、返回值、全局/局部变量、多个return、一个return返回多个值
10.类、对象
11.异常
    try:
        xxx
    except 异常的名字:
        异常的处理...
    else:
        没有异常的时候执行
    finally:
        不管有否产生异常，都会执行
12.模块、包
    import 模块、包
    xxxx.功能()

    from 模块 import test1,test2
    test1()

    from ... import *

    if __name__ == '__main__':
        xxx

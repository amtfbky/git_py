def test(num):

    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))
    num = 2
    print("函数要返回数据的内存地址是 %d" % id(num))
    return num

# 1.定义一个数字的变量
a = 1
# 数据的地址本质上就是一个数字
print("a 变量保存数据的内存地址是：%d" % id(a))

# 2.调用test函数，
# 本质上传递的是实参保存数据的引用，而非实参保存的数据

res = test(a)
print(res)
print("%s 的内存地址是：%d" % (res, id(res)))

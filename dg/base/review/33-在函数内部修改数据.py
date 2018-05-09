def demo(num_list):
    print("函数内部代码")
    num_list.append(9)
    print(num_list)

    print("函数执行完毕")

# gl_list和num_list都贴到列表的内存地址门框上
# 如果传递的参数是可变类型，在函数内部，使用方法修改了数据的内容，同样会影响到外部的数据
gl_list = [1,2,3]
demo(gl_list)
print(gl_list)

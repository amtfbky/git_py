"""定义函数时，是否接收参数，或者是否返回结果，是根据实际的功能需求
    1.如果函数内部处理的数据不确定，就可以将外界的数据以参数传递到函数内部
    2.如果希望一个函数执行完成后，向外界汇报执行结果，就可以增加函数的返回值"""

def measure():
    """测量温度和湿度"""

    print("测量开始...")
    temp = 39
    wetness = 50
    print("测量结束...")

    # 返回值可以用元组，而且小括号省略
    return temp, wetness

# 元组
res = measure()
print(res)

# 需要单独的处理温度和湿度，这样子不方便
print(res[0])
print(res[1])

# 如果函数返回的类型是元组，同时希望单独的处理元组中的元素
# 可以使用多个变量，一次接收函数的返回的结果
gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)

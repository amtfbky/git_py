def creatNum():
    # 当第一次next时，只打印start
    print("--------start-------")
    a,b = 0,1
    for i in range(5):
        # 执行到这里就是生成器了，只有next调用一次才能生成一个数据
        # 这样子就不会给内存造成浪费
        # yield会返回一个b的值，从1开始
        yield b
        a,b = b,a+b
    # 当遍历数据完成后打印stop再报错，说明生成器里没有数据了
    print("--------stop-------")


a = creatNum()
ret = next(a)
print(ret)
ret = next(a)
print(ret)
ret = next(a)
print(ret)
ret = next(a)
print(ret)
ret = next(a)
print(ret)
ret = next(a)

# 闭包就是函数里面有个内置函数，而且
# 这个内置函数里面又用到外置函数的参数
# 然后再返回内置函数的引用（是值吗？）

# 这是外置函数，带有参数
def test(num):
    print("--1--")

    # 这是内置函数，也带有参数
    def test_in(num2):
        print("--2--")
        print("num2=%d"%num2)
        # 这里用到外置函数的参数
        print(num+num2)

    # 函数执行到这里，还未执行内置函数
    # 等到下面返回时才会执行？
    print("--3--")
    # 返回内置函数的引用？
    return test_in

# 创建一个实例，并给num2也就是内置函数传参
# 再把这个实例对象让ret引用
ret = test(66)

# 函数创建实例后先执行外置函数，打印-1-和-3-
# 再往下把1传进去给内置函数
print("-" * 30)

# 此时，ret就是外置函数，实参传给num
ret(1)
#ret(100)
#ret(200)



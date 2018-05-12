def demo():
    return int(input("请输入一个整数:"))

def demo2():
    return demo()

# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())
except ValueError:
    print("请输入正确的整数")
except Exception as res:
    print("未知错误" % res)

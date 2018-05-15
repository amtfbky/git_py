def demo():
    print("哈哈，这是我的测试，你们导入看不见...")

def demo_try():
    print("这是学习name内置函数的作用...")

print(__name__) 
print("在导入的程序里看到name=被导入的模块名")

# 在if之上的不带缩进的语句会被执行，在if下面的语句则是开发者的测试语句
# 被导入不会执行
demo_try()
if __name__ == '__main__':
    print(__name__) # 如果执行本模块，__name__永远=__main__
    print("小明开发的模块")
    demo()

# 把用户输入的数字打印出来

def demo(*nums):
     for n in nums:
        print("您输入的数字为：%d" % n)

# 一个元组
n_input = (int(input("第1个数字：")),
        int(input("第2个数字：")),
        int(input("第3个数字：")))

# 这里的参数要加上*，才能拆包
demo(*n_input)

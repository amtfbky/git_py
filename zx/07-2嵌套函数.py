# 这是我第一个用自己的想法写出的Python程序，成功了！\(^o^)/
# 让用户自己输入数字，想打印几条分隔线就就打印几条
def print_line():
    print("*" * 30)

def print_lines():
    i = int(input("请输入您想打印分隔线的数字: "))
    j = 0
    while j < i:
        print_line()
        j += 1
print_lines()

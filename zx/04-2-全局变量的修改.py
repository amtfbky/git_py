""" 时间：18412
    作者：Aaron
    内容：局部变量和全局变量"""

# 设定全局变量 
wendu = 0

# 定义获取温度函数
def get_wendu():
    # 修改全局变量，global声明wendu是全局变量
    global wendu
    wendu = 22

# 定义显示温度函数
def print_wendu(xingcan):
    print("温度是：%d"%xingcan)

    
# 创建获取温度实例
get_wendu()
# 创建显示温度实例
print_wendu(wendu)


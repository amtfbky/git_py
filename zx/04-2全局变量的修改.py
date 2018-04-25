'''
def get_w():

    wendu = 33
    return wendu

def print_w(a):
	
# a是形参，但把get_w函数的引用res当成参数给print_w函数
# 而a传给print_w的是get_w函数的返回值
    print("%d"%a)

res = get_w()
print_w(res)
'''
wendu = 0
def get_w():
    global wendu
    wendu = 33

# print_w函数的参数是wendu，这是get_w函数里的全局变量名，而全局变量已经由global改成33
# 如果print_w传的是函数外的wendu，那可以把变量名改掉，就是说函数外的wendu不是get_w函数里的wendu
def print_w(wendu):
    print("%d"%wendu)

get_w()
print_w(wendu)

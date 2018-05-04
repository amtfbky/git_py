''' 时间：2018年04月12日16:16:57
    作者：Aaron
    内容：1.先求三个数的和
          2.再求三个数的平均值
          3.再求三个数平均值的平方'''

# 这里用的是形参，可以用其他字母代替，以下一样 
def sum_3_num(a,b,c):
    res = a + b + c
    #print("三个数字的和：%d"%res)
    return res

def verage_3_num(n1,n2,n3):
    res2 = sum_3_num(n1,n2,n3)  
    # 这里用的也是形参，但必须是在函数方法的参数定义过的
    res2 /= 3
    #print("三个数的平均值：%d"%res2)
    return res2

def pingfang_3_num(f1,f2,f3):
    res3 = verage_3_num(f1,f2,f3)
    res3 *= res3 * res3 
    print("三个数平均值的平方：%d"%res3)

num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字："))
num3 = int(input("请输入第三个数字："))

# 这里实例用的是实参，所以要写num...
#sum_3_num(num1,num2,num3)
#verage_3_num(num1,num2,num3)
pingfang_3_num(num1,num2,num3)

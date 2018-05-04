def tst(a,b,func):

    #res = a+b
    res = func(a,b)
    return res
#func_new = input("请输入一个匿名函数：")
func_new = 'lambda x,y:x*y+100'	# 这里要字符串才行
func_new = eval(func_new)

num = tst(11,22,func_new)
print(num)

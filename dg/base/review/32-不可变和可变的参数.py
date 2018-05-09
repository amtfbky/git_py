def demo(num, new_list):
    # 只要针对参数使用赋值语句，会在函数内部修改局部变量的引用，不会影响到外部变量的引用
    num = 100
    new_list = [1,2,3]
    print(num)
    print(new_list)


gl_num = 99
gl_l = [4,5,6]

demo(gl_num, gl_l)
print(gl_num)
print(gl_l)

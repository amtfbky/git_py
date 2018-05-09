def demo(num, num_list):
    print("函数开始")
    num += num
    #num = num + num

    # 在Python中，列表变量调用+=本质上是在执行列表变量的extend方法，不会修改变量的引用
    # 这个不理解！！！！！！
    # 不会修改变量的引用，就会影响到外部变量，何故？

    #num_list += num_list
    #num_list.extend(num_list)
    
    # 这句为何就修改了变量的引用呢？然后就没有影响到外部变量
    num_list = num_list + num_list
    print(num)
    print(num_list)
    print("函数完成")

gl_num = 9
gl_list = [1,2,3]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)


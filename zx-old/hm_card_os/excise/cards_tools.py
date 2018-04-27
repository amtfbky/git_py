# 记录所有的名片字典
card_list = []

def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("")
    print("1.add")
    print("2.showall")
    print("3.find")
    print("")
    print("0.exit")
    print("*" * 50)
def new_card():

    """新增名片"""
    print("*" * 50)
    print("新增名片")

    # 1.提示用户输入名片的详细信息
    # 用input接收用户输入信息，没有用str函数转换

    # 2.使用用户输入的信息建立一个名片字典
    # 格式为：字典名={"key":value}

    # 3.将名片字典添加到列表中
    # 用append将字典信息添加到列表中，并打印出来

    # 4.提示用户添加成功
    # 用格式显示
    
def show_all():
    
    """显示所有名片"""
    print("*" * 50)
    print("显示所有名片")

    # 判断是否存在名片记录没有则提示且返回
    # 用if len==0判断列表中的记录是否为空，并用return返回

    # 打印表头
    
    # 打印分割线

    # 遍历名片列表依次输出字典信息
    
def search_card():
    
    """查询名片"""
    print("*" * 50)
    print("查询名片")

    # 1.提示用户输入要搜索的姓名

    # 2.遍历名片列表，查询要搜索的姓名，如果没有找到，需要提示用户
    # 用for遍历找到的名片字典

        # 用if语句判断要搜索的姓名是否在列表中
            # 打印名片列表

            # 针对找到的名片记录执行修改和删除操作，再break循环

    
def deal_card():

    """处理名片
    :param find_dict: 查询到的名单字典"""
    # 打印查询到的名单字典
    

    # 对该名单字典选择操作
    
    # 对该名单进行修改操作
    # 用if判断操作值==1时修改

    # 对该名单进行删除操作
    # 用elif判断操作==2时删除

def input_card_info():

    """修改名片信息
    :param dict_value: 字典中原有的值
    :param tip_msg: 输入的提示文字
    :return: 如果用户输入了内容，就返回内容，否则返回字典中原有的值"""
    
    # 1.提示用户输入内容

    # 2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果

    # 3.如果用户没有输入内容，返回”字典中原有的值“
card_list = []

def show_menu():
    print("*" * 50)
    print("")
    print("         名片管理系统v1.0")
    print("1.添加名片")
    print("2.显示名片")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*" * 50)

def add_card():
    """添加名片"""

    # 1.让用户输入名片信息
    name_str = input("请输入您的姓名：")
    phone_str = input("请输入您的电话：")
    addr_str = input("请输入您的住址：")

    # 2.把名片信息放到名片字典
    card_dict = {"name":name_str,
                "phone":phone_str,
                "addr":addr_str}

    # 3.将名片字典添加到名片列表
    card_list.append(card_dict)

    # 4.提示用户添加成功并显示名片信息
    print("%s 添加成功！" % name_str)

def show_all():

    """显示名片"""
    print("显示所有名片")
    print("-" * 50)
    
    # 判断是否有名片，如果没有，则提示用户并且返回
    if len(card_list) == 0:
        print("没有名片，请添加！")
        return
    
    # 1.打印表头
    for m in ["姓名", "电话", "地址"]:
        print(m, end="\t\t")
    print("")

    # 2.打印分隔线
    print("=" * 50)

    # 3.遍历名片字典
    for d in card_list:
        print("%s\t\t%s\t\t%s" % (d["name"],
            d["phone"],
            d["addr"]))

def search_card():
    """搜索名片"""
    
    print("-" * 50)
    print("")

    # 我居然把input粘贴成print，粘贴真的省事了？
    #find_name = print("请输入您要查找的姓名：")

    # 1.提示用户输入要查找的姓名
    find_name = input("请输入您要查找的姓名：")
    # 2.遍历名片列表，如果没有，则提示...
    for d in card_list:
        if d["name"] == find_name:
            for m in ["姓名", "电话", "地址"]:
                print(m, end="\t\t")
            print("")
            print("-" * 50)
            print("%s\t\t%s\t\t%s" % (d["name"],
                d["phone"],
                d["addr"]))
            break
    else:
        print("抱歉，没有找到 %s！" % find_name)

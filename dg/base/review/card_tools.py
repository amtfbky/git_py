card_list = []

def show_menu():
    print("=" * 50)
    print("")
    print("         名片管理系统v1.0")
    print("1.添加名片")
    print("2.显示所有名片")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("=" * 50)

def add_card():
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
    print(card_list)


def show_all():
    pass


def search_card():
    pass



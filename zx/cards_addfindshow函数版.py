# 定义名片列表
card_dics = []
def menu():
    # 1.打印系统功能提示
    print("*"*50)
    print("1.add")
    print("2.del")
    print("3.change")
    print("4.find")
    print("5.all")
    print("6.break")
    print("*"*50)

menu()

def card_new_add():
    # 把用户的添加信息赋值变量
    i_name = input("Name: ")
    i_qq = input("QQ: ")
    i_addr = input("Addr: ")

    # 定义一个新的字典存储一个新的名片
    new_dic = {}
    new_dic['name'] = i_name
    new_dic['qq'] = i_qq
    new_dic['addr'] = i_addr

    # 将一个字典添加到列表中
    card_dics.append(new_dic)
    # print(card_dics)  # for test

def card_find():
    find_name = input("Please input find name: ")
    find_flag = 0   # 默认表示没有找到
    for tmp in card_dics:
        if find_name == tmp['name']:
            print("%s\t%s\t%s" % (tmp['name'], tmp['qq'], tmp['addr']))
            find_flag = 1   # 表示找到了
            break
    # 判断是否找到了
    if find_flag == 0:
        print("No this people...")

def card_showall():
    print("name\tqq\taddr")
    for tmp in card_dics:
        print("%s\t%s\t%s"% (tmp['name'],tmp['qq'],tmp['addr']))

def main():
    while True:
        # 2.获取用户的输入
        num = int(input("Please input your choice: "))
        # 3.根据用户的输入执行相应的功能
        if num == 1:
            card_new_add()

        elif num == 2:
            pass
        elif num == 3:
            pass
        elif num == 4:
            card_find()

        elif num == 5:
            card_showall()

        elif num == 6:
            break
    else:
        print("your input error! Please input again!")

    print("")
main()

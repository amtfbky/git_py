import card_tools

def main():
    while True:
        card_tools.show_menu()

        action_num = input("请输入您要选择的操作：")
        print("您选择的操作是：【%s】" % action_num)

        # 这里action_num直接判断是否在列表里，很是简洁明了
        if action_num in ["1", "2", "3"]:

            # 这里的1是字符串，要加上引号，我居然没加
            if action_num == "1":
                card_tools.add_card()
            elif action_num == "2":
                card_tools.show_card()
            elif action_num == "3":
                card_tools.search_card()

        # 这里的条件判断和上面第一层判断是并列关系
        # 我给写到嵌套if里了，导致输入不能退出
        elif action_num == "0":
            print("欢迎再次光临！")
            break
        else:
            print("您输入有误，请重新输入！")


if __name__ == "__main__":
    main()

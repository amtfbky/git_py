#-*-coding:UTF-8-*-
def modify_card_infor():
    """用来修改一个名片"""

    modify_name = raw_input("请输入要修改的人的姓名：") #输入要修改的那个人的姓名
#   find_flag = 0                                   #默认表示没有找到
    modify_flag = 0                                 #判断是否修改成功，默认修改失败
#   sign = 0
    for temp in card_infors:
#       sign+=1
        if modify_name == temp["name"]:
#           find_flag = 1
            print("1.修改姓名")                     #打印修改菜单
            print("2.修改QQ")
            print("3.修改weixin")
            print("4.修改地址")
            print("5.退出修改系统")
            while True:
                num2 = int(input("请输入你要修改的信息的编号：")) #输入修改项对应的编号
                if num2==1:
#                   card_infors[sign-1]["name"] = input("请输入您要修改的正确姓名：")  #在对应的修改编号下修改相应的信息
                    temp["name"] = input("请输入您要修改的正确姓名：")
                    modify_flag = 1
                elif num2==2:
#                   card_infors[sign-1]["qq"] = input("请输入您要修改的正确QQ：")
                    temp["qq"] = input("请输入您要修改的正确QQ：")
                    modify_flag = 1
                elif num2==3:
#                   card_infors[sign-1]["weixin"] = input("请输入您要修改的正确weixin：")
                    temp["weixin"] = input("请输入您要修改的正确weixin：")
                    modify_flag = 1
                elif num2==4:
#                   card_infors[sign-1]["addr"] = input("请输入您要修改的正确地址：")
                    temp["addr"] = input("请输入您要修改的正确地址：")
                    modify_flag = 1
                elif num2==5:
                    break
                else:
                    print("输入有误，请重新输入:")
                if modify_flag == 1:                #判断是否修改成功
                    print("修改成功！")
                    break
            break
"""需要注意的一个地方是，如果你用的版本是3.6的，那么下面的用到的所有从外界接收信息所用到的input()用input()就行了，如果是2.7版本，那么如果接收的是字符串要用raw_input()(将接收到的信息自动转化为字符串，即使你输入的是12345那也是字符串12345)"""

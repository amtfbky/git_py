# 把用户输入的信息罗列出来
# 把一个定义好的字典信息遍历


def demo(**person):
    for person_info in person:
#         print("%s 的信息为：姓名：%s"
#               "             年龄：%s"
#               "             性别：%s"
#                             % ((person_info[0],
#                                 person_info[0],
#                                 person_info[1],
#                                 person_info[2])))
#                                 
          # 一句代码OK

          print("%s : %s" % (person_info, person[person_info]))

# dic_in = {"name": input("请输入您的姓名："),
#             "age": input("请输入您的年龄："),
#             "gender": input("请输入您的性别：")}

# key可以是中文
dic_in = {"姓名": input("请输入您的姓名："),
            "年龄": input("请输入您的年龄："),
            "性别": input("请输入您的性别：")}

demo(**dic_in)

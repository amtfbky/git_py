poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for s in poem:
    # 这种样式把center的width参数设成10
    #print(s.center(10))

    # 这种是把在两边各加一竖杠
    #print("|%s|" % s.center(10))

    # 这种是在width参数后面再加一个中文全角的空格符号，就比较漂亮了
    #print("|%s|" % s.center(10, "　"))

    # 竖杠、width=10、全角空格，左对齐
    #print("|%s|" % s.ljust(10, "　"))

    # 竖杠、width=10、全角空格，右对齐
    print("|%s|" % s.rjust(10, "　"))

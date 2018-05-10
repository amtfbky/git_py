def sum_number(num):
    print(num)

    # 出口
    if num == 1:
        return

    sum_number(num - 1)

    print("完成 %d" % num)

sum_number(3)

def multiple_table():
    i = 1
    while i < 10:
        j = 1
        while j <= i:
            """每一行要打印的就是i的数字就是行数，共9行
               每一列要打印的是j的循环，当i=1时，j就循环一次，当i=2时，j循环2次，依次递增"""
            print("第%d列*第%d行=%d" % (j, i, (i*j)), end="\t")
            j += 1
        i += 1
        print("")

def creatNum():
    print("--------start-------")
    a,b = 0,1
    for i in range(5):
        print("----1----")
        yield b
        print("----2----")
        a,b = b,a+b
        print("----3----")
    print("--------stop-------")


a = creatNum()
# 当这样循环时，数据显示完成后不会报错，点解？
for n in a:
    print(n)

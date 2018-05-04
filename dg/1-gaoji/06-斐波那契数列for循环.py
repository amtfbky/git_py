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
for n in a:
    print(n)

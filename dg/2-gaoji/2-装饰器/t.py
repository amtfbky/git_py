def w1(func):
    def inner():
        print("-----quanxian-----")

        func()
    return inner

@w1
def f1():
    print("----f1-----")


f1()

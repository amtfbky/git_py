def test1():
    while True:
        print("-----1------")
        yield None

def test2():
    while True:
        print("-----2------")
        yield None


t1 = test1()
t2 = test2()

while True:
    t1.__next__()
    t2.__next__()

# 这就是协程，还有进程和线程

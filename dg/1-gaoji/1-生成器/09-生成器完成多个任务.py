# 这里有三个死循环，协程进行工作
# 不断先后打印1和2
def test1():
    while True:
        print("-----1------")
        # 并用一个生成器管制着一次只生成一个数据，这样子不会造成内存压力
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

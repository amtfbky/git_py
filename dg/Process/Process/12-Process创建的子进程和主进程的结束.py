from multiprocessing import Process
import time

# 跨平台的写法，以后不用fork了
def test():
    # while True: 
    for i in range(5):
        print("----test---")
        time.sleep(1)

p = Process(target=test)
# 让这个进程开始执行test函数里的代码
p.start()

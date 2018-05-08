from multiprocessing import Process
import time
import random


def test():
    for i in range(random.randint(1,5)):
        print("---%d---"%i)
        time.sleep(1)


p = Process(target=test)
p.start()
#p.join()    # 堵塞，等到堵塞通了主进程才能往下走？
p.join(1)   # 增加timeout时间，就给你一秒，过了一秒就执行
print("----main----")



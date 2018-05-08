from multiprocessing import Pool
import os
import random
import time


def worker():
    for i in range(5):
        print("---pid = %d---"%os.getpid())
        #print("++++++%d+++++"%i)
        time.sleep(1)

p = Pool(3)

for i in range(10):
    print("---%d---"%i)
    p.apply_async(worker)


p.close()   # 关闭进程池，关闭后p不再接收新的请求
p.join()    # 等待p中所有子进程执行完毕，必须放在close语句之后

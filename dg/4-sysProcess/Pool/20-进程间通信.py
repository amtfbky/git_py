from multiprocessing import Process, Queue
import os
import time
import random

# 写入数据进程
def write(q):
    for value in ['A', 'B', 'C']:
        print("Put %s to queue..." % value)
        q.put(value)
        time.sleep(random.random())

# 读取数据进程
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("Get %s from queue." % value)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    # 父进程创建Queue,并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    # 启动子进程，写入
    pw.start()

    # 等待pw结束
    pw.join()

    # 启动子进程pr，读取
    pr.start()
    pr.join()

    # pr进程里是死循环，无法等待其结果，只能强行终止
    print("")
    print("所有数据都写入且读完")

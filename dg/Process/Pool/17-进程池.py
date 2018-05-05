from multiprocessing import Pool
import os
import random
import time


def worker(num):
    for i in range(5):
        print("---pid = %d--num = %d-"%(os.getpid(), num))
        #print("++++++%d+++++"%i)
        time.sleep(1)

# 3表示进程池中最多有3个进程一起执行
p = Pool(3)

for i in range(10):
    print("---%d---"%i)

    """向进程池添加任务：
    注意：如果添加的任务数量超过了池中的进程个数，那么不会导致添加不进去
          添加到进程中的任务，如果还没有执行的话，那么此时他们会等待池中的进程完成一个任务后，
          自动去用刚刚的那个进程，完成当前的任务"""
    p.apply_async(worker, (i,))


p.close()   # 关闭进程池，关闭后p不再接收新的请求，不能再添加新任务了
"""等待p中所有子进程执行完毕，必须放在close语句之后
   主进程创建/添加任务后，默认不会等待池中的任务执行完后才结束；
   而是当主进程的任务做完之后，立马结束，如果这个地方没有join，会导致池中的任务不会执行"""
p.join()

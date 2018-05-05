import os
import time

ret = os.fork()
if ret == 0:    # 子进程ret=0
    while True:
        print("-----我是子进程-----")
        time.sleep(1)
else:           # 父进程ret>0
    while True:
        print("-----我是父进程-----")
        time.sleep(1)

import os

# 父进程
ret = os.fork()
if ret == 0:    # 子进程ret=0
    # 子进程
    print("-----我是子进程--%d-%d---"%(os.getpid(), os.getppid()))
else:           # 父进程ret>0
    # 父进程
    print("-----我是父进程--%d-%d---"%(os.getpid(), os.getppid()))

# 父子进程
ret = os.fork()
if ret == 0:    # 子进程ret=0
    # 孙子
    print("-----我是other子进程--%d-%d--"%(os.getpid(), os.getppid()))
else:           # 父进程ret>0
    # 儿子
    print("-----我是other父进程--%d-%d--"%(os.getpid(), os.getppid()))

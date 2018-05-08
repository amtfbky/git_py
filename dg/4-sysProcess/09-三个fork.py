import os

os.fork()
print("第1次")
os.fork()
print("第2次")
os.fork()
print("第3次")

print("----1--%d-%d--"%(os.getpid(), os.getppid()))

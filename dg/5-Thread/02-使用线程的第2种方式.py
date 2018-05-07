import threading
import time


class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            # name属性中保存的是当前线程的名字
            msg = "I'm "+self.name+' @ '+str(i)


if __name__ = '__main__':
    t = MyThread()
    t.start()

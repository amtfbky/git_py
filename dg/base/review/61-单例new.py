# new方法的重写：
# 1.在内存中为对象分配空间
# 2.返回对象的引用

class MusicPlayer(object):
    def __new__(cls, *a, **b):
        
        1.创建对象时，new方法会被自动调用
        print("new方法创建对象，分配内存空间")

        2.为对象分配空间
        instance = super().__new__(cls)

        3.返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化...")


# 创建播放器对象
player = MusicPlayer()

print(player)

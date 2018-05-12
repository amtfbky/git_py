# 知识点：一个对象的属性，可以是另一个类创建的对象
# 第一步：设计枪类
# 第二步：设计士兵类

class Gun:
    """枪类"""

    def __init__(self, model):
        # 1.枪的型号
        self.model = model

        # 2.子弹的数量，初始为0
        self.bullet_count = 0

    def add_bullet(self, count):
    # 把子弹数量的形参count传进来
        self.bullet_count += count

    def shoot(self):
        # 1.判断子弹数量
        if self.bullet_count <= 0:
            # 提示没有子弹
            print("哥们，[%s]还没有装子弹呢！" % self.model)
            return

        # 2.发射子弹，-1
        self.bullet_count -= 1

        # 3.显示发射信息
        print("[%s] 哒哒哒...[剩%d发]" % (self.model, self.bullet_count))


class Soldier:
    """士兵类"""

    def __init__(self, name):
        self.name = name
        # 2.gun，这里就是把枪类创建的对象当做属性
        # 当不知道怎么给这个属性赋值时，就赋值None
        self.gun = None


# 创建枪对象
ak47 = Gun("Ak47")

# 装填子弹
ak47.add_bullet(50)
# 发射
ak47.shoot()

# 创建士兵对象
gemen = Soldier("汤姆")
# 显示枪的信息，此时还没有枪，那怎么把枪交给士兵呢？
#print(gemen.gun)

# 这里就是关键点了，把枪交给士兵，就是给gun属性赋值
gemen.gun = ak47
# 此时，已经把枪给士兵了，已经有了枪对象
print(gemen.gun)

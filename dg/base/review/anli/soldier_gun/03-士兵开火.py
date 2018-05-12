# 知识点：一个对象的属性，可以是另一个类创建的对象
# 一旦把一个对象引用赋值给另一个对象的属性
# 就可以调用前者里面的方法，如此例的装填和发射子弹
# 第一步：设计枪类
# 第二步：设计士兵类
# 第三步：士兵开火

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

    def fire(self, count):
        # 1.判断士兵是否有枪
        if self.gun is None:
            print("啊哦！哥们咋还没枪呢！")
            return
        
        # 2.高喊口号
        print("[%s]，冲啊..." % self.name)
        
        # 3.让枪装填子弹，这里就是调用了枪类里的方法，下同
        self.gun.add_bullet(count)

        # 4.让枪发射子弹
        self.gun.shoot()

# 创建枪对象
ak47 = Gun("Ak47")

# 创建士兵对象
gemen = Soldier("汤姆")

# 把枪交给士兵
gemen.gun = ak47
# 士兵装填子弹并开火
gemen.fire(50)
print(gemen.gun)

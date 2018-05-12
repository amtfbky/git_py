# 知识点：一个对象的属性，可以是另一个类创建的对象
# 第一步：设计枪类

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


# 创建枪对象
ak47 = Gun("Ak47")

# 装填子弹
ak47.add_bullet(50)
# 发射
ak47.shoot()

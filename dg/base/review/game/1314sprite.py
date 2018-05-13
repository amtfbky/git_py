# 敌机出场第四步随机出现1：导入random模块这是官方标准模块，在上
import random
# pygame是第三方模块，在下
import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新的帧率
FRAME_PER_SEC = 60
# 敌机出场第一步1：设置创建敌机的定时器常量
CREATE_ENEMY_ENENT = pygame.USEREVENT
# 玩家出场第六步2：玩家发射子弹事件常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


# pygame.sprite.Sprite内置创建精灵的类？
class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 1.如果该类没有调用object，则要调用父类的init方法
        super().__init__()

        # 2.定义对象的属性
        self.image = pygame.image.load(image_name)  # 精灵图像
        self.rect = self.image.get_rect()           # 精灵背景
        self.speed = speed                          # 精灵速度，缺省是1

    def update(self):

        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed
        

class Background(GameSprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):
        # 1.调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")
        # 2.判断上方是交替图像，如果是，需要设置初始位置
        if is_alt:
            self.rect.y = -self.rect.height

    # 重写父类的update方法
    def update(self):
        # 1.调用父类的方法实现
        super().update()

        # 2.判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height

# 敌机出场第二步：创建敌机类
class Enemy(GameSprite):
    """敌机精灵"""

    def __init__(self):
        super().__init__("./images/enemy1.png")
        # 敌机出场第四步随机出现2:随机速度
        self.speed = random.randint(1, 3)
        # 敌机出场第四步随机出现3:
        # 垂直方向随机
        self.rect.bottom = 0
        # 水平方向随机
        # max_x = 窗口宽度-敌机图像宽度
        max_x = SCREEN_RECT.width - self.rect.width
        # 从0到max_x之间随机水平出现敌机
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            #print("飞出屏幕，需要从精灵组删除...")
            # 敌机出场第五步2：销毁飞出屏幕的敌机，空出内存
            # kill方法将精灵从所有精灵组中移出，精灵就会被自动销毁
            self.kill()

    # 敌机出场第五步1：销毁飞出屏幕的敌机，空出内存
    # del方法没有销毁
    def __del__(self):
        #print("敌机挂了...%s" % self.rect)
        pass


# 玩家出场第一步1：设计玩家类
class Hero(GameSprite):
    """玩家精灵"""

    def __init__(self):
        # 1.调用父类方法，设置image&speed
        super().__init__("./images/me1.png", 0)
        # 2.设置玩家的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

        # 3.玩家出场第七步2:创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    # 玩家出场第四步1：设置玩家水平移动方法
    def update(self):

        # 玩家水平移动
        self.rect.x += self.speed

        # 玩家出场第五步：控制玩家不能离开屏幕
        if self.rect.x < 0:
            # 当玩家左侧<0，就让玩家x值=0
            self.rect.x = 0
        # 当玩家右侧>屏幕右侧，就让玩家右侧x值=屏幕右侧
        elif self.rect.right > SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):
        #print("shoot bullet...")

#         # 玩家出场第七步4-1：发射单枚子弹
#         # 1.创建子弹精灵
#         bullet = Bullet()
#         # 2.设置精灵的位置
#         bullet.rect.bottom = self.rect.y - 20
#         bullet.rect.centerx = self.rect.centerx
#         # 3.将精灵添加到精灵组
#         self.bullets.add(bullet)

        # 玩家出场第七步4-2：发射3枚子弹
        for i in (0, 1, 2):
            # 1.创建子弹精灵
            bullet = Bullet()
            # 2.设置精灵的位置
            bullet.rect.bottom = self.rect.y - i*20
            bullet.rect.centerx = self.rect.centerx
            # 3.将精灵添加到精灵组
            self.bullets.add(bullet)

# 玩家出场第七步1：设计子弹精灵类
class Bullet(GameSprite):
    """子弹精灵"""

    def __init__(self):
        super().__init__("./images/bullet1.png", -2)

    def update(self):
        super().update()

        if self.rect.bottom < 0:
            self.kill()

    def __del__(self):
        #print("bullet was kill...")
        pass

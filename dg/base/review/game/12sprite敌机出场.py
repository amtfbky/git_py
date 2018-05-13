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
            print("飞出屏幕，需要从精灵组删除...")
            # 敌机出场第五步2：销毁飞出屏幕的敌机，空出内存
            # kill方法将精灵从所有精灵组中移出，精灵就会被自动销毁
            self.kill()

    # 敌机出场第五步1：销毁飞出屏幕的敌机，空出内存
    # del方法没有销毁
    def __del__(self):
        print("敌机挂了...%s" % self.rect)

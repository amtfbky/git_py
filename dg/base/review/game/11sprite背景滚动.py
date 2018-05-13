import pygame

# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
FRAME_PER_SEC = 60


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

# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time
import random

class Base(object):
    """飞机和子弹的基类
        screen_temp:初始屏幕
        x:引用图片的x坐标，取左上角的值
        y:引用图片的y坐标，取左上角的值
        image_name:游戏引用图片"""

    # 定义Base的init方法
    def __init__(self, screen_temp, x, y, image_name):
    
        self.x = x
        self.y = y
        self.screen = screen_temp
        self.image = pygame.image.load(image_name)    

class BasePlane(Base):
    """飞机的基类"""
        
    # 飞机基类的init方法
    def __init__(self, screen_temp, x, y, image_name):
    
        # 调用Base的init方法
        Base.__init__(self, screen_temp, x, y, image_name)
        
        # 存储发射出去的子弹对象引用
        self.bullet_list = []

    # 图片的显示方法,包括飞机和子弹
    def display(self):

        # 定义图片的基本属性,图片引用
        self.screen.blit(self.image, (self.x,self.y))

        # 遍历子弹,并调用子弹显示方法和移动方法,删除越界的子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()

            # 判断子弹(包括玩家和敌机发射的子弹)是否越界,这里是调用judge方法
            if bullet.judge():

                # 删除越界子弹
                self.bullet_list.remove(bullet)

class HeroPlane(BasePlane):
    """玩家飞机的类"""

    # 定义玩家飞机的init方法       
    def __init__(self, screen_temp):
   
        # 调用飞机基类的init方法,并给父类该方法里传实参
        BasePlane.__init__(self, screen_temp, 210, 600, "./quanmin/image/hero0.png")
        # super().__init__()

    # 定义玩家飞机向左移动的方法
    def move_left(self):
        self.x -= 5

    # 定义玩家飞机向右移动的方法
    def move_right(self):
        self.x += 5

    # 定义玩家飞机开火方法
    def fire(self):

        # 将玩家飞机发射的子弹(其实是每个子弹的图片)添加到子弹列表
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(BasePlane):
    """敌机的类"""

    # 敌机的init方法
    def __init__(self, screen_temp):
    
        # 调用飞机基类的init方法,并给父类该方法里传实参
        BasePlane.__init__(self, screen_temp, 0, 0, "./quanmin/image/UI.png")
        
        # 用来存储敌机默认的显示方向
        self.direction = "right"
      
    # 定义敌机的移动方法
    def move(self):

        # 判断敌机移动方向向右,坐标+5
        if self.direction == "right":
            self.x += 5
        # 判断敌机移动方向向左,坐标-5
        elif self.direction == "left":
            self.x -= 5

        # 判断敌机坐标,不能> 450
        if self.x > 450:
            # 让敌机在到达450位置时向左移动
            self.direction = "left"
        # 判断敌机坐标,不能< 0
        elif self.x < 0:
            # 让敌机在到达0位置时向右移动
            self.direction = "right"
    
    # 定义敌机开火方法
    def fire(self):

        # 定义1到200之间一个随机数,让敌机子弹在这个随机数出现时才显示
        random_num = random.randint(1, 200)

        #if random.randint(1, 100) == 78:
        # 换下面写法不会出现随机同时出现几颗子弹,当随机数是8或者20(这样子频率比只有一个随机数的来的低)的时候,子弹才会显示
        if random_num == 8 or random_num == 20:

            # 将敌机发射的子弹(其实是每个子弹的图片)添加到子弹列表
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

class BaseBullet(Base): 
    """子弹的基类"""

    # 定义子弹基类的init方法
    def __init__(self, screen_temp, x, y, image_name):
        
        # 调用Base的init方法
        Base.__init__(self, screen_temp, x, y, image_name)
        
    # 定义子弹图片的显示方法
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))             
        
class Bullet(BaseBullet):
    """定义玩家发射子弹类"""

    # 玩家子弹的init方法
    def __init__(self, screen_temp, x, y):
        
        # 调用子弹基类的init方法,并给父类该方法里传实参
        BaseBullet.__init__(self, screen_temp, x+55, y-40, "./quanmin/button_green.9.png")
        
    # 定义玩家飞机发射的子弹的移动方法
    def move(self):
        self.y -= 5

    # 定义玩家子弹是否越界的方法
    def judge(self):
        # 判断玩家飞机发射的子弹是否越界
        if self.y < 0:
            # 如果越界返回真,即在飞机基类调用该方法时删除越界的子弹
            return True
        else:
            # 如果未越界返回假,则子弹不会被删除
            return False

class EnemyBullet(BaseBullet):
    """定义敌机发射子弹类"""

    # 敌机子弹的init方法
    def __init__(self, screen_temp, x, y):
        
        # 调用子弹基类的init方法,并给父类该方法里传实参
        BaseBullet.__init__(self, screen_temp, x+31, y+9, "./quanmin/button_red.9.png")
        
    # 定义敌机发射的子弹的移动方法
    def move(self):
        self.y += 5

    # 定义敌机子弹是否越界的方法
    def judge(self):
        # 判断敌机发射的子弹是否越界
        if self.y > 768:
            # 如果越界返回真,即在飞机基类调用该方法时删除越界的子弹
            return True
        else:
            # 如果未越界返回假,则子弹不会被删除
            return False

# 定义玩家飞机左右移动和发射子弹的按键控制方法,hero_temp参数指向玩家飞机实例            
def key_control(hero_temp):
    # 获取事件，比如按键等
    for event in pygame.event.get():

        # 判断是否点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()

        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                # 按了a键调用玩家飞机向左移动的方法
                hero_temp.move_left()

            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                # 按了d键调用玩家飞机向右移动的方法
                hero_temp.move_right()

            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                # 按了空格键调用玩家飞机开火的方法,这是用按键来控制的,而敌机是默认循环自动开火
                hero_temp.fire()

# 定义主要设置和调配的方法
def main():
    # 设置屏幕,512,768是背景图片的像素也是坐标值,0指?32指?
    screen = pygame.display.set_mode((512,768),0,32)
    # 设置背景图片
    backgroud = pygame.image.load("./quanmin/image/img_bg_level_3.jpg")
    # 创建一个飞机对象
    hero = HeroPlane(screen)
    # 创建一个敌机对象
    enemy = EnemyPlane(screen)

    # 这是游戏的核心,让这些图片不断死循环显示,直到玩家点击退出按钮
    while True:
        # 游戏屏幕调用背景图片
        screen.blit(backgroud,(0,0))

        # 调用玩家飞机图片,实验
        #screen.blit(hero, (x,y))

        # 玩家飞机调用显示方法
        hero.display()
        # 敌机调用显示方法
        enemy.display()
        # 调用敌机的移动方法
        enemy.move()
        # 调用敌机的开火方法
        enemy.fire()
        # 调用游戏的update方法,内置
        pygame.display.update()
        # 调用按键控制方法,针对玩家飞机
        key_control(hero)

        # 控制循环频率的,睡眠时间越大,频率越低
        time.sleep(0.01)

# 设置name方法
if __name__ == "__main__":
    main()

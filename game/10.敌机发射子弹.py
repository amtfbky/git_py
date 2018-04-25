# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time
import random

class HeroPlane(object):
    def __init__(self, screen_temp):
        self.x = 210
        self.y = 600
        self.screen = screen_temp
        self.image = pygame.image.load("./quanmin/image/hero0.png")
        self.bullet_list = [] # 存储发射出去的子弹对象引用

    def display(self):
        self.screen.blit(self.image, (self.x,self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)

    def move_left(self):
        self.x -= 5
    def move_right(self):
        self.x += 5
    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class EnemyPlane(object):
    """敌机的类"""
    def __init__(self, screen_temp):
        self.x = 0
        self.y = 0
        self.screen = screen_temp
        self.image = pygame.image.load("./quanmin/image/UI.png")
        self.bullet_list = [] # 存储发射出去的子弹对象引用
        self.direction = "right"    # 用来存储敌机默认的显示方向

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)
        
    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x > 450:
            self.direction = "left"
        elif self.x < 0:
            self.direction = "right"
    def fire(self):
        random_num = random.randint(1, 200)
        #if random.randint(1, 100) == 78:   # 换下面写法不会出现随机同时出现几颗子弹
        if random_num == 8 or random_num == 20:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))
        
class Bullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 55
        self.y = y - 40
        self.screen = screen_temp
        self.image = pygame.image.load("./quanmin/button_green.9.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

class EnemyBullet(object):
    def __init__(self, screen_temp, x, y):
        self.x = x + 31
        self.y = y + 9
        self.screen = screen_temp
        self.image = pygame.image.load("./quanmin/button_red.9.png")

    def display(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5

    def judge(self):
        if self.y > 768:
            return True
        else:
            return False
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
                hero_temp.move_left()

            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()

            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()
def main():
    screen = pygame.display.set_mode((512,768),0,32)

    backgroud = pygame.image.load("./quanmin/image/img_bg_level_3.jpg")

    # 创建一个飞机对象
    hero = HeroPlane(screen)
    # 创建一个敌机
    enemy = EnemyPlane(screen)
    while True:
        
        screen.blit(backgroud,(0,0))

        #screen.blit(hero, (x,y))
        hero.display()
        enemy.display()
        enemy.move()    # 调用敌机的移动方法
        enemy.fire()    # 敌机开火
        pygame.display.update()
        
        key_control(hero)

        time.sleep(0.01)

if __name__ == "__main__":
    main()

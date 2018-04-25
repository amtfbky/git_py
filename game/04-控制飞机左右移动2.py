# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import time

def main():
    screen = pygame.display.set_mode((512,768),0,32)

    backgroud = pygame.image.load("./quanmin/image/img_bg_level_1.jpg")

    hero = pygame.image.load("./quanmin/image/hero0.png")

    x = 210
    y = 600

    while True:
        
        screen.blit(backgroud,(0,0))

        screen.blit(hero, (x,y))

        pygame.display.update()
        
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
                    x -= 5

                # 检测按键是否是d或者right
                elif event.key == K_d or event.key == K_RIGHT:
                    print('right')
                    x += 5

                # 检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')

        time.sleep(0.01)

if __name__ == "__main__":
    main()

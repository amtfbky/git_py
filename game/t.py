# -*- coding:utf-8 -*-
import pygame
import time

def main():
    screen = pygame.display.set_mode((512,768),0,32)

    backgroud = pygame.image.load("./quanmin/image/img_bg_level_1.jpg")
    
    hero = pygame.image.load("./quanmin/image/hero0.png")

    while True:
        screen.blit(backgroud,(0,0))
        screen.blit(hero,(210,600))
        pygame.display.update()
        time.sleep(0.01)

if __name__ == "__main__":
    main()

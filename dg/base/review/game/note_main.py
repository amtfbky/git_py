"""
import pygame
from plane_sprite import *


class 游戏主程序类(object):
    def __init__(self):
        print("游戏初始化")

        # 1.创建游戏窗口
        # 在精灵模块设置好窗口常量SCREEN_RECT调用size
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        
        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()

        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
    
    # 创建精灵，私有方法
    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = 背景类名()
        bg2 = 背景类名(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

    # 启动游戏方法
    def start_game(self):
        print("游戏开始...")
        while True:
            # 1.设置刷新频率
            self.clock.tick(常量FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    # 监听事件方法
    def __event_handler(self):
        for event in pygame.event.get():
            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                游戏主程序名.__game_over()

    # 检测碰撞方法
    def __check_collide(self):

    # 更新精灵图像方法
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

    # 游戏结束静态方法
    def __game_over(self):
        print("游戏结束...")

        pygame.quit()
        exit()


if __name__ == '__main__':
    
    # 创建游戏对象
    game = 主程序类名()
    # 启动游戏，调用start_game方法
    game.start_game()
    """

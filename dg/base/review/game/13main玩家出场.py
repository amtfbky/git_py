import pygame
from plane_sprite import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")

        # 1.创建游戏窗口
        # 在plane_sprite模块设置好窗口常量SCREEN_RECT调用size
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 2.创建游戏时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组的创建
        self.__create_sprites()

        # 4.设置定时器事件，创建敌机/秒
        pygame.time.set_timer(CREATE_ENEMY_ENENT, 1000)

        # 玩家出场第六步3：创建子弹，每隔0.5秒玩家发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)
    
    # 创建精灵，私有方法
    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)

        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 敌机出场第三步1：创建敌机精灵组
        self.enemy_group = pygame.sprite.Group()

        # 玩家出场第二步2：创建玩家精灵和精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始...")
        while True:
            # 1.设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制精灵组
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()
            
    def __event_handler(self):
        
        for event in pygame.event.get():

            # 判断是否退出游戏
            if event.type == pygame.QUIT:
                PlaneGame.__game_over()# 类名.__方法名
            # 敌机出场第一步2：判断事件
            elif event.type == CREATE_ENEMY_ENENT:
                #print("敌机出场...")

                # 敌机出场第三步2：
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            # 玩家出场第六步4：子弹创建事件监听，触发即创建子弹
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()

            # 玩家出场第三步1：左右移动事件监听方式一
#             elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
#                 print("move to right...")

            # 玩家出场第三步1：左右移动事件监听方式二
            # 使用键盘提供的方法获取键盘按键，返回按键元组
            keys_pressed = pygame.key.get_pressed()
            # 判断元组中对应的按键索引值 1
            if keys_pressed[pygame.K_RIGHT]:
                #print("move to right...")
                # 玩家出场第四步2：设置玩家平移事件监听
                self.hero.speed = 2
            elif keys_pressed[pygame.K_LEFT]:
                self.hero.speed = -2
            else:
                self.hero.speed = 0

    def __check_collide(self):
        pass

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        # 敌机出场第三步3：
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        # 玩家出场第二步3：
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        
        # 玩家出场子弹精灵组第七步3：
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over(self):
        print("游戏结束")

        pygame.quit()
        exit()

if __name__ == '__main__':

    # 创建游戏对象
    game = PlaneGame()
    # 启动游戏
    game.start_game()

import pygame

# 游戏初始化
pygame.init()

# 创建游戏窗口
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0,0))
#pygame.display.update()

hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 574))
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 1.定义rect记录玩家的初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)

# 游戏正式开始...
while True:
    # 指定循环体内部的代码执行的频率
    # 也叫游戏刷新帧率
    clock.tick(24)

    # 7.监听事件
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("游戏退出...")

            # quit卸载所有的模块
            pygame.quit()
            # 退出
            exit()
    
    # 2.修改玩家的位置
    hero_rect.y -= 5

    # 6.判断玩家的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700

    # 3.调用blit方法绘制图像
    # 5.增加背景图像的更新，让玩家图像更新不会留下重影
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 4.调用update方法更新显示
    pygame.display.update()

pygame.quit()

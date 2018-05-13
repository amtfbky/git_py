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

# 游戏正式开始...
while True:
    # 指定循环体内部的代码执行的频率
    # 也叫游戏刷新帧率
    clock.tick(60)
    pass

pygame.quit()

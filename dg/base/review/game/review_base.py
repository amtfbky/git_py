"""首先认识一下游戏的基础知识：
    1.精灵初始位置
    pygame.Rect：精灵尺寸类
    sprite_rect = pygame.Rect(x, y, width, height)
        sprite_rect.x：x轴原点坐标，即精灵左上角位置x值
        sprite_rect.y：y轴原点坐标，即精灵左上角位置y值
        sprite_rect.width：精灵宽度
        sprite_rect.height：精灵高度
        sprite_rect.size：包含了精灵宽度和高度的数值元组
        
    2.游戏窗口
    screen = pygame.display.set_mode((xxx, xxx))
        调用显示游戏窗口设置，包含了几个参数
        这里设置了窗口高度和宽度

    3.绘制精灵图像
    在游戏窗口里绘制背景和游戏精灵图像(背景也是精灵)
        1）加载图像数据
            精灵图像变量名称 = pygame.image.load("Path")
        2）blit绘制图像
            screen.blit(精灵图像变量名, (原点坐标)) # 就是图像出现的位置
        3）更新屏幕显示，固定必须，全部精灵图像绘制完成后统一更新一次
            pygame.display.update()

    4.游戏执行流程
        1）游戏初始化
            pygame.init()
        2）创建游戏窗口
            第2步骤
        3）绘制精灵图像
            第3步骤
        4）创建时钟对象
            为了设置游戏刷新帧率?
            clock = pygame.time.Clock()

        7）5.移动精灵，包括精灵循环出现
        定义精灵的初始位置，为了在下面循环体内移动精灵
            sprite = pygame.Rect(x, y, width, height)

        8）6.创建敌机精灵和精灵组
        8-1)# 敌机精灵
            enemy = 敌机精灵类("Path")
            enemy1 = 敌机精灵类("Path")

        8-2)#敌机精灵组
            enemy_group = pygame.sprite.Group(enemy, enemy1)

        5）游戏开始
            while True:
                # 刷新帧率
                clock.tick(60)      # 1/60秒

                8）6.监听事件
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        print("游戏退出...")

                        # quit卸载所有的模块
                        pygame.quit()
                        # 退出
                        exit()

                7-1)# 修改精灵的位置，移动精灵
                sprite_rect.y -= 5  # 精灵往上移动5个单位

                7-3)# 判断精灵位置，让精灵循环出现
                if sprite.y <= -sprite_rect.height:
                    sprite.y = 游戏窗口高度

                7-2)# 调用blit方法绘制精灵图像
                # 为了不重影，要先绘制背景图像覆盖移动的精灵
                screen.blit(bg, (0, 0))
                screen.blit(sprite, sprite_rect)

                8-2)# 精灵组调用两个方法
                8-2-1)# 所有精灵更新位置
                enemy_group.update()

                8-2-2)# 在screen上绘制所有的精灵
                enemy_group.draw(screen)

                7-2)# 一定要调用更新方法
                pygame.display.update()

        6）游戏退出
            pygame.quit()

新的知识点：从创建敌机开始
敌机出场
    1.分析敌机特点：
        1-1）每隔1秒出现一架敌机
        1-2）飞从屏幕上方，速度不一
        1-3）出现的水平位置不一
        1-4）飞出屏幕下方，不会再出现即删除

    2.利用定时器添加敌机

玩家出场
    1.需求分析
        1-1）玩家出现在屏幕水平中间，距离底部120像素
        1-2）玩家每隔5秒发射一次子弹，每次连发3枚子弹
        1-3）玩家默认不会移动，需要按键(事件监听)左右方向控制
        
    2.子弹需求
        2-1）从玩家正上方发射沿直线上飞
        2-2）飞出屏幕后从精灵组删除

    3.捕获键盘按键两种方式
        一种是:用户必须抬起按键才算一次按键事件，操作灵活性低
       
        一种是:用户按住方向键不放，能持续向某一个方向移动，灵活性高

碰撞检测
    两个精灵组中所有的精灵的碰撞检测
    pygame.sprite.groupcollide(group1, group2, dokill1, dokill2, collided=None) -> Sprite_dict
    如果dokill=True，发生碰撞的精灵将被自动移除
    collided参数是用于计算碰撞的回调函数

    判断某个精灵和指定精灵组中的精灵的碰撞
    pygame.sprite.spritecollide(group1, group2, dokill1, dokill2, collided=None) -> Sprite_list
    如果dokill=True，发生碰撞的精灵将被自动移除
    collided参数是用于计算碰撞的回调函数
    返回精灵组中跟精灵发生碰撞的精灵列表
    """

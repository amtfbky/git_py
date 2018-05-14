"""
# 屏幕大小的常量
# 刷新帧率常量


class 游戏精灵类(pygame.sprite.Sprite):
    # 初始化方法
        # 1.如果该类没有调用object，则调用父类的init方法

        # 2.定义对象的属性
        # 图像
        # 尺寸
        # 速度

    # 图像更新方法
        # 在屏幕的垂直方向移动


class 背景类名(游戏精灵类):
    # 初始化方法
        # 1.调用父类实现精灵的创建(image/rect/speed)
        # 2.判断是否交替图像，如果交替，需要设置初始位置
    
    # 重写父类的update方法
        # 1.调用父类方法实现

        # 2.判断是否移出屏幕，如果移出，将图像设置到屏幕的上方


class 敌机精灵类(游戏精灵类):
    # 初始化方法
        # 1.调用父类方法，创建敌机精灵，同时指定敌机图片
        # 2.指定敌机的初始随机速度
        # 3.指定敌机的初始随机位置

    # 重写父类的update方法
        # 1.调用父类方法，保持垂直方法的飞行
        # 2.判断是否飞出屏幕，如果是，需要从精灵组删除敌机


class 玩家精灵类(游戏精灵类):
    # 初始化方法
        # 1.指定玩家图片
        # 2.初始速度=0
        # 3.定义bullets子弹精灵组保存子弹精灵

    # 重写update方法
        # 1.玩家需要水平移动
        # 2.不能移出屏幕

    # 增加bullets属性，记录所有子弹精灵
    # 增加fire方法，发射子弹


class 子弹精灵类(游戏精灵类):
    # 初始化方法
        # 1.指定子弹图片
        # 2.初始速度=-2，上飞
    # 重写update方法
        # 判断是否飞出屏幕，如果是，从精灵组删除
    """
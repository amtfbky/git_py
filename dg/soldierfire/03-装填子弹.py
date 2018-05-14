class Person(object):
    """人的类"""

    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name

    # 装填子弹第二步：在人类增加装填方法
    def zt_bullet(self, dan_jia_tmp, bullet_tmp):
        """装填子弹"""
        # 弹夹.摁子弹(子弹)，接着在弹夹增加摁子弹方法
        dan_jia_tmp.en_bullet(bullet_tmp)


class Gun(object):
    """枪类"""
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name


class Danjia(object):
    """弹夹类"""
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num#用来记录弹夹最大容量

        # 装填子弹第四步1：在弹夹类初始方法里增加子弹列表
        self.bullet_list = []#用来记录子弹的引用

    # 装填子弹第三步：在弹夹类增加摁子弹方法
    def en_bullet(self, bullet_tmp):
        # 装填子弹第四步2：把子弹添加到子弹列表
        self.bullet_list.append(bullet_tmp)


class Bullet(object):
    """子弹类"""
    def __init__(self, sha_shang_li):
        super(Bullet, self).__init__()
        self.sha_shang_li = sha_shang_li


def main():
    """主程序"""
    # 1.创建士兵对象
    tom = Person("汤姆")
    # 2.创建枪对象
    ak47 = Gun("AK47")
    # 3.创建弹夹对象
    dan_jia = Danjia(60)
    # 4.创建一些子弹
    bullet = Bullet(10)
    # 5.装填子弹
    # 装填子弹第一步：在主程序里增加装填方法
    # 士兵.装填方法(弹夹对象, 子弹对象)
    tom.zt_bullet(dan_jia, bullet)
    # 6.安装弹夹
    # 7.发枪给士兵
    # 8.创建敌人
    # 9.士兵开火

if __name__ == '__main__':
    main()

class Person(object):
    """人的类"""

    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name


class Gun(object):
    """枪类"""
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name


class Danjia(object):
    """弹夹类"""
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num 


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
    # 6.安装弹夹
    # 7.发枪给士兵
    # 8.创建敌人
    # 9.士兵开火

if __name__ == '__main__':
    main()

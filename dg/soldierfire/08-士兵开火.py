class Person(object):
    """人的类"""

    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name
        # 士兵领枪第四步：在人类里增加枪属性
        self.gun = None # 用来保存枪对象的引用
        # 士兵领枪第六步：增加士兵血量属性
        self.hp = 100

    # 装填子弹第二步：在人类增加装填方法
    def zt_bullet(self, dan_jia_tmp, bullet_tmp):
        """装填子弹"""
        # 弹夹.摁子弹(子弹)，接着在弹夹增加摁子弹方法
        dan_jia_tmp.en_bullet(bullet_tmp)

    # 安装弹夹第二步：在人类增加安装方法
    def az_danjia(self, gun_tmp, dan_jia_tmp):
        # 枪.卡入弹夹(弹夹)
        gun_tmp.karu_danjia(dan_jia_tmp)

    # 士兵领枪第二步：在人类增加领枪方法
    def ling_gun(self, gun_tmp):
        # 将增加的枪属性=枪对象
        self.gun = gun_tmp
        
    # 士兵领枪第五步：显示士兵对象信息
    def __str__(self):
        if self.gun:    # 枪属性=枪对象
            return "%s 的血量：%d，他有枪[%s]..." % (self.name, self.hp, self.gun)
        else:
            # 士兵开火第九步：判断敌人血量,当血量<0,提示已挂
            if self.hp > 0:
                return "%s 的血量：%d，他没有枪..." % (self.name, self.hp)
            else:
                return "%s 已挂..." % self.name
    
    # 士兵开火第二步：在人类增加开火方法
    def fire(self, diren):
        # 枪.射击(敌人)
        self.gun.shoot_enemy(diren)

    # 士兵开火第六步：在人类增加敌人掉血方法
    def diao_xue(self, sha_shang_li):
        """根据杀伤力减除血量"""
        self.hp -= sha_shang_li


class Gun(object):
    """枪类"""
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name
        # 安装弹夹第四步：增加弹夹属性
        self.danjia = None  #用来记录弹夹对象的引用

    # 安装弹夹第三步：在枪类增加卡入弹夹方法
    def karu_danjia(self, dan_jia_tmp):
        # 安装弹夹第五步：让弹夹属性=弹夹对象
        self.danjia = dan_jia_tmp

    # 测试枪第二步：判断弹夹，返回不同信息
    def __str__(self):
        if self.danjia: # 弹夹属性=弹夹对象
            # 格式化输出指定对象引用能输出对象信息
            return "枪的信息：%s, %s" % (self.name, self.danjia)
        else:
            return "枪的信息：%s,这把枪没有弹夹..." % self.name
    
    # 士兵开火第三步：射击敌人
    def shoot_enemy(self, diren):
        # 先从弹夹中取子弹
        nums_bullet = self.danjia.eject_bullet()

        # 让子弹射击敌人
        if nums_bullet:
            # 子弹.击中(敌人)
            nums_bullet.jizhong(diren)
        else:
            print("弹夹中没有子弹了...")

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
        
    # 测试弹夹第二步：返回子弹列表数量和弹夹最大容量
    def __str__(self):
        return "弹夹的信息：[%d/%d]" % (len(self.bullet_list), self.max_num)

    # 士兵开火第四步：弹夹弹出子弹,返回子弹
    def eject_bullet(self):
        # 弹出弹夹里的子弹
        if self.bullet_list:
            return self.bullet_list.pop()
        else:
            return None

class Bullet(object):
    """子弹类"""
    def __init__(self, sha_shang_li):
        super(Bullet, self).__init__()
        self.sha_shang_li = sha_shang_li

    # 士兵开火第五步：子弹击中敌人
    def jizhong(self, diren):
        """让敌人掉血"""
        # 敌人.掉血(一颗子弹的威力)
        diren.diao_xue(self.sha_shang_li)


def main():
    """主程序"""
    # 1.创建士兵对象
    tom = Person("汤姆")
    # 2.创建枪对象
    ak47 = Gun("AK47")
    # 3.创建弹夹对象
    dan_jia = Danjia(60)
    # 测试弹夹第三步：多创建一些子弹,用for
    for i in range(15):
        print(i)
        # 4.创建一些子弹
        bullet = Bullet(10)
        # 5.装填子弹
        # 装填子弹第一步：在主程序里增加装填方法
        # 士兵.装填子弹(弹夹对象, 子弹对象)
        tom.zt_bullet(dan_jia, bullet)
    # 6.安装弹夹
    # 安装弹夹第一步：在主程序里增加安装方法
    # 士兵.安装弹夹(枪, 弹夹)
    tom.az_danjia(ak47, dan_jia)
    # 测试弹夹第一步：显示弹夹信息
    # 测试弹夹信息
    # 测试枪第一步：显示枪信息
    print(dan_jia)
    # 测试枪的信息
    print(ak47)
    # 7.发枪给士兵
    # 士兵领枪第一步：士兵.领枪方法(枪)
    tom.ling_gun(ak47)
    # 士兵领枪第三步：测试士兵对象
    print(tom)
    # 8.创建敌人
    enemy = Person("法西斯")
    #print(enemy)   # for test
    # 9.士兵开火
    tom.fire(enemy)
    # 士兵开火第七步：显示敌人信息
    print(enemy)
    # 士兵开火第八步：让士兵再开枪
    print(tom)
    tom.fire(enemy)
    print(enemy)
    print(tom)
    tom.fire(enemy)
    print(enemy)
    print(tom)
    tom.fire(enemy)
    print(enemy)
    print(tom)
    tom.fire(enemy)
    print(enemy)
    print(tom)
    tom.fire(enemy)
    print(enemy)
    print(tom)
    tom.fire(enemy)
    print(enemy)
    print(tom)
    tom.fire(enemy)
    print(enemy)
    print(tom)
    tom.fire(enemy)
    print(enemy)
    print(tom)
    tom.fire(enemy)
    print(enemy)
    print(tom)

if __name__ == '__main__':
    main()

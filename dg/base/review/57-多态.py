class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s 蹦蹦跳跳的玩耍..." % self.name)


class Xtq(Dog):
    def game(self):
        print("%s 飞到天上去玩耍..." % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    # 创建不同的Dog对象，就会产生不同的结果
    # 这在游戏里是常态，背景不变，但用户选择的对象可以随意改变

    def game_with_dog(self, dog):
        print("%s 和 %s 高兴的玩耍..." % (self.name, dog.name))
        dog.game()


#wangcai = Dog("旺财")
xiaotianquan = Xtq("天狗")

xiaoming = Person("小明")
#xiaoming.game_with_dog(wangcai)
xiaoming.game_with_dog(xiaotianquan)

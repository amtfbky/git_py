class Game(object):
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助信息...")

    @classmethod
    def show_top_score(cls):
        print("历史记录最高分:%d" % cls.top_score)

    def start_game(self):
        print("[%s]开始游戏..." % self.player_name)


xm = Game("小明")

# 1.显示帮助信息，不需要访问实例属性和类属性
xm.show_help()

# 2.显示历史最高分，只需要访问类属性
xm.show_top_score()

# 3.创建实例，既需要访问实例属性?，又需要访问类属性
xm.start_game()

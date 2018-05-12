class Women:
    def __init__(self, name):

        self.name = name

        self.__age = 18

    def __secret(self):
        print("my age is %d" % self.__age)


xiaofang = Women("小芳")

#print(xiaofang.__age)

xiaofang.__secret()

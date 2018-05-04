class Cat:
    """定义了一个Cat类"""

    def eat(self):
        print("%s在吃鱼..."%self.name)

    def drink(self):
        print("%s正在喝水..."%self.name)

    def introduce(self):
        #print("%s info: %d"%(tom.name,tom.age))
        print("%s info: %d"%(self.name,self.age))

tom = Cat()

# 获取属性的第一种方式
#print("%s info: %d"%(tom.name,tom.age))
tom.name = "汤姆"
tom.age = 40
tom.eat()
tom.drink()
tom.introduce()
# 获取属性的第二种方式：self（可以写成其他，但约定俗成都写self）
jiafei = Cat()
jiafei.name = "加菲"
jiafei.age = 50
jiafei.eat()
jiafei.drink()
jiafei.introduce()



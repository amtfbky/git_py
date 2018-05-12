# self.weight -= 0.5,self.weight += 1
# print(xm),print(girl)

class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "%s weight is %.2f Kg." % (self.name, self.weight)

    def run(self):
        # 这里的weight变量是局部变量，要在函数内重新定义
        weight = 0.5
        self.weight -= weight
        #weight -= self.weight  # Oh!MyGod
        #self.weight -= weight  # OMG2
        #self.weight -= 0.5
        print("%s love run..." % self.name)

    def eat(self):
        weight = 1
        self.weight += weight
        #weight += self.weight
        #self.weight -= weight
        #self.weight += 1
        print("%s love eat too..." % self.name)

xm = Person("小明", 75)
xm.run()
xm.eat()
print(xm)

girl = Person("小美", 60)
girl.run()
girl.eat()
print(girl)
# 最后一句说明小明和小美两个对象之间的方法是互不影响的
print(xm)

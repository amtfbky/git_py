class Animal:
    def eat(self):
        print("------eat------")
    def drink(self):
        print("------drink------")
    def sleep(self):
        print("------sleep------")
    def run(self):
        print("------run------")

class Dog(Animal):
    def bark(self):
        print("======Wang...=====")

class Xtq(Dog):
    def bark(self):
        print("***xiaotianquan's wang") # 重写方法
        #Dog.bark(self)  # 一定要加上self参数,第一种调用被重写的父类方法
        super().bark()  # 第二种调用被重写的父类方法
    def fly(self):
        print("I can fly...")

class Cat(Animal):
    def catch(self):
        print("++++++Catch rat++++")


wangcai = Dog()
wangcai.eat()

jiafei = Cat()
jiafei.drink()

xtq = Xtq()
xtq.fly()
xtq.eat()
xtq.bark()

class Animal:
    def eat(self):
        print("-----eat-------")


class Dog(Animal):
    def bark(self):
        print("------wang-----")


class Xtq(Dog):
    def fly(self):
        print("------fly-------")

    def bark(self):
        print("-----God-------")

        # 在Python2使用，Python3还支持
        # 如果一旦用当前子类名，会死循环
        # Xtq.bark(self)
        #Dog.bark(self)

        # 推荐使用
        super().bark()

        print("$#@$#@$#!@$#!$")


xtq = Xtq()

xtq.bark()

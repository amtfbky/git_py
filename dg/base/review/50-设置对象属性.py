class Cat:
    def __init__(self, name, age):

        print("__init__会自动初始化")
        # 把对象属性封装在__init__方法里
        self.name = name
        self.age = age

    def eat(self):
        print("----%s[age=%d] eating-------" % (self.name, self.age))
        print(type(self.age))

info_input = Cat(input("name:"), int(input("age:")))
info_input.eat()

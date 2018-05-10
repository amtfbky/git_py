class Cat:
    def __init__(self, name, age):

        print("__init__会自动初始化")
        # 把对象属性封装在__init__方法里
        self.name = name
        self.age = age

    def eat(self):
        print("----%s[age=%d] eating-------" % (self.name, self.age))
        print(type(self.age))

    def __del__(self):
        print("baibai...")


info_input = Cat(input("name:"), int(input("age:")))
info_input.eat()

# 如果在这里del一个对象，系统会自动调用类里的del方法
del info_input
print("*" * 42)
# 如果没有在这里del，那系统会在程序执行完毕后调用del

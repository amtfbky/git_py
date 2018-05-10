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

    def __str__(self):
        "这是开发中要查看设置的初始化属性值"

        # 但要在创建类对象后打印对象才能显示返回的字符串
        return "I'm [%s and %d old],What's up?" % (self.name, self.age)

info_input = Cat(input("name:"), int(input("age:")))
#info_input = Cat("Tom", 50)
print(info_input)

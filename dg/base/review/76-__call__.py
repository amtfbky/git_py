class Animal(object):
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs
        self.stomach = []

    def __call__(self, food):
        self.stomach.append(food)

    def poop(self):
        if len(self.stomach) > 0:
            return self.stomach.pop(0)

    def __str__(self):
        return "A animal named %s" % self.name


cow = Animal("King", 4)
dog = Animal("Floop", 4)    #we can make many animals

print("cow %s,dog %s,both have %s legs" % (cow.name, dog.name, cow.legs))
print(cow)  # here __str__ method work

# give food to cow
cow("gras")
print(cow.stomach)

# give food to dog
dog("bone")
dog("beef")
print(dog.stomach)

# what comes inn most come out
print(cow.poop())
print(cow.stomach)  # empty stomach
"""Python中有一个有趣的语法，只要定义类型的时候，实现__call__函数，这个类型就成为可调用的。
换句话说，我们可以把这个类型的对象当作函数来使用，相当于 重载了括号运算符。"""

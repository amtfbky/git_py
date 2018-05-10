class Cat:
    def eat(self):
        print("------eat-------")
    def drink(self):
        print("------drink-------")


tom = Cat()
tom.eat()
tom.drink()

jiafei = Cat()
jiafei.eat()
jiafei.drink()

print(tom)
print(jiafei)
jiafei2 = jiafei
print(jiafei2)

class Cat:
    def eat(self):
        print("------eat-------")
    def drink(self):
        print("------drink-------")


tom = Cat()
tom.eat()
tom.drink()

print(tom)
addr = id(tom)
print("%d" % addr)
print("%x" % addr)

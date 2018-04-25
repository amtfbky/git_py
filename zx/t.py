class Cat:
    def __init__(self,new_name,new_age):
        self.name = new_name
        self.age = new_age

    def __str__(self):
        return "%s info:%d"%(self.name,self.age)

    def eat(self):
        print('eat')

    def introduce(self):
        print("%s info:%d"%(self.name,self.age))

tom = Cat(str(input('name:')),int(input('age:')))
tom.introduce()

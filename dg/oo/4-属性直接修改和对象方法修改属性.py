"""这是让在对象引用方法时修改对象的属性，比较安全？"""
class Dog:
    def set_age(self,new_age):
        if new_age>0 and new_age<=100:
            self.age = new_age
        else:
            self.age = 0
    
    def get_age(self):
        return self.age

dog = Dog()
#dog.age = 10
#dog.name = "xiaobai"
#print(dog.age)

dog.set_age(10)
age = dog.get_age()
print(age)
#dog.get_name()

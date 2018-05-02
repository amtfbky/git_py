# 给Person类动态添加属性和方法属性（即把类外面的方法函数添加成属性）
import types
class Person(object):
	def __init__(self, newName, newAge):
		self.name = newName
		self.age = newAge

	def eat(self):
		print("----%s正在吃----"%self.name)

def run(self):
	print("-----%s正在跑-----"%self.name)

@staticmethod
def test():
	print("-----static method------")

@classmethod
def printNum(cls):
	print("------class method------")


p1 = Person("p1", 10)
p1.eat()

# 在没有import之前，下面的代码是无法添加run属性的
#p1.run = run
# import types后，再把run方法用下面代码添加到p1里
p1.run = types.MethodType(run, p1)
p1.run()

#p1.test = staticMethod
Person.test = test
Person.test()

Person.printNum = printNum
Person.printNum()
	

class Person(object):
	__slots__ = ("name", "age")


p1 = Person()
p1.name = "laowang"
p1.age = 88
# 这里再添加addr属性就报错了
#p1.addr = "beijing"

print(p1.name)
print(p1.age)
	

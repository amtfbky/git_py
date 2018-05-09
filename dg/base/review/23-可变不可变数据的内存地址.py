# 列表变量的内存地址
a = [1,2,3]

print(id(a))
a.append(99)
print(a)
print(id(a))
a.remove(2)
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))

a = []
print(id(a))

print("*" * 30)
# 字典变量的内存地址
d = {"name":"xiaoming"}
print(id(d))
d["age"] = 18
print(d)
print(id(d))
d.pop("age")
print(d)
print(id(d))
d.clear()
print(d)
print(id(d))
d = {}
print(id(d))

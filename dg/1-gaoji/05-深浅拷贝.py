import copy
a=[1,2,3]
c=copy.deepcopy(a)
print(id(a))
print(id(c))
a.append(4)
print("a=%s"%a)
print("c=%s"%c)
b=a
print("b=%s"%b)
print("c=copy.deepcopy(a)深拷贝，b=a浅拷贝")

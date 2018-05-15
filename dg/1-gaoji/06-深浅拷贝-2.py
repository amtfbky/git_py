import copy
a=[1,2,3]
b=[4,5,6]
c=[a,b]
e=copy.deepcopy(c)
print(id(c))
print(id(e))
a.append(4)
print(c[0]) #[1,2,3,4]
print(e[0]) #[1,2,3]
print("列表深拷贝")
print("=" * 30)
# 列表深拷贝id不同，拷到第二层
f=copy.copy(c)
print(id(c))
print(id(f))
a.append(5)
print(c[0])
print(f[0])
print("列表copy拷贝")
print("=" * 30)
# 列表copy拷到第二层，并同步改动

g=(a,b)
h=copy.deepcopy(g)
print(id(g))
print(id(h))
a.append(6)
print(g[0])
print(h[0])
print("元组深拷贝")
print("=" * 30)
# 元组深拷贝拷到第二层，但不同步改动

i=copy.copy(g)
print(id(g))
print(id(i))
a.append(7)
print(g[0])
print(i[0])
print("元组copy拷贝")
# 元组copy拷到第一层，同步改动

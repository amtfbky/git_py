import copy

a = [1, 2, 3]
b = [4, 5, 6]
c = (a, b)

e = copy.copy(c)

print(id(c))
print(id(e))

a.append(4)
print(c[0])
print(e[0])
print("元组不可变,copy只拷到第一层，即只拷贝了标签")

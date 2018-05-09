hello = "hello world"

# 1.判断是否以指定字符串开始
print(hello.startswith("he"))

# 2.判断是否以指定字符串结束
print(hello.startswith("ld"))

# 3.查找指定字符串
# index同样是查找指定字符串的索引，但如果不存在则报错
# find则返回-1
print(hello.find("llo"))
print(hello.find("abc"))

# 4.替换字符串
# replace不会修改原有的字符串的内容，只会返回一个新的字符串
print(hello.replace("world", "python"))
print(hello)

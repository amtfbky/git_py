hello = "hello hello"

# 1.统计字符串长度
print(len(hello))

# 2.统计某一个小字符串出现的次数
print(hello.count("llo"))
# 如果小字符串不存在，统计值为0
print(hello.count("abc"))

# 3.某一个子(小)字符串出现的位置
print(hello.index("llo"))
# 如果子字符串不存在，则报错
#print(hello.index("abc"))

# python针对字符串的方法很多

info_tuple = ("zhangsan", 18, 18, 1.75)

print(type(info_tuple))
print(info_tuple[0])
print(info_tuple.index("zhangsan"))
print(info_tuple.count(18))
print(len(info_tuple))

#for i in info_tuple:
    # 使用格式字符串拼接i这个变量不方便！
    # 因为元组里面的数据类型通常是不同的
"""
empty_tuple = ()
print(type(empty_tuple))


single_tuple = (5)
print(type(single_tuple))


single_tuple2 = (5,)
print(type(single_tuple2))
"""

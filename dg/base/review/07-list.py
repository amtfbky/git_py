list_name = ["zhangsan", "lisi", "wangwu", "lisi", "lisi"]

list_name.append("xiaomei")
list_name.insert(1, "张嘎")
list_name2 = ["猪八戒", "孙悟空", "猪八戒", "沙僧"]
list_name.extend(list_name2)

list_name.remove("xiaomei")
list_name.pop()
list_name.pop(0)
#list_name.clear()

# del将变量从内存中删除
# 后续的代码就不能再使用这个已删除的变量
del list_name[1]
list_len = len(list_name)
print("列表的名单数量：%d" % list_len)
count = list_name.count("lisi")
print("列表中lisi出现的次数：%d次" % count)

# 从列表中删除第一次出现的数据，如果数据不存在，则报错
list_name.remove("猪八戒")
print(list_name)

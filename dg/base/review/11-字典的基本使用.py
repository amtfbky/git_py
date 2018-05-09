xiaoming = {"name":"小明", }

# 取值
print(xiaoming["name"])

# 增加/修改
xiaoming["age"] = 18
# 修改的时候如果key不存在，则报错
xiaoming["name"] = "小亮"

# 删除
# 如果key不存在，则报错
# xiaoming.pop("age")

# 1.统计键值对数量
print(len(xiaoming))

# 2.合并字典
# 注意:如果原字典里有相同key，则会覆盖原值
temp = {"gender":True, "age":20}
xiaoming.update(temp)

# 3.清空字典
# xiaoming.clear()

# 4.迭代遍历字典
# k为key
for k in xiaoming:
    print("%s - %s" % (k, xiaoming[k]))

print(xiaoming)

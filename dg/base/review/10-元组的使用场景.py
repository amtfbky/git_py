# 第一种，格式化字符串
info_tuple = ("小明", 18, 1.75)
print("%s 年龄是：%d，身高是： %.2f。" % info_tuple)

info_str = "%s 年龄是：%d，身高是： %.2f。" % info_tuple
print(info_str)


# 第二种，列表转换成元组，然后不可变
list_num = [1,2,3,4]
print(type(list_num))

tuple_num = tuple(list_num)
print(type(tuple_num))

# 再转回列表，可变
list_num2 = list(tuple_num)
print(type(list_num2))

# 第三种，是函数的参数，这会在以后的函数高级里讲到

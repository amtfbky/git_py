a = [1, 2, 3]

del a[1]
print(a)

del(a[1])
print(a)

# 如果把a删除则报错了
#del(a)
#print(a)

t = "afdafdlajkfjdjdksakfljfzfdsaffdas"
l = [1, 5, 8, 78]

print(max(t))
print(min(t))
print(max(l))
print(min(l))


d = {"a":"z", "b":"y", "c":"x"}
print(max(d))
print(min(d))

# cmp("1", "2") # Python3取消了cmp方法
# 怎么比较大小呢？
def dxbj(a, b):
    #return "a" < "b"
    return a < b

res = dxbj(1, 2)
print(res)
res = dxbj("aaa", "bbb")
print(res)
res = dxbj([1,1,1], [2,2,2])
print(res)
res = dxbj((1,1,1), (2,2,2))
print(res)
# 字典不是不能比较大小吗？这里为何返回True呢？
# 当我把return "a" < "b"引号去掉，就提示字典不能比较大小了！！！！！！！！！
#res = dxbj({"a":"y"}, {"b":"x"})
#print(res)

# =========================================================================

print([0,1,2,3][1:3])
# 元组切片
print((0,1,2,3)[1:3])
# 字典不能切片
#print({"a":1}, {"b":"c"}[1:3])

print([1,2] * 5)
print((1,2) * 5)
# print({"a":1} * 5)

print("hello" + "python")
print((1,2) + (3,4))
# +可以直接输出结果，也就是生成新的列表
print([1,2] + [3,4])
# extend只是把列表传递到被扩展的列表
num_list = [1,2]
num_list.extend([3,4])
print(num_list)

num_list.append(0)
print(num_list)
# append把新列表当成一个元素追加到原列表
num_list.append([8,9])
print(num_list)

# =========================================================================

def xhm(a, b):
    return a in b
    #return a not in b

res = xhm("a", "abc")
print(res)
res = xhm(1, [1,2,4])
print(res)
# 字典的key可以判断是否在字典里
res = xhm("a", {"a":"xiaomei"})
print(res)
# 字典的value不能判断是否在字典里
res = xhm("xiaomei", {"a":"xiaomei"})
print(res)

# =========================================================================

# for-else
for num in [1,2,3]:
    print(num)
    print("*******")
    if num == 2:
        print(num)
        break
else:
    print("当列表被遍历完之后执行到这里！如果在遍历里break，则else不被执行")

print("遍历结束！")


stu = [{"name":"张三"},
        {"name":"李四"}]
find_name = "wangwu"
for s in stu:
    print(s)
    if s["name"] == find_name:
        print("找到了 %s" % find_name)
        break
#     else:
#         print("如果把else写到这里，则会跟着if在for这个循环体里被遍历n次")
else:
    # 如果希望在搜索列表时，所有的字典检查之后，都没有发现需要搜索的目标
    # 还希望看到一个统一的提示！
    print("抱歉没有找到 %s" % find_name)

print("遍历结束！")

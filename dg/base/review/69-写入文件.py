# w覆盖原文件内容,a追加,带+频繁移动指针不推荐使用
file = open("README", "w")

txt = file.read()
print(txt)
print(len(txt))

file.close()

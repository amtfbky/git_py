# 1.获取用户要复制的文件名
old_file_name = input("filename: ")

# 2.打开这个文件(old)
old_file = open(old_file_name,"r")

# 3.新建一个文件(new)
new_file = open("new.txt","w")

# 4.oldxxxx.read()
content = old_file.read()

# 5.newxxxx.write()
new_file.write(content)

# 6.关闭两个文件
old_file.close()
new_file.close()

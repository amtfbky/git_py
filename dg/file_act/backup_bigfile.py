# 1.获取用户要复制的文件名
old_file_name = input("filename: ")

# 2.打开这个文件(old)
old_file = open(old_file_name,"r")

#new_file_name = "[复件]"+old_file_name
position = old_file_name.rfind(".")
new_file_name = old_file_name[:position] + "[复件]" + old_file_name[position:]

# 3.新建一个文件(new)
#new_file = open("new.txt","w")
new_file = open(new_file_name,"w")

# 4.从旧文件中读取数据，一次限定读取1024字节即1K
while True:
    content = old_file.read(1024)

    if len(content)==0:
        break
    # 5.写入新文件中
    new_file.write(content)
# 6.关闭两个文件
old_file.close()
new_file.close()

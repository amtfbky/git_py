import os
# 1.获取要重命名的文件夹名
folder_name = input("请输入要重命名的文件夹：")

# 2.获取制定的文件夹中的所有文件名
file_names = os.listdir(folder_name)
#os.chdir(folder_name)
# 3.重命名
for name in file_names:
    print(name)
    old_file_name = folder_name+"/"+name
    new_file_name = folder_name+"/"+"hh-"+name
    os.rename(old_file_name,new_file_name)

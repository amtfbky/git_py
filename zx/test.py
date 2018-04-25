import os
folder_name = input("wjj:")
file_names = os.listdir(folder_name)

for name in file_names:
    print(name)
    old_file_name = folder_name+"/"+name
    new_file_name = folder_name+"/"+"hh-"+name
    os.rename(old_file_name,new_file_name)

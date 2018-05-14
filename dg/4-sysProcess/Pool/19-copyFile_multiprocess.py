from multiprocessing import Pool,Manager
import os

def copyFileTask(name, oldFolderName, newFolderName, queue):
    "完成copy一个文件的功能"
    fr = open(oldFolderName+"/"+name)
    fw = open(newFolderName+"/"+name, "w")

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(name)

def main():
    # 0.获取原文件夹的名字
    oldFolderName = input("请输入文件夹的名字：")

    # 1.创建一个文件夹
    newFolderName = oldFolderName+"-复件"
    #print(newFolderName)
    os.mkdir(newFolderName)

    # 2.获取原文件夹中所有的文件名字
    fileNames = os.listdir(oldFolderName)
    #print(fileNames)

    # 3.使用多进程的方式copy
    pool = Pool(5)
    queue = Manager().Queue()

    # 遍历文件名并作为元组传参
    for name in fileNames:
        pool.apply_async(copyFileTask, args=(name, oldFolderName, newFolderName, queue))

    num = 0
    allNum = len(fileNames)
    while True:    # 如果死循环，就要设置break跳出
    #while num<allNum:
        queue.get()
        num += 1
        copyRate = num/allNum
        print("\rcopy的进度是：%.2f%%" % (copyRate*100), end="\n")
        if num == allNum:
            break

    print("已完成copy...")
if __name__ == '__main__':
    main()

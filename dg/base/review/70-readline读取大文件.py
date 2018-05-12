import time

f = open("README")

while True:
    t = f.readline()

    # 判断是否读取到内容
    if not t:
        break

    print("---wait 1s")
    time.sleep(1)

    print(t)

f.close()

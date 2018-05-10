# 标记位
exit_flag = False

for i in range(3):
    if i<2:
        continue
    print(i)
    for j in range(4):
        print("layer2", j)
        if j == 2:
            exit_flag = True
            break
        if exit_flag:
            break

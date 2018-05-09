# 假设网上抓取，去除空白字符，再使用 " " 作为分隔符，拼接成整齐字符串

poem = "登鹳雀楼\t 王之涣 \t 白日依山尽 \t\n 黄河入海流 \t\t 欲穷千里目 \t\n 更上一层楼"

#print(poem)

# 1.拆分
poem_list = poem.split()
print(poem_list)

# 2.合并
poem_str = " ".join(poem_list)
print(poem_str)

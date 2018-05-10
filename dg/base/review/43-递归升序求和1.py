def sum_number(num):
    if num ==1:
        # 要返回数字1
        return 1
    return num + sum_number(num - 1)

res = sum_number(100)
print(res)

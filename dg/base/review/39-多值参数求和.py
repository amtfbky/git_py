# 要求：随机罗列几个数字，让这几个数字累加

def sum_n(*nums):
    num = 0
    for n in nums:
        num += n
    return num

res = sum_n(1,2,3,4,5)
print(res)

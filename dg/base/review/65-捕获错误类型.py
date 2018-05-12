
try:
    num = int(input("请输入一个整数："))
    res = 8 / num
    print(res)
except ZeroDivisionError:
    print("除0错误")
except Exception as res:
    print("未知错误 %s" % res)
else:
    print("尝试成功")
finally:
    print("无论是否出现错误都会执行的代码")

print("-" * 42)

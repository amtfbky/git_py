#num = "1"
# 判断小数都为假,还有带特殊小括号的数字(unicode字符串)
#num = "1.1"
#num = "\u00b2"
num = "一千零一"

print(num.isdecimal())  # 全角数字
print(num.isdigit())    # 全角数字，(1)比这个括号要小，\u00b2
print(num.isnumeric())  # 全角数字，汉字数字


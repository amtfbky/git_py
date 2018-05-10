gl_list = [6,3,9]

# 默认是升序，可能用的较多
gl_list.sort()
print(gl_list)
# 当需要降序时，才设置reserve参数
gl_list.sort(reverse=True)
print(gl_list)

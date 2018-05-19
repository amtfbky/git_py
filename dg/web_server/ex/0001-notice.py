"""尝试重写一下，破绽百出，平时学习不严谨"""
# 1.NameError: name 'server_socket' is not defined
# server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 在vim里yy--->p，然后没有检查属性名，把server_socket改成s_socket

# 2.AttributeError: 'HTTPServer' object has no attribute 's_socket'
# s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 落了什么呢？在类里要定义属性应该加上self.
# 好了，加上self.--->self.s_socket

# 3.NameError: name 'handle_c' is not defined
# c_pro = Process(target=handle_c, args=(c_socket,))
# 这里也是和上面一样的错误
# 好了，加上self.--->self.handle_c

# 4.TypeError: Can't convert '_sre.SRE_Match' object to str implicitly
# 无法隐式转换 对象到 str"
# f = open(HTML_ROOT_DIR + f_name, "rb")
# 无法打开文件，点解呢？
# f_name = re.match(r"\w+ +(/[^ ]*)", request_start_line.decode("utf-8"))
# 落了.group(1)，没有取出文件名index.html

# 5.The file is not found!
# 服务器能通了，但显示文件没有发现
"""if '/' == f_name:
    f_name = 'index.html'
"""



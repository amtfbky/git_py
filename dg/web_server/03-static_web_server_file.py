# -*- coding:utf-8 -*-
import socket
import re
from multiprocessing import Process
# 这是静态文件根目录
HTML_ROOT_DIR = "./html"


def handle_client(client_socket):
    """服务器处理客户端请求"""
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request data:", request_data)

    # 第一步：1.把获取的报文按行切开，得到一个各行数据的列表
    request_lines = request_data.splitlines()
    # 2.遍历显示这个列表内容
    for line in request_lines:
        print(line)

    # 解析请求报文
    # GET / HTTP/1.1
    # 第二步：1.把列表第一句报文拿出来正则匹配，得到web服务器的网页文件名index.html
    request_start_line = request_lines[0]
    # 匹配规则：字母至少一个 空格至少一个 分组(/[斜杠后面可能是空格 ]接着后面任意字符)
    file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)

    # 2.判断域名后面如果为空(浏览器默认会有/)，则默认为/index.html
    if "/" == file_name:
        file_name = "/index.html"# 我这里写成"./index.html"，导致让/一直等于它

    # 第三步：操作网页服务器文件这是服务器干的事
    try:
        # 1.尝试打开
        f = open(HTML_ROOT_DIR + file_name, "rb")
    except IOError:
        # 第四步：构造响应数据，2.如果匹配结果有异常则显示
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_headers = "Server: My server\r\n"
        response_body = "The file is not found!"
    else:
        # 2.如果匹配成功，则读取文件，并用一个变量引用
        f_data = f.read()
        f.close()

        # 第四步：构造响应数据，1.匹配成功的显示，准备好文件
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My server\r\n"
        response_body = f_data.decode("utf-8")

    # 第四步：构造响应数据
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data:", (response_start_line + response_headers)
    # 第五步：向客户端返回响应数据，即浏览器打开网页
    client_socket.send(bytes(response, "utf-8"))
    # 第六步：关闭客户端连接
    client_socket.close()


if __name__ == '__main__':
    # socket解决传输层以下的事情
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("", 8000))
    server_socket.listen(128)

    while True:
        client_socket, client_addr = server_socket.accept()
        #print("[%s, %s]用户连接上了" % client_addr[0], client_addr[1])
        print("[%s, %s]用户连接上了" % client_addr)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()


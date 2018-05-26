# -*- coding:utf-8 -*-

import socket

from multiprocessing import Process

# 这是静态文件根目录，服务器的网页文件放在这个目录下
HTML_ROOT_DIR = "./html"


def handle_client(client_socket):
    """处理客户端请求"""
    # 获取浏览器的请求信息
    request_data = client_socket.recv(1024)
    print("request data:", request_data)

    """这就是浏览器的请求信息：省略
    GET / HTTP/1.1
    Host: 127.0.0.1:8002
    ...
    """

    # 解析请求信息
    # 先把信息文按照换行函数分开(列表)
    request_lines = request_data.splitlines()
    # 再遍历显示
    for line in request_lines:
        print(line)
    # 开始处理报文
    # 第一步：获取报文第一句
    request_start_line = request_lines[0]
    # 第二步：匹配提取网页文件名
    file_name = re.match(r"\w+ +(/[^ ]*)", request_start_line.decode("utf-8")).group(1)
    # 第三步：尝试打开读取该网页文件，如果发生异常做出处理
    try:
        f =

    request_start_line

    # 第四步：构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello world"
    response = response_start_line + response_headers + "\r\n" + response_body

    # 向浏览器返回响应数据，为什么要发送响应数据呢？因为返回的数据就是网页啊！我怎么这么懵啊！
    client_socket.send(bytes(response, "utf-8"))

    """这是浏览器接收到从服务器这里发送的响应数据
    HTTP/1.1 200 OK
    Server: My server
    """

    # 关闭客户端连接
    client_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8002))
    server_socket.listen(128)


    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s, %s]用户连接上了" % client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
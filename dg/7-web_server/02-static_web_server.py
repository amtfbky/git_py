## -*- coding:utf-8 -*-
import socket
from multiprocessing import Process
HTML_ROOT_DIR = ""


def handle_client(client_socket):
    """处理客户端请求"""
    # 这是获取客户端请求数据
    request_data = client_socket.recv(1024)
    print("request data:", request_data)
    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello world"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data:", response)
    # 向客户端返回响应数据
    client_socket.send(bytes(response, "utf-8"))
    # 关闭客户端连接
    client_socket.close()


if __name__ == '__main__':
    # socket解决传输层以下的事情
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))
    server_socket.listen(128)

    while True:
        client_socket, client_addr = server_socket.accept()
        #print("[%s, %s]用户连接上了" % client_addr[0], client_addr[1])
        print("[%s, %s]用户连接上了" % client_addr)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()


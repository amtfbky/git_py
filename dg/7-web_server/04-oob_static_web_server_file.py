## -*- coding:utf-8 -*-
import socket
import re
from multiprocessing import Process
# 这是静态文件根目录
HTML_ROOT_DIR = "./html"


class HTTPServer(object):
    """"""
    def __init__(self, port):
        # socket解决传输层以下的事情
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_addr = self.server_socket.accept()
            #print("[%s, %s]用户连接上了" % client_addr[0], client_addr[1])
            print("[%s, %s]用户连接上了" % client_addr)
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def handle_client(self, client_socket):
        """处理客户端请求"""
        # 这是获取客户端请求数据
        request_data = client_socket.recv(1024)
        print("request data:", request_data)
        request_lines = request_data.splitlines()
        for line in request_lines:
            print(line)

        # 解析请求报文
        # GET / HTTP/1.1
        request_start_line = request_lines[0]
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)

        if "/" == file_name:
            file_name = "./index.html"

        # 打开文件，读取内容
        try:
            f = open(HTML_ROOT_DIR + file_name, "rb")
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "Server: My server\r\n"
            response_body = "The file is not found!"
        else:
            f_data = f.read()
            f.close()

            # 构造响应数据
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server: My server\r\n"
            response_body = f_data.decode("utf-8")

        response = response_start_line + response_headers + "\r\n" + response_body
        print("response data:", response)
        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))
        # 关闭客户端连接
        client_socket.close()
        
        def bind(self, port):
            self.server_socket.bind(("", port))

def main():
    http_server = HTTPServer()
    # http_server.set_port
    http_server.bind(8080)
    http_server.start()

if __name__ == '__main__':
    main()

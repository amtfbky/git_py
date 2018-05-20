# -*- coding:utf-8 -*-
import socket
import re
import time
import sys
from multiprocessing import Process
# 这是静态文件根目录
HTML_ROOT_DIR = "./html"
#WSGI_PYTHON_DIR = "./wsgipython"


class HTTPServer(object):
    """"""
    def __init__(self, application):
        # socket解决传输层以下的事情
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.app = application

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_addr = self.server_socket.accept()
            #print("[%s, %s]用户连接上了" % client_addr[0], client_addr[1])
            print("[%s, %s]用户连接上了" % client_addr)
            print("-----------------test-------------------\r\n")
            handle_client_process = Process(target=self.handle_client, args=(client_socket,))
            handle_client_process.start()
            client_socket.close()

    def start_response(self, status, headers):
        """
        server_headers = [
                    {"Server", "My Server"}
                ]"""
        response_headers = "HTTP/1.1 " + status + "\r\n"
        for header in headers:
            response_headers += "%s: %s\r\n" % header
        self.response_headers = response_headers
        print("response data: ", self.response_headers)

    def handle_client(self, client_socket):
        """处理客户端请求"""
        # 这是获取客户端请求数据
        request_data = client_socket.recv(1024)
        #print("request data:", request_data)
        request_lines = request_data.splitlines()
        #for line in request_lines:
        #    print(line)

        # 解析请求报文
        # GET / HTTP/1.1
        request_start_line = request_lines[0]
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)
        method = re.match(r"(\w+) +/[^ ]* ", request_start_line.decode("utf-8")).group(1)

        env = {
                "PATH_INFO": file_name,
                "METHOD": method
        }
        response_body = self.app(env, self.start_response)
        # 这个程序能启动，但浏览器显示该网页无法正常工作
        # 服务器运行提示HTTPServer没有self.response_headers这个属性，点解？
        response = self.response_headers + "\r\n" + response_body
        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))
        # 关闭客户端连接
        client_socket.close()
        
    def bind(self, port):
        self.server_socket.bind(("", port))

def main():
    #sys.path.insert(1, WSGI_PYTHON_DIR)
    http_server = HTTPServer()
    # http_server.set_port
    http_server.bind(8000)
    http_server.start()

if __name__ == '__main__':
    main()

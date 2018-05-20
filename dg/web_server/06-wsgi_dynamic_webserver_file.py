# -*- coding:utf-8 -*-
import socket
import re
import time
import sys
from multiprocessing import Process
# 这是静态文件根目录
HTML_ROOT_DIR = "./html"
WSGI_PYTHON_DIR = "./wsgipython"


class HTTPServer(object):
    """"""
    def __init__(self):
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

    # 第三步：通过调用app把响应文从动态文件传回处理
    def start_response(self, status, headers):
        """这就是动态文件的响应文
        status = "200 OK"
        headers = [
                ("Content-Type", "text/plain")
                ]"""

        # 构造响应文头,这是第一句
        response_headers = "HTTP/1.1 " + status + "\r\n"
        # 遍历传回的headers,它是元组里的值对,用逗号隔开
        for i in headers:
            # 让响应文第一句后面接上遍历出来的值对，用:隔开
            response_headers += "%s: %s\r\n" % i

        # 初始化响应文头
        self.response_headers = response_headers

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
        #method = re.match(r"(\w+) +/[^ ]* ", request_start_line.decode("utf-8")).group(1)

        # 第一步：提取请求的文件名
        # "/ctime.py"
        if file_name.endswith(".py"):
            # 执行py文件,动态导入ctime模块
            m = __import__(file_name[1:-3])	# =ctime
            env = {
            #        "PATH_INFO": file_name,
            #        "METHOD": method
                    }
            # 第二步：调用创建好的ctime.py文件里的app，传参,这里把start_response当做参数
            # 把返回的东西当做响应文的body，就是网页内容
            response_body = m.application(env, self.start_response) # =m.ctime.application()
            # 第四步：把初始化好的响应文头+body
            response = self.response_headers + "\r\n" + response_body
        else:
            if "/" == file_name:
                file_name = "/index.html"

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
            print("response data:", (response_start_line + response_headers))
        # 向客户端返回响应数据
        client_socket.send(bytes(response, "utf-8"))
        # 关闭客户端连接
        client_socket.close()
        
    def bind(self, port):
        self.server_socket.bind(("", port))

def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    http_server = HTTPServer()
    # http_server.set_port
    http_server.bind(8000)
    http_server.start()

if __name__ == '__main__':
    main()

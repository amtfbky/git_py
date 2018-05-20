import socket
import re
import time
import sys
from multiprocessing import Process

HTML_ROOT_DIR = "./html"
WSGI_PYTHON_DIR = "./wsgipython"


class HTTPServer(object):
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self.server_socket.listen(128)
        while True:
            client_socket, client_addr = self.server_socket.accept()
            print("request data: %s %s" % client_addr)
            client_pro = Process(target=self.handle_client, args=(client_socket,))
            client_pro.start()
            client_socket.close()

    def start_response(self, status, headers):
        response_headers = "HTTP/1.1" + status + "\r\n"
        for i in headers:
            response_headers += "%s: %s\r\n" % i
        self.response_headers = response_headers

    def handle_client(self, client_socket):
        request_data = client_socket.recv(1024)
        request_lines = request_data.splitlines()
        request_start_line = request_lines[0]
        file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)

        if file_name.endswith(".py"):
            m = __import__(file_name[1:-3])
            env = {}
            response_body = m.application(env, self.start_response)
            response = self.response_headers + "\r\n" + response_body
            print("response data: ", self.response_headers)
        else:
            if "/" == file_name:
                file_name = "/index.html"
            
            try:
                f = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                response_start_line = "HTTP/1.1 404 Not Found\r\n"
                response_headers = "Server: My server\r\n"
                response_body = "The file is not found!"
            else:
                file_data = f.read()
                f.close()
                response_start_line = "HTTP/1.1 200 OK\r\n"
                response_headers = "Server: My server\r\n"
                response_body = file_data.decode("utf-8")

            response = response_start_line + response_headers + "\r\n" + response_body
            print("response data: ", (response_start_line + response_headers))
        client_socket.send(bytes(response, "utf-8"))
        client_socket.close()

    def bind(self, port):
        self.server_socket.bind(("", port))

def main():
    sys.path.insert(1, WSGI_PYTHON_DIR)
    http_server = HTTPServer()
    http_server.bind(8000)
    http_server.start()

if __name__ == "__main__":
    main()

import socket
from multiprocessing import Process
import re

HTML_ROOT_DIR = "./html"

class HTTPServer(object):
    def __init__(self):
        self.s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def start(self):
        self.s_socket.listen(128)
        while True:
            c_socket, c_addr = self.s_socket.accept()
            print("%s:%s" % c_addr)
            c_pro = Process(target=self.handle_c, args=(c_socket,))
            c_pro.start()
            c_socket.close()

    def handle_c(self, c_socket):
        request_d = c_socket.recv(1024)
        request_lines = request_d.splitlines()
        for i in request_lines:
            print(i)

        request_start_line = request_lines[0]
        f_name = re.match(r"\w+ +(/[^ ]*)", request_start_line.decode("utf-8")).group(1)

        if "/" == f_name:
            f_name = "/index.html"

        try:
            f = open(HTML_ROOT_DIR + f_name, "rb")
        except IOError:
            response_start_line = "HTTP/1.1 404 Not Found\r\n"
            response_headers = "Server: My server\r\n"
            response_body = "The file is not found!"
        else:
            f_data = f.read()
            f.close()
            response_start_line = "HTTP/1.1 200 OK\r\n"
            response_headers = "Server: My server\r\n"
            response_body = f_data.decode("utf-8")

        response = response_start_line + response_headers + "\r\n" + response_body
        c_socket.send(bytes(response, "utf-8"))
        c_socket.close()

    def bind(self, port):
        self.s_socket.bind(("", port))

def main():
    s = HTTPServer()
    s.bind(8000)
    s.start()

if __name__ == "__main__":
    main()

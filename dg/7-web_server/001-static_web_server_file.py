from socket import *
from multiprocessing import Process
import re

HTML_ROOT_DIR = "./html"

def handle_client(client_socket):
    """deal client data"""
    request_data = client_socket.recv(1024)
    request_lines = request_data.splitlines()
    for i in request_lines:
        print(i)

    request_start_line = request_lines[0]
    file_name = re.match(r"\w+ +(/[^ ]*)", request_start_line.decode("utf-8")).group(1)

    if "/" == file_name:
        file_name = "/index.html"

    try:
        f = open(HTML_ROOT_DIR + file_name, "rb")
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
    print("response data: ", (response_start_line + response_headers))
    client_socket.send(bytes(response, "utf-8"))
    client_socket.close()

if __name__ == "__main__":
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(("", 8000))
    server_socket.listen(128)
    while True:
        client_socket, client_addr = server_socket.accept()
        print("%s:%s line..." % client_addr)
        client_process = Process(target=handle_client, args=(client_socket,))
        client_process.start()

        client_socket.close()

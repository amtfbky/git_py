import socket
from threading import Thread

# 函数客户端处理
def handle_client(client_socket):
    
    # 获取客户端信息并打印
    recv_data = client_socket.recv(1024)
    print("request data: %s" % recv_data)

    # 构造响应数据
    # 报文头
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello world"
    response = response_start_line + response_headers + "\r\n" + response_body
    print("response data: ", response)
    # 发送响应数据
    client_socket.send(bytes(response, "utf-8"))

    # 关闭新创建的套接字
    client_socket.close()

# 主程序
if __name__ == "__main__":
    # 创建主动套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定
    server_socket.bind(("", 8001))
    server_socket.listen(9)
    # 监听，变成被动套接字

    # 循环
    while True:
        # 等待链接
        client_socket, client_info = server_socket.accept()

        # 打印客户端信息
        print("client info: %s" % str(client_info))

        # 创建子进程，调用函数
        client = Thread(target=handle_client, args=(client_socket,))

        # 开启子进程
        client.start()

        # 关闭新创建的套接字
        #client_socket.close()

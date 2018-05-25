# coding:utf-8
import socket


def f1(request):
    # 处理用户请求，返回相应的内容
    f = open("index.html", 'rb')
    data = f.read()
    f.close()
    return data


def f2(request):
    f = open("article.html", "r")
    data = f.read()
    f.close()
    return data


routes = [
    ("/xxx", f1),
    ("/ooo", f2),
]


def run():
    # 服务端socket
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', 8080))
    sock.listen(5)

    while True:
        # 用户连接后，服务端获取用户请求信息
        conn, addr = sock.accept()
        # 服务端获取数据
        data = conn.recv(8096)
        # 把获取到的数据转成字符串
        # data = str(data,encoding="utf-8") # py3 yes py2 no
        # data = bytes(data,encoding="utf-8") # py2 and py3 no
        # 把请求报文在两个换行处分割成报文头和报文体
        headers, body = data.split("\r\n\r\n")
        # 把报文头用一个换行分割
        tmp_list = headers.split("\r\n")
        # 再把报文头第一句用空格分割
        method, url, protocal = tmp_list[0].split(" ")
        # 服务端发送响应文
        conn.send(b"HTTP/1.1 200 OK\r\n\r\n")

        # 判断URL,就是HTTP/1.1 /这里就是url ...
        # 这里和django里的urls.py差不多了

        # 要先定义func_name
        func_name = None
        # 遍历路由
        for item in routes:
            # 判断路由，赋值
            if item[0] == url:
                func_name = item[1]
                break

        # 执行判断出来的函数，就是每个动态网页
        if func_name:
            response = func_name(data)
        else:
            response = b"404"
        conn.send(response)
        conn.close()


if __name__ == "__main__":
    run()

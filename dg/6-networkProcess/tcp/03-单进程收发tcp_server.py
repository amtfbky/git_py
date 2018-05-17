from socket import *

tcpSerSocket = socket(AF_INET, SOCK_STREAM)

tcpSerSocket.bind(("", 7790))

tcpSerSocket.listen(5)

# 单进程单任务服务端
while True:

    # 如果有新的客户端链接服务器，则产生一个newsocket专门为这个客户端服务
    # tcpSersocket就可以省下来专门等待其他客户端的链接
    newSocket, clientaddr = tcpSerSocket.accept()

    # 针对返回的新的客户端，单进程收发，即单工
    while True:

        recvData = newSocket.recv(1024)

        # 如果接收的数据长度为0，则说明客户端关闭了链接
        if len(recvData)>0:
            print("%s:%s"%(str(clientaddr), recvData.decode("gb2312")))
        else:
            break

        # 发送一些数据到客户端
        sendData = input("send: ")
        newSocket.send(sendData.encode("GB2312"))

    # 关闭这个客户端服务的socket，只要关闭了，就不能再为这个客户端服务了，如果还需要服务
    # 只能在前面的客户端关闭的前提下开启新的客户端
    newSocket.close()

# 关闭监听socket，就不能再接收任何新的客户端的链接
tcpSerSocket.close()






# 单任务服务器，需要关闭一个客户端再开启一个客户端，不实用
from socket import *

tcpSerSocket = socket(AF_INET, SOCK_STREAM)

tcpSerSocket.bind(("", 7790))

tcpSerSocket.listen(5)

while True:

    newSocket, clientaddr = tcpSerSocket.accept()

    try:
        while True:

            recvData = newSocket.recv(1024)

            if len(recvData)>0:
                print("%s:%s"%(str(clientaddr), recvData))
            else:
                print("[%s]client already off..." % str(clientaddr))
                break
    finally:
        newSocket.close()

tcpSerSocket.close()






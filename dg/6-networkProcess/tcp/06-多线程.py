from threading import Thread
from socket import *

def dealWithClient(newSocket, clientaddr):
    while True:

        recvData = newSocket.recv(1024)

        if len(recvData)>0:
            print("%s:%s"%(str(clientaddr), recvData))
        else:
            print("[%s]client already off..." % str(clientaddr))
            break
    newSocket.close()

def main():
    tcpSerSocket = socket(AF_INET, SOCK_STREAM)

    tcpSerSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    tcpSerSocket.bind(("", 7790))

    tcpSerSocket.listen(5)

    try:
        while True:

            # 主进程，等待新客户端链接
            newSocket, clientaddr = tcpSerSocket.accept()
            
            # 主进程，接下来创建一个新的进程负责数据处理
            print("客户端：[%s]" % str(clientaddr))
            client = Thread(target=dealWithClient, args=(newSocket, clientaddr))
            client.start()

            # 这里一定不能关闭newSocket
            #newSocket.close()
    finally:
        tcpSerSocket.close()

if __name__ == '__main__':
    main()

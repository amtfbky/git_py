from socket import *
from multiprocessing import Process

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

    try:    # 用try为了Ctrl+c关闭时接收异常?并关闭被动套接字
        while True:

            # 主进程，等待新客户端链接
            newSocket, clientaddr = tcpSerSocket.accept()
            
            # 主进程，接下来创建一个新的进程负责数据处理
            print("客户端：[%s]" % str(clientaddr))
            client = Process(target=dealWithClient, args=(newSocket, clientaddr))
            client.start()

            newSocket.close()
    finally:
        tcpSerSocket.close()

if __name__ == '__main__':
    main()

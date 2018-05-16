# 这个程序不实用，只是理解单进程非堵塞的原理
# 如果上万个用户链接，那要遍历这么多的用户系统会卡
from socket import *

tcpSerSocket = socket(AF_INET, SOCK_STREAM)

tcpSerSocket.bind(("", 7792))

# 第一步,让这个socket变成非堵塞
tcpSerSocket.setblocking(False)

tcpSerSocket.listen(100)

# 第三步：用来保存所有已经链接的客户端的信息
clientAddList = []

while True:

    # 等待一个新的客户端链接(即完成3次握手)
    # 就是在这里堵塞，打通
    # 第二步：
    try:
        newSocket, clientaddr = tcpSerSocket.accept()
    except:
        pass
    else:
        print("一个新客户端已链接：[%s]" % str(clientaddr))
        # 第五步：让客户端的socket变成非堵塞
        newSocket.setblocking(False)

        # 第四步：添加新socket和客户端地址
        clientAddList.append((newSocket, clientaddr))

    # 第五步：遍历客户端列表，接收信息
    for newSocket, clientaddr in clientAddList:
        # 第六步：加try
        try:
            recvData = newSocket.recv(1024)
        except:
            pass
        else:
            # 第七步：判断客户端关闭
            if len(recvData)>0:
                print("%s:%s" % (str(clientaddr), recvData))
            else:
                # 第八步：关闭客户端socket，从列表删除客户端信息
                newSocket.close()
                clientAddList.remove((newSocket, clientaddr))
                print("%s 已下线..." % str(clientaddr))

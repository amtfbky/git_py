from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(("192.168.1.3", 2426))

# TCP客户端已经链接好了服务器，所以在以后的的数据发送中，不需要填写对方的ip和port--->打电话
# UDP在发送数据的时候，因为没有之前的链接，所以要填写--->写信
clientSocket.send("hhaa".encode("gb2312"))

recvData = clientSocket.recv(1024)

print("recvData:%s"%recvData)

clientSocket.close()

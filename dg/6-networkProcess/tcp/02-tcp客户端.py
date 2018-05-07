from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect(("192.168.1.5", 2426))

clientSocket.send("hhaa".encode("gb2312"))

recvData = clientSocket.recv(1024)

print("recvData:%s"%recvData)

clientSocket.close()

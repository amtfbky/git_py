from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

# 绑定本地信息，一般看到绑定，肯定是服务器，客户端可以不绑定
serverSocket.bind(("", 7789))

# 只要看到listen，肯定是服务器
serverSocket.listen(5)

print("-----1------")
clientSocket,clientInfo = serverSocket.accept()

#clientSocket表示这个新的客户端
#clientInfo表示这个新的客户端的ip和port

print("-----2------")
recvData = clientSocket.recv(1024)

print("-----3------")
print("%s:%s"%(str(clientInfo), recvData))

clientSocket.close()
serverSocket.close()






from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(("", 7788))

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






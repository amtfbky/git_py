from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

# UDP发送时，接收方xp的网络调试助手都会开辟一个新的端口
# python3 +b
udpSocket.sendto(b"haha", ("192.168.1.5", 8080))
# python2
#udpSocket.sendto("haha", ("192.168.1.5", 8080))

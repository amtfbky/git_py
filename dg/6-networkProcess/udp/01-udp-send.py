from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

# python3 +b
udpSocket.sendto(b"haha", ("192.168.1.5", 8080))
# python2
#udpSocket.sendto("haha", ("192.168.1.5", 8080))

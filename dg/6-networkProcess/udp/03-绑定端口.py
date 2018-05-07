#coding=utf-8
from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

udpSocket.bind(("", 7788))

# python3 +b
#udpSocket.sendto(b"haha", ("192.168.1.5", 2426))
# python2
udpSocket.sendto("haha", ("192.168.1.5", 2426))

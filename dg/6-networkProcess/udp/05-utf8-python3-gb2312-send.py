from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)

destIp = input("Ip: ")
destPort = int(input("Port: "))
sendData = input("Input: ")

#udpSocket.sendto(sendData.encode("utf-8"), (destIp, destPort))
udpSocket.sendto(sendData.encode("GB2312"), (destIp, destPort))

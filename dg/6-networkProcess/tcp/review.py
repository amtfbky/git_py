# 如果s套接字协议发送广播数据，那就需要这句话
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

# 以广播的形式发送数据到本网络的所有电脑中
s.sendto("hi", dest)

tcp:传输控制协议
    稳定
    相比upd慢一些，但感觉不出来
    web服务

udp:用户数据包协议

服务端：
1.socket：主动套接字
2.bind
3.listen：将主动套接字变为被动套接字
4.accept:返回一个元组

1.买个手机socket
2.插入手机卡bind
3.设置手机为响铃模式listen
4.等着别人的电话，准备接听accept

客户端：
1.socket
2.connect
3.发信
4.收信
5.显示收信
6.关闭socket

三次握手
第一步：SYN 发给服务器数字0
第二步：SYN+ACK确认包 返回数字1
第三步：ACK+1

四次挥手，如果不挥手，会占用资源
第一步：FIN给服务器
第二步：ACK给客户端

第三步：FIN给客户端
第四步：ACK给服务器

IP是逻辑地址
MAC是物理地址
掩码是为了得到网络号
网关，我知道哪里能贷到款，我指给你
DNS



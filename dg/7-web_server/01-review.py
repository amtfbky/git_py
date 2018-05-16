应用层
    解决要传输什么数据
    张三跟老王通信：
        天王盖地虎————>宝塔镇河妖
传输层
    解决如何传输数据udp icp，快递公司
网络层
    IP，理解为地理位置坐标
链路层
    具体的传输工具

GET / HTTP/1.1
Host: 127.0.0.1:8000
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9

GET / HTTP/1.1
Host: www.baidu.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: BAIDUID=3664AEEEA1832CF0099CD924765B4139:FG=1; FP_UID=a0c96d94ad519f2c823e28518ecfe6c4; cflag=13%3A3; BIDUPSID=3664AEEEA1832CF0099CD924765B4139; PSTM=1526363128; BD_UPN=123353; sugstore=1; BD_HOME=0; H_PS_PSSID=1430_21091_18560_20718
后面加的
Content-Length:128
\r\n
username
password
请求体...
html体

HTTP 请求方式
GET 获取数据
POST 修改数据
PUT 保存数据
DELETE 删除
OPTION 询问服务器某种支持特性
HEAD 返回报文头

/
/index.html
/css/index.css

HTTP/1.1 版本

服务器响应部分
HTTP/1.1 200 OK	#状态码
Bdpagetype: 1
Bdqid: 0xa54fc9c70004b270
Cache-Control: private
Connection: Keep-Alive
Content-Encoding: gzip
Content-Type: text/html; charset=utf-8
Cxy_all: baidu+86ce91bf9af965476753dcedfd546a15
Date: Tue, 15 May 2018 06:04:19 GMT
Expires: Tue, 15 May 2018 06:04:18 GMT
Server: BWS/1.1
Set-Cookie: BDSVRTM=0; path=/
Set-Cookie: BD_HOME=0; path=/
Set-Cookie: H_PS_PSSID=1430_21091_18560_20718; path=/; domain=.baidu.com
Strict-Transport-Security: max-age=172800
Vary: Accept-Encoding
X-Powered-By: HPHP
X-Ua-Compatible: IE=Edge,chrome=1
Transfer-Encoding: chunked

URL Location
协议://www.xxx.com/资源定位/?key1=value1&key2=value2&key3...(查询字符串Query String)
URI
URN Name未来趋势

代码流程
# tcp socket 服务器
socket = socket.socket()
socket.bind()
socket.listen()
c = socket.accept()
while True:
    p = Process(target=fun, args=())
    p.start()
    c.close()

def fun(c):
    # 接收数据
    # request_data = recv()
    # print(request_data)
    # 解析HTTP报文数据 request_data
    # 提取请求方式
    # 提取请求路径
    HTML_ROOT_DIR = "./html"
    /index.html
    try:
        f = open(HTML_ROOT_DIR + "index.html")
    data = f.read()
    f.close()
    except IOError:
        HTTP1.1 404 Not Found\r\n
        \r\n
        not found

    # 返回响应数据
    HTTP1.1 200 OK\r\n
    \r\n
    hello itcast
    # send()
    # close()


# -*- coding:utf-8 -*-

import time

# WSGI协议动态web服务器第二步，app接参
def application(env, start_response):
    status = "200 OK"
    headers = [
                ("Content-Type", "text/plain")
            ]
    # 在函数里又把参数当函数把响应文传回服务器主体
    start_response(status, headers)
    # 让app返回东西
    return time.ctime()

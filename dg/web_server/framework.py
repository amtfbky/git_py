# -*- coding:utf-8 -*-

import time
from server import HTTPServer


class Application(object):
    """框架核心部分，即主体程序，框架通用"""
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")
        for url, handler in self.urls:
            if path == url:
                return handler(env, start_response)
        # 代表没有找到路由信息，404错误
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "not found"

def show_ctime(env, start_response):
    status = "200 OK"
    headers = [
                ("Content-Type", "text/plain")
            ]
    return time.ctime()

def say_hello(env, start_response):
    status = "200 OK"
    headers = [
                ("Content-Type", "text/plain")
            ]
    return "hello web"

def say_haha(env, start_response):
    status = "200 OK"
    headers = [
                ("Content-Type", "text/plain")
            ]
    return "hello haha"

if __name__ == "__main__":
    urls = [("/", show_ctime),
            ("/ctime", show_ctime),
            ("/sayhello", say_hello),
            ("/sayhaha", say_haha)
            ]

    app = Application(urls)
    http_server = HTTPServer(app)
    http_server.bind(8000)
    http_server.start()

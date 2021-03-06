# -*- coding:utf-8 -*-

import time
from server import HTTPServer


class Application(object):
    """框架核心部分，即主体程序，框架通用"""
    def __init__(self, urls):
        # 路由信息
        self.urls = urls

    # call魔法让app()
    def __call__(self, env, start_response):
        """
        env = {
                "PATH_INFO": file_name,
                "METHOD": method
        }"""
        # get拿到env里值对的对应值,这里就是file_name
        path = env.get("PATH_INFO", "/")
        print("get res: %s" % path)

        # 遍历urls，值对包含url和函数
        for url, handler in self.urls:

            # 这里如果file_name=url，则调用该函数，就是动态网页
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
    # url+handler
    urls = [("/", show_ctime),
            ("/ctime", show_ctime),
            ("/sayhello", say_hello),
            ("/sayhaha", say_haha)
            ]

    # 创建app
    app = Application(urls)
    # 把app传给web服务器主体
    http_server = HTTPServer(app)
    http_server.bind(8000)
    http_server.start()

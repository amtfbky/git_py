# -*- coding:utf-8 -*-

import time

# from server import HTTPServer

HTML_ROOT_DIR = "./html"


class Application(object):
    """框架核心部分，即主体程序，框架通用"""
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")
        if path.startswith("/static"):
            file_name = path[7:]
            try:
                f = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                # 代表没有找到路由信息，404错误
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "not found"
            else:
                f_data = f.read()
                f.close()
                status = "200 OK"
                headers = []
                start_response(status, headers)
                return f_data.decode("utf-8")

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

urls = [("/", show_ctime),
        ("/ctime", show_ctime),
        ("/sayhello", say_hello),
        ("/sayhaha", say_haha)
        ]

app = Application(urls)

# if __name__ == "__main__":
#     urls = [("/", show_ctime),
#             ("/ctime", show_ctime),
#             ("/sayhello", say_hello),
#             ("/sayhaha", say_haha)
#             ]
#
#     app = Application(urls)
#     http_server = HTTPServer(app)
#     http_server.bind(8001)
#     http_server.start()

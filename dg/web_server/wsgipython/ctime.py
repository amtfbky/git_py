# -*- coding:utf-8 -*-

import time

def application(env, start_response):
    status = "200 OK"
    headers = [
                ("Conten-Type", "text/plain")
            ]
    start_response(status, headers)
    return time.ctime()

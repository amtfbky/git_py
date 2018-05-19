# -*- coding:utf-8 -*-
import re

s = """<img src="https://staticlive.douyucdn.cn/storage/webpic_resources/upload/slide/2018/0426/1.jpg" data-original="https://staticlive.douyucdn.cn/storage/webpic_resources/slide/2018/0426/2.jpg">"""

# 我这里试验结果没有加?就不贪婪了，加了?还是一样
#r = re.search(r"https.+\.jpg", s).group()
r = re.search(r"https.+?\.jpg", s).group()
print(r)

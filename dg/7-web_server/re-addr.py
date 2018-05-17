# -*- coding:utf-8 -*-
import re

#s ="""https://www.bing.com/dict?FORM=Z9LH3"""
#s ="""https://32434341.com/class/clsass/dict?FORM=Z9LH3"""
#s ="""https://lib.cn.bing.cn/news/dict?FORM=Z9LH3"""
#s ="""https://www.zy-ls.com/dict?FORM=Z9LH3"""
s ="""https://cn.bing.com/dict?FORM=Z9LH3"""

#r = re.sub(r"https://.+/", "", s)
#r = re.sub(r"https://.+?/", "", s)
#r = re.sub(r"https://.+?/(.*)", "", s)

# y=x.group(1)
r = re.sub(r"(https://.+?/).*", lambda x: x.group(1), s)
print(r)

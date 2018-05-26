# -- coding:utf8 -*-

from MysqlHelper import MysqlHelper
import hashlib

name=raw_input("username: ")
while True:
    pwd1=raw_input("pwd: ")
    pwd2=raw_input("again: ")
    if pwd1==pwd2:
        break

sql='insert into users(name,passwd) values(%s,%s)'

# 先加密,再转换成十六进制
pwd=hashlib.sha1(pwd2.encode("utf-8")).hexdigest()
user_input=[name, pwd]
helper=MysqlHelper('localhost',3306,'guanxi','root','Nmamtf@013')

# 不理解封装的MysqlHelper 2018年05月21日20:22:59
# 总算搞明白了，但不熟 2018年05月22日10:37:02
res=helper.cud(sql, user_input)

# -*- coding:utf8 -*-

from MysqlHelper import MysqlHelper

import hashlib

name=raw_input('name: ')
while True:
    pwd1=raw_input('code: ')
    pwd2=raw_input('again: ')
    if pwd1==pwd2:
        break

sql='insert into users(name,passwd) values(%s,%s)'
pwd=hashlib.sha1(pwd2.encode('utf-8')).hexdigest()
sqlhelper=MysqlHelper('localhost',3306,'guanxi','root','Nmamtf@013')
data=[name, pwd]
sqlhelper.cud(sql,data)
#print("name: %s code: %s" % data)  # no
#print("name: %s code: %s" % (data[0], data[1]))
print("name: "+data[0]+"\t"+"code: "+data[1])

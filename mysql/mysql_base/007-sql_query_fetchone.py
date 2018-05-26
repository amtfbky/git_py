# -*- coding:utf8 -*-

from MysqlHelper import MysqlHelper

sql='select name from students where id=3'
h=MysqlHelper('localhost',3306,'guanxi','root','Nmamtf@013')
# 返回查询的单行数据
data=h.one(sql)

print("Name: %s" % data)

# -*- coding:utf8 -*-

from MysqlHelper import MysqlHelper

sname=raw_input('del name: ')
params=[sname]
sql='delete from users where name=%s'
h=MysqlHelper('localhost',3306,'guanxi','root','Nmamtf@013')
res=h.cud(sql, params)
print("delete:", sname)

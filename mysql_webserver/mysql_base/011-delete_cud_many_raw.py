# -*- coding:utf8 -*-

from MysqlHelper import MysqlHelper

sql='delete from users where id>5'
h=MysqlHelper('localhost',3306,'guanxi','root','Nmamtf@013')
res=h.cud(sql, [])
print(res)

# -*- coding:utf8 -*-

from MysqlHelper import MysqlHelper

sql='delete from users where id=9'
h=MysqlHelper('localhost',3306,'guanxi','root','Nmamtf@013')
res=h.cud(sql, [])
#res=h.cud(sql) # no

# -*- coding:utf8 -*-

from MysqlHelper import MysqlHelper

sname=raw_input('add name: ')
scode=raw_input('code: ')
params=[sname,scode]
sql='insert into users(name,passwd) values(%s,%s)'
h=MysqlHelper('localhost',3306,'guanxi','root','Nmamtf@013')
res=h.cud(sql, params)

# -*- coding:utf8 -*-

from MysqlHelper import MysqlHelper

# 修改
# name=raw_input("username: ")
# id1=raw_input("Num: ")
# 
# sql='update students set name=%s where id=%s'
# params=[name, id1]

# 查询
sql='select id,name from students where id<5'

sqlhelper=MysqlHelper('localhost',3306,'guanxi','root','Nmamtf@013')
#sqlhelper.cud(sql, params)
res=sqlhelper.all(sql)
print(res)

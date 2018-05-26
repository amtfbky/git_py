# -*- coding:utf8 -*-

from MysqlHelper import MysqlHelper

sql='select * from users'
r=MysqlHelper('localhost',3306,'guanxi','root','Nmamtf@013')
data=r.all(sql)

for i in data:
    #print("ID:"+str(i[0])+"Name:"+str(i[1])+"Pwd:"+str(i[2]))
    #print(i)
    print("ID: %s Name: %s Code: %s" % i)

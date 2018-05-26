# -*- coding:utf8 -*-

from MysqlHelper import MysqlHelper

sql='select id,name from students where id<4'
h=MysqlHelper('localhost',3306,'guanxi','root','Nmamtf@013')
res=h.all(sql)
for i in res:
    #print('ID:'+str(i[0][0])+' Name:'+i[0][1]) # no
    #print(i) # 'long' object has no attribute '__getitem__'
    print("ID: %s Name: %s" % i)

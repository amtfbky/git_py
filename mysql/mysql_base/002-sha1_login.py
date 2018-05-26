# -- coding:utf8 -*-

from MysqlHelper import MysqlHelper
from hashlib import sha1

name=raw_input("username: ")
pwd=raw_input("pwd: ")

# 对密码加密
s1=sha1()
# s1=md5()  # for test
s1.update(pwd)
pwd2=s1.hexdigest()

sql='select passwd from users where name=%s'
helper=MysqlHelper('localhost',3306,'guanxi','root','Nmamtf@013')
#res=helper.one(sql,[name]) # for test
# 这里查询全部的行，所以用all
res=helper.all(sql,[name])

# 验证
if len(res)==0:
    print('Username error...')
elif res[0][0]==pwd2:
    print('Login OK')
else:
    print('Code error...')


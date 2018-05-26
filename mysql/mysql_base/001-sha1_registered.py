# -*- coding:utf8 -*-

from MySQLdb import *
import hashlib

name = raw_input("用户名:")
while True:
    pwd1 = raw_input("密码:")
    pwd2 = raw_input("请再输入一遍密码:")
    if pwd1 == pwd2:
        break
try:
    conn = connect(host="localhost", port=3306, user="root", passwd="Nmamtf@013", db="guanxi", charset="utf8")
    cus1 = conn.cursor()
    sql = "insert into users(name,passwd) values(%s,%s)"
    pwd = hashlib.sha1(pwd2.encode("utf-8")).hexdigest()
    print(pwd)
    res = [name,pwd]
    print(res)
    cus1.execute(sql,res)
    conn.commit()
    cus1.close()
    conn.close()
except Exception as e:
    print(e)
else:
    print("新用户创建成功")

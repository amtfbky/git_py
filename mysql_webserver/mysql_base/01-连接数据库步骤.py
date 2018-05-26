# -*- coding:utf8 -*-

from MySQLdb import *

try:
    conn=connect(host="localhost",
            port=3306,
            user="root",
            passwd="Nmamtf@013",
            db="guanxi",
            charset="utf8")
    cursor=conn.cursor()
    #cursor.execute('select * from users')
    cursor.execute('select * from students')
    data=cursor.fetchall()

    for i in data:
        #print("ID:"+str(i[0])+"Name:"+str(i[1])+"Pwd:"+str(i[2]))
        #print(i[1])  
        # not all arguments converted during string formatting
        # 不是在字符串格式化期间转换的所有参数，少了%s

        print("ID: %s Name: %s Gender: %s" % i)
    cursor.close()
    conn.close()
except Exception,e:
    print(e.message)

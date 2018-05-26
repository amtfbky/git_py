# -*- coding:utf8 -*-

from MySQLdb import *

try:
    name_py=raw_input("请输入姓名：")
    # 第一步：连接数据库
    conn=connect(host='localhost',
            port=3306,
            user='root',
            passwd='Nmamtf@013',
            db='guanxi',
            charset='utf8')
    # 第二步：开启游标，调用cursor函数
    cs1=conn.cursor()

    # sql='insert into students(name) values("zhangsan")'
    # sql='update students set name="laoge" where id=5'
    # cs1.execute(sql)

    # 第三步：执行SQL语句,execute函数第二个参数是个元组
    sql='insert into students(name) values(%s)'
    cs1.execute(sql,[name_py])

    # 第四步：提交
    conn.commit()
    
    # 第五步：关闭游标
    cs1.close()
    # 第六步：关闭数据库
    conn.close()

except Exception,e:
    print(e.message)



# -*- coding:utf8 -*-

from MySQLdb import *


class MysqlHelper:
    def __init__(self, host, port, db, user, passwd, charset='utf8'):
        self.host=host
        self.port=port
        self.db=db
        self.user=user
        self.passwd=passwd
        self.charset=charset

    def open(self):
        self.conn=connect(host=self.host,
                port=self.port,
                db=self.db,
                user=self.user,
                passwd=self.passwd,
                charset=self.charset)
        self.cs1=self.conn.cursor()

    def close(self):
        self.cs1.close()
        self.conn.close()

    # 增删改
    def cud(self, sql, params):
        try:
            self.open()
            self.cs1.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception,e:
            print(e.message)

    # 查，返回一行
    def one(self, sql, params=[]):
        try:
            self.open()
            self.cs1.execute(sql, params)
            res=self.cs1.fetchone()
            self.close()
            return res
        except Exception,e:
            print(e.message)

    # 查，返回多行
    def all(self, sql, params=[]):
        try:
            self.open()
            self.cs1.execute(sql, params)
            res=self.cs1.fetchall()
            self.close()
            return res
        except Exception,e:
            print(e.message)

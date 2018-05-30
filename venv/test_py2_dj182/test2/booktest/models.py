# -*- coding: utf-8 -*-

from django.db import models


class BookInfoManager(models.Manager):
    """自定义管理器：原始数据查询"""
    def get_queryset(self):
        """重写父类原始数据查询方法"""
        # 在调用父类方法实现查询的基础上再把一些数据过滤掉
        return super(BookInfoManager, self).get_queryset().filter(
            isDelete=False)     # 过滤掉逻辑删除的

    def create(cls, btitle, bpub_date):
        b=BookInfo()
        b.btitle=btitle
        b.bpub_date=bpub_date
        b.bread=0
        b.bcommet=0
        b.isDelete=False
        return b


class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0)            # 阅读量
    bcommet=models.IntegerField(null=False)         # 评论量
    isDelete=models.BooleanField(default=False)

    class Meta:     # 元选项，改变一些元信息，这里将模型对应表名的应用前缀booktest去掉
        db_table='bookinfo'

    book1=models.Manager()
    book2=BookInfoManager()         # 可自己定义多个管理器

    @classmethod
    def create(cls, btitle, bpub_date):
        b=BookInfo()
        b.btitle=btitle
        b.bpub_date=bpub_date
        b.bread=0
        b.bcommet=0
        b.isDelete=False
        return b


class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=1000)      # 描述
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo)
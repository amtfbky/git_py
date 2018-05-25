# -*- coding: utf-8 -*-

from django.db import models


class BookInfoManager(models.Manager):
    """自定义管理器：原始数据查询"""
    def get_queryset(self):
        """重写父类原始数据查询方法"""
        # 在调用父类方法实现查询的基础上再把一些数据过滤掉
        return super(BookInfoManager, self).get_queryset().filter(
            isDelete=False)     # 过滤掉逻辑删除的


class BookInfo(models.Model):
    btitle=models.CharField(max_length=20)
    bpub_date=models.DateTimeField(db_column='pub_date')
    bread=models.IntegerField(default=0)            # 阅读量
    bcommet=models.IntegerField(null=False)         # 评论量
    isDelete=models.BooleanField(default=False)

    class Meta:                                     # 元选项?
        db_table='bookinfo'

    book1=models.Manager()    # 可自己定义多个管理器，但默认的管理器就没了
    book2=BookInfoManager()


class HeroInfo(models.Model):
    hname=models.CharField(max_length=10)
    hgender=models.BooleanField(default=True)
    hcontent=models.CharField(max_length=1000)      # 描述
    isDelete=models.BooleanField(default=False)
    book=models.ForeignKey(BookInfo)
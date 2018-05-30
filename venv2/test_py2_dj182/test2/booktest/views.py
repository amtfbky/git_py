# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.db.models import Max, F, Q    # 聚合函数
from models import *


def index(req):
    # list = BookInfo.book1.filter(heroinfo__hcontent__contains='八')
    # list = BookInfo.book1.filter(pk__lte=3)
    # Max1 = BookInfo.book1.aggregate(Max('bpub_date'))
    # list = BookInfo.book1.filter(bread__gt=20)      # 阅读量>20

    # F对象，两个字段的值做比较
    # list = BookInfo.book1.filter(bread__gt=F('bcommet') * 2)      # 阅读量>评论量
    # list = BookInfo.book1.filter(isDelete=F('heroinfo__isDelete'))

    # Q对象，逻辑或
    list = BookInfo.book1.filter(pk__lt=4, btitle__contains='八')    # 逻辑与主键<4并且title包含'八'
    # list = BookInfo.book1.filter(Q(pk__lt=2)|Q(btitle__contains='传'))    # 主键<2或title包含'传'
    context = {"list_key": list
               # , 'Max1': Max
               }    # 上下文
    return render(req, 'booktest/index.html', context)

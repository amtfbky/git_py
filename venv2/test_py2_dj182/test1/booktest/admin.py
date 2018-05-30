# -*- coding:utf-8 -*-

from django.contrib import admin

from models import *

# Register your models here.
# 关联类添加
#class HeroInfoInline(admin.StackedInline):
class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    extra = 3

class BookInfoAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['id','btitle','bpub_date']
    # 过滤字段
    list_filter = ['btitle']
    # 搜索字段
    search_fields = ['btitle']
    # 分页
    list_per_page = 10
    # 添加页
    #fields = ['bpub_date', 'btitle']
    # 修改页属性
    fieldsets = [
            ('base',{'fields':['btitle']}),
            ('super',{'fields':['bpub_date']})
            ]
    inlines = [HeroInfoInline]

# 
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo)

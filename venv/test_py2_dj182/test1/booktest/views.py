# -*- coding:utf-8 -*-

from django.shortcuts import render

from django.http import *

from .models import *
#from django.template import RequestContext,loader

# Create your views here.
def index(request):
    #temp = loader.get_template('booktest/index.html')
    #return HttpResponse(temp.render())

    # 在HTML里挖坑,通过视图向html文件传递数据
    #context={'title':'all'}
    
    bookList = BookInfo.objects.all()
    context = {'list':bookList}

    return render(request,'booktest/index.html',context)

def show(request,id):
    book = BookInfo.objects.get(pk=id)
    herolist = book.heroinfo_set.all()
    context = {'list':'herolist'}
    return render(request,'booktest/show.html',context)

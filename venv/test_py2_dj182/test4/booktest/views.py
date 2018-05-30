# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from models import *


def index(request):
    # hero=HeroInfo.objects.get(pk=1)
    # context={'hero': hero}

    list=HeroInfo.objects.filter(isDelete=False)
    context={'list': list}
    return render(request, 'booktest/index.html', context)

def show(request, id, id2):
    context={'id': id}
    return render(request, 'booktest/show.html', context)

# 模板教科案例框架
def user1(request):
    context={'uname': '阿弥陀佛'}
    return render(request, 'booktest/user1.html', context)

def user2(request):
    return render(request, 'booktest/user2.html')

# HTML转义
def htmlTest(request):
    context={'list': '<h1>abc</h1>'}
    return render(request, 'booktest/htmlTest.html', context)

# csrf
def csrf1(request):
    return render(request, 'booktest/csrf1.html')

def csrf2(request):
    uname=request.POST['uname']
    return HttpResponse(uname)

# 验证码
def verify_code(request):
    from PIL import Image, ImageDraw, ImageFont
    import random
    # 创建背景色
    bgcolor=(random.randrange(50, 100), random.randrange(50, 100), 0)
    # 规定宽高
    width=100
    height=25
    # 创建画布
    image=Image.new('RGB', (width, height), bgcolor)
    # 构造字体对象
    font=ImageFont.truetype('FreeMono.ttf', 24)
    # 创建画笔
    draw=ImageDraw.Draw(image)
    # 创建文本内容
    text='0123abcd'

    # 逐个绘制8个字符
    # for i in range(4):
    #     draw.text((i*25, 0),
    #          text[random.randrange(0, len(text))],
    #          (255, 255, 255),
    #          font)

    # 4个字符的绘制
    # draw.text((0, 0), text, (255, 255, 255), font)

    # 将字符存入session
    textTmp=''
    for i in range(4):
        textTmp1=text[random.randrange(0, len(text))]
        textTmp+=textTmp1
        draw.text((i*25, 0),
                  textTmp1,
                  (255, 255, 255),
                  font)
        request.session['code']=textTmp

    # 保存到内存流中
    import cStringIO    # 内存操作的包
    buf=cStringIO.StringIO()
    image.save(buf, 'png')

    return HttpResponse(buf.getvalue(), 'image/png')

def verify_test1(request):
    return render(request, 'booktest/verify_test1.html')

def verify_test2(request):
    code1=request.POST['code1']
    code2=request.session['code']
    if code1==code2:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')
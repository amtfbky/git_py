# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse('Hello world')

def detail(request, p1, p2, p3):
    return HttpResponse('%s/%s/%s' % (p1, p2, p3))

# 展示链接的页面
def getTest1(request):
    return render(request, 'booktest/getTest1.html')

# 接收一键一值的情况
def getTest2(request):
    # 根据键接收值
    a1=request.GET['a']
    b1=request.GET['b']
    c1=request.GET['c']
    # 构造上下文
    context={'a': a1, 'b': b1, 'c': c1}
    # 向模板传递上下文，渲染
    return render(request, 'booktest/getTest2.html', context)

# 接收一键多值的情况
def getTest3(request):
    a1=request.GET.getlist('a')
    context={'a': a1}
    return render(request, 'booktest/getTest3.html', context)

def postTest1(request):
    return render(request, 'booktest/postTest1.html')

def postTest2(request):
    uname=request.POST['uname']
    upwd=request.POST['upwd']
    ugender=request.POST['ugender']
    uhobby=request.POST.getlist('uhobby')
    context={'uname': uname, 'upwd': upwd, 'ugender': ugender, 'uhobby': uhobby}
    return render(request, 'booktest/postTest2.html', context)

# 练习cookie
def cookieTest(request):
    response=HttpResponse()
    cookie=request.COOKIES
    if cookie.has_key('t1'):
        response.write(cookie['t1'])
    # response.set_cookie('t1', 'hello cookie')
    return response

# 转向(重定向)练习
def redTest1(resquest):
    # return HttpResponseRedirect('/booktest/redTest2/')
    return redirect('/booktest/redTest2/')

def redTest2(resquest):
    return HttpResponse('这是转向来的页面')

# 通过用户登录来练习session
def session1(request):
    # uname = None
    # uname=request.session['myname']
    uname = request.session.get('myname', '未登录')
    context={'uname': uname}
    return render(request, 'booktest/session1.html', context)

def session2(request):
    return render(request, 'booktest/session2.html')

def session2_handle(request):
    # uname=request.POST('uname')
    uname=request.POST['uname']
    request.session['myname']=uname
    return redirect('/booktest/session1/')

def session3(request):
    del request.session['myname']
    return redirect('/booktest/session1/')
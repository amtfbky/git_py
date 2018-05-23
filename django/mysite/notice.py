把新定义的app加到settings.py中的INSTALL_APPS中：
	django会自动找到app中的模板文件(learn/templates/...
				    learn/static/...)

# 第一步：
mysite/learn/view.py
# 引入HttpResponse，用来向网页返回内容=print
from django.http import HttpResponse

# index函数，第一个参数必须是request，与网页发来的请求有关，可以包含get或post的内容，函数返回内容到网页
# 接着打开mysite/mysite/urls.py
def index(request):
    return HttpResponse(u'欢迎光临!')


# 第二步：
mysite/mysite/urls.py
# 加入一行
url(r'^$', 'learn.views.index', name='home'),



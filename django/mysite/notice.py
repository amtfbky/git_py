把新定义的app加到settings.py中的INSTALL_APPS中：
	django会自动找到app中的模板文件(learn/templates/...
				    learn/static/...)
learn/view.py
# 
def index(request):
    return HttpResponse(u'欢迎光临!')


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
# 这上面是根据自强学堂的PDF教程文档来的，因为我没有安装Django1.5版本，只开了个头
--------------------------------------------------------------------------------------
# 下面是根据麦子学院的光希老师的视频教程，这里还是Django1.5版本，我在Ubuntu1604装了虚拟环境
# 再安装了Django1.5
django-admin.py startproject website
website/website/setting.py
# 加'blog'，改时区和中文

website/website/urls.py
# 加上
	url(r'^blog/index/$', 'blog.views.index'),


django-admin.py startapp blog

# 这一步会反复改内容
website/blog/views.py
# 在blog的视图里写下网页内容

	# 1.最初的显示
	from django.http import HttpResponse

	def index(request):
		return HttpResponse("<h1>Hello world</h1>") # 渲染

python manage.py runserver
	# 打开浏览器
	http://127.0.0.1:8000/blog/index/

# 这是输出Hello world

# 第二次改写blog视图 
	# 2.开始从HTML文件嵌入,模板化的方式
	from django.http import HttpResponse
	from django.template import loader, Context


	def index(request):
		# 分离的思想
		# 向模板提供数据
		t = loader.get_template("index.html")
		c = Context({})
		return HttpResponse(t.render(c)) # 渲染
<h1>hello, django</h1>
----------------------------
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{title}}</title>
</head>
<body>
<h1>hello, {{name}}</h1>
</body>
</html>
    c = Context({"title": "django", "name": "tom"})
# 浏览器
hello, tom
----------------------------
<h1>hello, {{user}}</h1>
    user = {"name": "tom", "age": 23, "sex": "male"}
    c = Context({"title": "django", "name": user})
# 浏览器
hello, 


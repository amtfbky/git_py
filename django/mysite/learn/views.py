# coding:utf-8

# from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader, Context


# Create your views here.
def index(request):
    # 现在显示index.html
    t = loader.get_template("index.html")
    # 在HTML里嵌入???
    user = {"name": "tom", "age": 23, "sex": "male"}
    c = Context({"title": "django", "name": user})
    return HttpResponse(t.render())

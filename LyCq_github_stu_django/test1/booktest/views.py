from django.shortcuts import render
from django.http import HttpResponse

def index(req):
    return HttpResponse('hello world')

def detail(req, n1, n2, n3):
    return HttpResponse("year:%s,month:%s,date:%s"%(n1, n2, n3))

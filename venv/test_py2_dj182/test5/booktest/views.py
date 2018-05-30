from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
from models import *
from django.core.paginator import *

def index(request):
    return render(request, 'booktest/index.html')

def my_exp(request):
    a1 = int('abc')
    return HttpResponse('hello')

def upload_pic(request):
    return render(request, 'booktest/upload_pic.html')

def upload_handle(request):
    pic1 = request.FILES['pic1']
    pic_name = os.path.join(settings.MEDIA_ROOT, pic1.name)
    with open(pic_name, 'w') as pic:
        for i in pic1.chunks():
            pic.write(i)
    return HttpResponse('<img src="/static/media/%s"/>' % pic1.name)

# many page
def hero_list(request, pindex):
    if pindex == '':
        pindex = '1'
    list = HeroInfo.objects.all()
    paginator = Paginator(list, 5)
    page = paginator.page(int(pindex))
    context = {'page': page}
    return render(request, 'booktest/hero_list.html', context)

# area query
def area(request):
    return render(request, 'booktest/area.html')

def area2(request, id):
    id1 = int(id)
    if id1 == 0:
        data = AreaInfo.objects.filter(parea__isnull=True).values()
    else:
        data = [{}]
    list = []
    for area in data:
        list.append([area.id, area.title])

    return JsonResponse({'data': list})
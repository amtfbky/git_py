from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^my_exp$', views.my_exp),
    url(r'^upload_pic$', views.upload_pic),
    url(r'^upload_handle$', views.upload_handle),
    url(r'^hero_list/(\d*)$', views.hero_list),
    url(r'^area/$', views.area),
    url(r'^area/(\d+)/$', views.area2),
]
from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    # 2018/05/30/ ==> 05/30/2018
    # url(r'^(?P<n3>\d+)/(?P<n1>\d+)/(?P<n2>\d+)/$', views.detail),
    url(r'^(?P<n1>\d+)/(?P<n2>\d+)/(?P<n3>\d+)/$', views.detail),
]
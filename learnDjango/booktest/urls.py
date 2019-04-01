# -*- coding:utf-8 -*-
# Author:Gehao
from django.conf.urls import  url

from booktest import views

urlpatterns=[
    #url(r'^$',views.index),#booktest/后面为空就会匹配到这个view函数上
    url(r'^$',views.index,name='index'),
    url(r'^(\d+)$',views.show), #提取出来的值，被 views.py 中的对应视图函数接收
    url(r'^getTest1/$',views.getTest1),
    url(r'^getTest2/$',views.getTest2),
    url(r'^getTest3/$',views.getTest3),
    url(r'^postTest1/$',views.postTest1),
    url(r'^postTest2/$',views.postTest2),
    url(r'^cookieTest/$',views.cookieTest),
    url(r'^redTest1/$',views.redTest1),
    url(r'^redTest2/$',views.redTest2)
]
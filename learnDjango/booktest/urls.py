# -*- coding:utf-8 -*-
# Author:Gehao
from django.conf.urls import  url

from booktest import views

urlpatterns=[
    url(r'^$',views.index),#booktest/后面为空就会匹配到这个view函数上
    url(r'^(\d+)$',views.show) #提取出来的值，被 views.py 中的对应视图函数接收
]
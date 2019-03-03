# -*- coding:utf-8 -*-
# Author:Gehao
from django.conf.urls import  url

from booktest import views

urlpatterns=[
    url(r'^$',views.index)
]
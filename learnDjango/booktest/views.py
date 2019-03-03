from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
# Create your views here.
def index(request):#第一个参数是request
    #temp = loader.get_template('booktest/index.html')#加载模板,返回一个模板对象
    #return HttpResponse(temp.render())#render()渲染模板
    return render(request,'booktest/index.html')#渲染模板,加载
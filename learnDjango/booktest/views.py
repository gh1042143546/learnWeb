from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import *
# Create your views here.

def index(request):#第一个参数是request
    #temp = loader.get_template('booktest/index.html')#加载模板,返回一个模板对象
    #return HttpResponse(temp.render())#render()渲染模板
    booklist = BookInfo.objects.all()
    context = {'list':booklist}
    return render(request,'booktest/index.html',context)#渲染模板,加载
def show(request,id):
    book = BookInfo.objects.get(pk=id)
    herelist = book.heroinfo_set.all()
    context = {'list':herelist}
    return render(request,'booktest/show.html',context)
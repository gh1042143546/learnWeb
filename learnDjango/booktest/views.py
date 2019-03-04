from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
from .models import *
# Create your views here.

def index(request):#��һ��������request
    #temp = loader.get_template('booktest/index.html')#����ģ��,����һ��ģ�����
    #return HttpResponse(temp.render())#render()��Ⱦģ��
    booklist = BookInfo.objects.all()
    context = {'list':booklist}
    return render(request,'booktest/index.html',context)#��Ⱦģ��,����
def show(request,id):
    book = BookInfo.objects.get(pk=id)
    herelist = book.heroinfo_set.all()
    context = {'list':herelist}
    return render(request,'booktest/show.html',context)
from django.shortcuts import render
from django.http import *
from django.template import RequestContext,loader
# Create your views here.
def index(request):#��һ��������request
    #temp = loader.get_template('booktest/index.html')#����ģ��,����һ��ģ�����
    #return HttpResponse(temp.render())#render()��Ⱦģ��
    return render(request,'booktest/index.html')#��Ⱦģ��,����
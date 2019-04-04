# -*- coding:utf-8 -*-
from django.shortcuts import render,redirect
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
def show(request,id):#接收正则提取出来的值
    book = BookInfo.objects.get(pk=id)
    herelist = book.heroinfo_set.all()
    context = {'list':herelist}
    return render(request,'booktest/show.html',context)
def getTest1(request):
    return render(request,'booktest/getTest1.html')
def getTest2(request):
    #根据键接收值
    a = request.GET['a']
    b = request.GET['b']
    context = {'a':a,'b':b}
    return render(request,'booktest/getTest2.html',context)
def getTest3(request):
    a = request.GET.getlist('a')
    b = request.GET['b']
    context = {'a':a,'b':b}
    return render(request,'booktest/getTest3.html',context)

def postTest1(request):
    return render(request,'booktest/postTest1.html')

def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}
    return render(request,'booktest/postTest2.html',context)
#cookie 练习
def cookieTest(request):
    #request.COOKIES
    response=HttpResponse()
    cookie = request.COOKIES
    if cookie.__contains__('t1'):
        response.write(cookie['t1'])
    #response.set_cookie('t1','abc')服务端设置cookie值，浏览器请求后保存该值，后面再次请求这个网站时自动带上cookie的值
    return response

#重定向练习
def redTest1(request):
    #return HttpResponseRedirect('/booktest/redTest2/')
    return redirect('/booktest/redTest2/')
def redTest2(request):
    return HttpResponse("重定向")

#session练习
def session1(request):
    uname=request.session.get('myname','未登录')
    #uname = None
    context = {'uname':uname}
    return render(request,'booktest/session1.html',context)
def session2(request):
    return render(request,'booktest/session2.html')
def session_handle(request):
    request.session['myname']=request.POST['uname']
    request.session.set_expiry(0)#设置有效时间，关闭浏览器失效
    return redirect('/booktest/session1/')

def session3(request):
    #删除session
    del request.session['myname']
    return redirect('/booktest/session1/')

#session依赖于cookie，cookie中的sessionID就是用来传递session值的

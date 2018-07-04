# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from models import *
# Create your views here.


def index_view(request):
    uname = request.session['admin_name']
    booklist = BookBorrow.objects.all().order_by('-borrow_num')[:3]
    return render(request, 'index.html', {'uname': uname, 'booklist': booklist})



def index_view2(request):
    uname = request.session['admin_name']
    num = request.GET.get('num', 1)
    num = int(num)

    booklist = BookBorrow.objects.all().order_by('-borrow_num')
    size = 2
    paginator = Paginator(booklist, size)

    try:
        t_per_page = paginator.page(num)  # 获取当前页码的记录
    except PageNotAnInteger:  # 如果用户输入的页码不是整数时,显示第1页的内容
        t_per_page = paginator.page(1)
    except EmptyPage:  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        t_per_page = paginator.page(paginator.num_pages)

    # 每页开始页码
    begin = (num - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1

    # 每页结束页码
    end = begin + 9
    if end > paginator.num_pages:
        end = paginator.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pagelist = range(begin, end + 1)


    return render(request, 'more.html', {'uname': uname, 'paginator': paginator, 't_per_page': t_per_page, 'pagelist': pagelist})



def login_view(request):
    if request.method == 'GET':
        #cookies信息
        if request.COOKIES.has_key('loginUser'):
            loginUser = request.COOKIES.get('loginUser', '').split(',')
            name = loginUser[0]
            pwd = loginUser[1]

            return render(request, 'login.html', {'name': name, 'pwd': pwd})
        #如果请求方式是get就直接显示登录界面
        return render(request,'login.html')
    else:
        # 1.获取请求参数
        name = request.POST.get('name')
        PWD = request.POST.get('pwd')
        flag = request.POST.get('flag')
        response = HttpResponse()
        if Admin.objects.filter(admin_name=name,admin_password=PWD):
            request.session['admin_name'] = name
            response.status_code = 302
            response.setdefault('Location', '/')
            if flag == '1':
                response.set_cookie('loginUser', name + ',' + PWD, max_age=3 * 24 * 60 * 60, path='/login/')

                return response
            else:
                response.delete_cookie('loginUser', path='/login/')
                return response
        else:
            response.delete_cookie('loginUser', path='/login/')
            response.status_code = 302
            response.setdefault('Location', '/login/')
            return response


def manager_view(request):
    uname = request.session['admin_name']
    managerList = Admin.objects.all()
    return render(request, 'manager.html', {'uname': uname,'managerList':managerList})



def change_view(request):
    uname = request.session['admin_name']
    return render(request, 'pwd_Modify.html', {'uname': uname})


def reader_view(request):
    uname = request.session['admin_name']
    readerlist = Reader.objects.all()
    return render(request, 'reader.html', {'uname': uname, 'readerlist': readerlist})


def library_view(request):
    uname = request.session['admin_name']
    #页面展示图书馆信息
    if request.method == 'GET':
        lib_list = LibraryInfo.objects.all()
        #如果不为空，直接查询展示图书馆信息
        if lib_list:
            lib = lib_list[0]
            return render(request, 'library_modify.html',{'lib':lib,'uname': uname})
        #如果为空，渲染初始表单页面

        return render(request, 'library_modify.html',{'uname': uname})

    #增加或者修改图书馆信息
    if request.method == 'POST':
        #如果为空，获取到一个空占位符
        lib_id = request.POST.get('lib_id')
        if len(lib_id)==0:
            lib_id = 0

        lib_id = int(lib_id)

        lib_name = request.POST.get('libraryname','')
        lib_manager = request.POST.get('curator','')
        lib_phone = request.POST.get('tel','')
        lib_location = request.POST.get('address','')
        lib_email = request.POST.get('email','')
        lib_url = request.POST.get('url','')
        lib_build = request.POST.get('createDate','')
        lib_info = request.POST.get('introduce','')
        #查询是否已存在图书馆信息
        libobj = LibraryInfo.objects.filter(lib_id=lib_id)
        #如果为空，直接创建一个对象
        if not libobj:
            LibraryInfo.objects.create(lib_name=lib_name,lib_manager=lib_manager,lib_phone=lib_phone,lib_location=lib_location,lib_email=lib_email,lib_url=lib_url,lib_build=lib_build,lib_info=lib_info)
        #如果已存在，只进行更新信息
        else:
            libobj.update(lib_name=lib_name,lib_manager=lib_manager,lib_phone=lib_phone,lib_location=lib_location,lib_email=lib_email,lib_url=lib_url,lib_build=lib_build,lib_info=lib_info)

        return HttpResponseRedirect('/lm/libraryModify/')


def readerType_view(request):
    uname = request.session['admin_name']
    readerTypelist = ReaderType.objects.all()
    return render(request, 'readerType.html', {'uname': uname, 'readerTypelist': readerTypelist})


def parameter_view(request):
    uname = request.session['admin_name']
    return render(request, 'parameter_modify.html', {'uname': uname})


def bremind_view(request):
    uname = request.session['admin_name']
    borrowlist = BookBorrow.objects.all()
    return render(request, 'bremind.html', {'uname': uname, 'borrowlist': borrowlist})


def borrowQuery_view(request):
    uname = request.session['admin_name']
    borrowlist = BookBorrow.objects.all()

    return render(request, 'borrowQuery.html', {'uname': uname, 'borrowlist': borrowlist})


def bookType_view(request):
    uname = request.session['admin_name']
    bookTypelist = BookType.objects.all()
    return render(request, 'bookType.html', {'uname': uname, 'bookTypelist': bookTypelist})


def bookRenew_view(request):
    uname = request.session['admin_name']
    return render(request, 'bookRenew.html', {'uname': uname})


def bookQuery_view(request):
    uname = request.session['admin_name']
    booklist = Book.objects.all()
    return render(request, 'bookQuery.html', {'uname': uname, 'booklist': booklist})


def bookcase_view(request):
    uname = request.session['admin_name']
    return render(request, 'bookcase.html', {'uname': uname})


def bookBorrow_view(request):
    uname = request.session[u'admin_name']
    return render(request, 'bookBorrow.html', {'uname': uname})


def bookBack_view(request):
    uname = request.session['admin_name']
    return render(request, 'bookBack.html', {'uname': uname})


def book_view(request):
    uname = request.session['admin_name']
    booklist = Book.objects.all()
    return render(request, 'book.html', {'uname': uname, 'booklist': booklist})
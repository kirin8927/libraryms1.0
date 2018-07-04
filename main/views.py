# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from main.models import *


def index_view(request):
    uname = request.session.get('admin_name')
    return render(request,'index.html',{'uname':uname})


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

        # # 2.查询数据库
        # if name and PWD :
        #     c = Admin.objects.filter(admin_name=name,admin_password=PWD).count()
        #     if c == 1:
        #         request.session['admin_name'] = name
        #         return render(request,'index.html',{'name':name})
        # try:
        #     passwd_db = TbManager.objects.get(name=name).password
        # except:
        #     messages.add_message(request,messages.WARNING,'找不到用户')
        #     return  render(request,'login.html',{'login_info_list':'请使用正确的账号密码'})
        # if PWD == passwd_db:
        #     request.session['name'] = name
        #     request.session.set_expiry(600)
        #     return render(request,'index.html',{'welcome':'欢迎你'})
        # else:
        #     messages.add_message(request,messages.WARNING,'密码错误')
        #     return render(request,'login.html',{'login_info_list':'请使用正确的账号密码'})

        # 3.判断是否登录成功
        # return redirect('/login/')


def manager_view(request):
    uname = request.session['admin_name']
    managerList = Admin.objects.all()
    return render(request, 'manager.html', {'uname': uname,'managerList':managerList})





def change_view(request):
    uname = request.session.get('admin_name')
    return render(request,'pwd_Modify.html',{'uname':uname})


def reader_view(request):
    uname = request.session.get('admin_name')
    readerlist = Reader.objects.all()
    return render(request,'reader.html',{'uname':uname,'readerlist':readerlist})


def library_view(request):
    uname = request.session.get('admin_name')
    if request.method == 'GET':
        lib_list = LibraryInfo.objects.all()
        return render(request, 'library_modify.html',{'uname': uname,'lib_list':lib_list})
    if request.method == 'POST':
        lib_name = request.POST.get('libraryname','')
        lib_manager = request.POST.get('curator','')
        lib_phone = request.POST.get('tel','')
        lib_location = request.POST.get('address','')
        lib_email = request.POST.get('email','')
        lib_url = request.POST.get('url','')
        lib_build = request.POST.get('createDate','')
        lib_info = request.POST.get('introduce','')
        if not LibraryInfo.objects.all():
            LibraryInfo.objects.create(lib_name=lib_name,lib_manager=lib_manager,lib_phone=lib_phone,lib_location=lib_location,lib_email=lib_email,lib_url=lib_url,lib_build=lib_build,lib_info=lib_info)
        else:
            LibraryInfo.objects.filter(lib_id=1).update(lib_name=lib_name,lib_manager=lib_manager,lib_phone=lib_phone,lib_location=lib_location,lib_email=lib_email,lib_url=lib_url,lib_build=lib_build,lib_info=lib_info)
        lib_list = LibraryInfo.objects.all()
        return render(request,'library_modify.html',{'lib_list':lib_list,'uname': uname})



def readerType_view(request):
    uname = request.session.get('admin_name')
    readerTypelist = ReaderType.objects.all()
    return render(request,'readerType.html',{'uname':uname,'readerTypelist':readerTypelist})


def parameter_view(request):
    uname = request.session.get('admin_name')
    return render(request,'parameter_modify.html',{'uname':uname})


def bremind_view(request):
    uname = request.session.get('admin_name')
    borrowlist = BookBorrow.objects.all()
    return render(request,'bremind.html',{'uname':uname,'borrowlist':borrowlist})


def borrowQuery_view(request):
    uname = request.session.get('admin_name')
    borrowlist = BookBorrow.objects.all()

    return render(request,'borrowQuery.html',{'uname':uname,'borrowlist':borrowlist})


def bookType_view(request):
    uname = request.session.get('admin_name')
    bookTypelist = BookType.objects.all()
    return render(request,'bookType.html',{'uname':uname,'bookTypelist':bookTypelist})


def bookRenew_view(request):
    uname = request.session.get('admin_name')
    return render(request,'bookRenew.html',{'uname':uname})


def bookQuery_view(request):
    uname = request.session.get('admin_name')
    booklist = Book.objects.all()
    return render(request,'bookQuery.html',{'uname':uname,'booklist':booklist})


def bookcase_view(request):
    uname = request.session.get('admin_name')
    return render(request,'bookcase.html',{'uname':uname})


def bookBorrow_view(request):
    uname = request.session.get('admin_name')
    return render(request,'bookBorrow.html',{'uname':uname})


def bookBack_view(request):
    uname = request.session.get('admin_name')
    return render(request,'bookBack.html',{'uname':uname})


def book_view(request):
    uname = request.session.get('admin_name')
    booklist = Book.objects.all()
    return render(request,'book.html',{'uname':uname,'booklist':booklist})


def base_view(request):
    uname = request.session.get('admin_name')
    return render(request,'base.html',{'uname':uname})


def more_view(request):
    uname = request.session.get('admin_name')
    return render(request,'more.html',{'uname':uname})


def sign_view(request):
    uname = request.session.get('admin_name')
    if request.method == 'GET':
        adminlist = Admin.objects.all()

        return render(request,'register.html',{'uname':uname,'adminlist':adminlist})
    if request.method == 'POST':
        admin_name = request.POST.get('adminname', '')
        pwd = request.POST.get('password', '')
        admin_jurisdiction = int(request.POST.get('power', ''))
        admin_jurisdiction = Jurisdiction.objects.get(jurisdiction_id=admin_jurisdiction)
        tel = request.POST.get('tel', '')
        flag = Admin.objects.filter(admin_name=admin_name)
        if flag:
            return JsonResponse({'flag':True})


        Admin.objects.create(admin_name=admin_name,admin_password=pwd,admin_phone=tel,admin_jurisdiction=admin_jurisdiction)


        return HttpResponseRedirect('/manager/')



def bookcaseAdd_view(request):
    uname = request.session.get('admin_name')
    if request.method == 'GET':
        bookcaselist = BookStore.objects.all()

        return render(request,'bookcaseAdd.html',{'uname':uname,'bookcaselist':bookcaselist})
    if request.method == 'POST':
        store_name= request.POST.get('storename', '')

        store_id= request.POST.get('storeid', '')


        BookStore.objects.create( store_name=store_name,store_id=store_id)
        bookcaselist = BookStore.objects.all()
        return render(request,'bookcaseAdd.html',{'uname':uname,'bookcaselist':bookcaselist,'storename':store_name,'storeid':store_id})




def readerTypeAdd_view(request):
    uname = request.session.get('admin_name')
    if request.method == 'GET':
        readerTypelist = ReaderType.objects.all()

        return render(request,'readerTypeAdd.html',{'uname':uname,'readerTypelist':readerTypelist})
    if request.method == 'POST':
        reader_type= request.POST.get('readerTypename', '')

        reader_borrow_num= request.POST.get('borrowdays', '')
        r_obj = ReaderType.objects.filter(reader_type=reader_type)

        if r_obj:
            r_obj.update(reader_type=reader_type,reader_borrow_num=reader_borrow_num)
        else:

            ReaderType.objects.create( reader_type=reader_type,reader_borrow_num=reader_borrow_num)

        return HttpResponseRedirect('/readerType/')



def reader_add_view(request):
    uname = request.session.get('admin_name')
    if request.method == 'GET':
        readerlist = Reader.objects.all()
        reader_type_list = ReaderType.objects.all()
        return render(request,'readerAdd.html',{'uname':uname,'readerlist':readerlist,'reader_type_list':reader_type_list})
    if request.method == 'POST':
        reader_name = request.POST.get('readername', '')
        reader_id = int(request.POST.get('readerid', ''))
        reader_type= int(request.POST.get('readerType', ''))
        reader_type =ReaderType.objects.get(readertype_id=reader_type)
        reader_card = request.POST.get('readercard', '')
        # reader_card_num = request.POST.get('readercardnum', '')
        reader_phone = request.POST.get('tel', '')
        reader_email = request.POST.get('email', '')
        roj = Reader.objects.filter(reader_card=reader_card)
        if roj:
            print('用户已经存在')
        else:
            r = Reader(reader_name=reader_name,reader_id=reader_id, reader_type=reader_type,reader_card=reader_card,reader_phone=reader_phone,reader_email=reader_email)
            r.save()
        return HttpResponseRedirect('/reader/')



def bookTypeAdd_view(request):
    uname = request.session.get('admin_name')
    if request.method == 'GET':
        bookTypelist = BookType.objects.all()

        return render(request,'bookTypeAdd.html',{'uname':uname,'bookTypelist':bookTypelist})
    if request.method == 'POST':
        book_type= request.POST.get('bookTypename', '')

        borrow_days= request.POST.get('borrowdays', '')
        roj = BookType.objects.filter(book_type=book_type)
        if roj:
            print('用户已经存在')
        else:
            BookType.objects.create( book_type=book_type,borrow_days=borrow_days)

        return HttpResponseRedirect('/bookType/')





def book_add_view(request):
    uname = request.session.get('admin_name')
    if request.method == 'GET':
        booklist = Book.objects.all()
        booktype_list = BookType.objects.all()
        bookstore_list = BookStore.objects.all()

        return render(request,'bookAdd.html',{'uname':uname,'booklist':booklist,'booktype_list':booktype_list,'bookstore_list':bookstore_list})
    if request.method == 'POST':
        book_name = request.POST.get('bookname', '')
        book_type = int(request.POST.get('booktype', ''))
        book_type = BookType.objects.get(booktype_id=book_type)
        book_store = int(request.POST.get('bookstore', ''))
        book_store = BookStore.objects.get(store_id=book_store)
        book_author = request.POST.get('bookauthor', '')
        book_publishing = request.POST.get('bookp', '')
        book_price = request.POST.get('bookprice', '')
        book_num = request.POST.get('booknum', '')

        Book.objects.create(book_name=book_name, book_type=book_type,book_store=book_store,book_author=book_author,book_publishing=book_publishing,book_price=book_price,book_num=book_num)
        return HttpResponseRedirect('/book/')
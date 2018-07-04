#coding=utf-8

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.index_view),
    url(r'^login/$',views.login_view),
    url(r'^manager/$',views.manager_view),
    url(r'^change_pwd/$',views.change_view),
    url(r'^reader/$',views.reader_view),
    url(r'^libraryModify/$',views.library_view),
    url(r'^parameterModify/$',views.parameter_view),
    url(r'^readerType/$',views.readerType_view),
    url(r'^bremind/$',views.bremind_view),
    url(r'^borrowQuery/$',views.borrowQuery_view),
    url(r'^bookType/$',views.bookType_view),
    url(r'^bookRenew/$',views.bookRenew_view),
    url(r'^bookQuery/$',views.bookQuery_view),
    url(r'^bookcase/$',views.bookcase_view),
    url(r'^bookBorrow/$',views.bookBorrow_view),
    url(r'^bookBack/$',views.bookBack_view),
    url(r'^book/$',views.book_view),
    url(r'^more/$',views.index_view2),
]
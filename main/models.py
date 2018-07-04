#coding=utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

# 书架模型类
class BookStore(models.Model):
    store_id = models.AutoField(primary_key=True)
    store_name = models.CharField(max_length=30)

# 图书类型模型类
class BookType(models.Model):
    booktype_id = models.AutoField(primary_key=True)
    book_type = models.CharField(max_length=30)
    borrow_days = models.IntegerField()

# 读者类型模型类
class ReaderType(models.Model):
    readertype_id = models.AutoField(primary_key=True)
    reader_type = models.CharField(max_length=30)
    reader_borrow_num = models.IntegerField(null=True,blank=True)

    def __unicode__(self):
        return u'ReaderType:%s,%s'%(self.reader_type,self.reader_borrow_num)

# 管理员权限模型类
class Jurisdiction(models.Model):
    jurisdiction_id = models.AutoField(primary_key=True)
    system_settings = models.BooleanField()
    reader_manage = models.BooleanField()
    boook_manage = models.BooleanField()
    book_return_borrow = models.BooleanField()
    system_search = models.BooleanField()

# 读者模型类
class Reader(models.Model):
    reader_id = models.AutoField(primary_key=True)
    reader_name = models.CharField(max_length=30)
    reader_type = models.ForeignKey(ReaderType,on_delete=models.CASCADE)
    reader_card = models.CharField(max_length=30)
    # reader_card_num = models.CharField(max_length=30)
    reader_phone = models.CharField(max_length=30)
    reader_email = models.CharField(max_length=30)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.reader_type = ReaderType.objects.get(reader_type=self.reader_type.reader_type)
        except ReaderType.DoesNotExist:
            self.reader_type = ReaderType.objects.create(reader_type=self.reader_type.reader_type,reader_borrow_num=self.reader_type.reader_borrow_num)

        return models.Model.save(self, force_insert, force_update, using,update_fields)
    def __unicode__(self):
        return u'Reader:%s,%s'%(self.reader_name,self.reader_card)
# 管理员模型类
class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=30)
    admin_password = models.CharField(max_length=30)
    admin_jurisdiction = models.ForeignKey(Jurisdiction,on_delete=models.CASCADE)
    admin_phone = models.CharField(max_length=30)

# 图书信息模型类
class Book(models.Model):
    book_id = models.AutoField(primary_key=30)
    book_name = models.CharField(max_length=30)
    book_store = models.ForeignKey(BookStore,on_delete=models.CASCADE)
    book_type = models.ForeignKey(BookType,on_delete=models.CASCADE)
    book_publishing = models.CharField(max_length=30)
    book_author = models.CharField(max_length=30)
    book_price = models.FloatField()
    book_num = models.IntegerField()

# 图书借阅信息模型类
class BookBorrow(models.Model):
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    reader_id = models.ForeignKey(Reader,on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    private_date = models.DateField()
    if_return = models.BooleanField()
    borrow_num = models.IntegerField()

    class Meta:
        unique_together = (('reader_id','book_id'),)

# 图书归还信息模型类
class BookReturn(models.Model):
    book_id = models.ForeignKey(Book,on_delete=models.CASCADE)
    reader_id = models.ForeignKey(Reader,on_delete=models.CASCADE)
    # borrow_date = models.DateField()
    return_date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = (('reader_id','book_id'),)

# 图书续借信息模型类
class BookRenewal(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    reader_id = models.ForeignKey(Reader, on_delete=models.CASCADE)
    # borrow_date = models.DateField()
    renewal_date = models.DateField()

    class Meta:
        unique_together = (('reader_id','book_id'),)

# 图书馆信息模型类
class LibraryInfo(models.Model):
    lib_id = models.AutoField(primary_key=True)
    lib_name = models.CharField(max_length=30)
    lib_manager = models.CharField(max_length=30)
    lib_phone = models.IntegerField()
    lib_location = models.CharField(max_length=30)
    lib_email = models.CharField(max_length=30)
    lib_url = models.CharField(max_length=30)
    lib_build = models.DateField()
    lib_info = models.TextField()

# 图书馆通行证信息模型类
class TransactionCard(models.Model):
    transactioncard_id = models.AutoField(primary_key=True)
    price = models.FloatField()
    indate = models.IntegerField()

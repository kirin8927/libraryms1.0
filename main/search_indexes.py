#coding=utf-8
from haystack import indexes
from main.models import *

#z注意格式
class BookIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True,use_template=True)

    #给title，content设置索引
    book_id = indexes.NgramField(model_attr='book_id')
    book_name = indexes.NgramField(model_attr='book_name')


    def get_model(self):
        return Book

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('book_id')
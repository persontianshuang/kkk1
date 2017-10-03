

from mongoengine import *


from settings.db import _connect

connect(_connect)

class KindleBooks(Document):
    '''
    集合： 显示在列表页的内容，句子，平假名，类型（video，song，text）
    '''

    book_raw_name = StringField()
    # 去掉括号的名字
    book_simple_name = StringField()

    book_url = StringField()
    book_img = StringField()


    def __str__(self):
        return self.book_raw_name






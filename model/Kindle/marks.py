
from mongoengine import *


from settings.db import _connect

connect(_connect)

class KindleMarks(Document):
    '''
    集合： 显示在列表页的内容，句子，平假名，类型（video，song，text）
    '''
    外键  用户  书
    user
    book_from
    content = StringField()
    find_page = StringField()
    read_time = DateTimeField()


    def __str__(self):
        return self. content





from mongoengine import *


from settings.db import _connect

connect(_connect)

class KindleMarks(Document):
    还是用Django吧
    content = StringField()
    find_page = StringField()
    read_time = DateTimeField()

    def __str__(self):
        return self.content




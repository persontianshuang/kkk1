from crawl.collection_dtails import CollectionDtails,raw_data
from settings.db import _db

coll = _db['zhihu_collection']

for x in raw_data:
    single = CollectionDtails(x).start()
    print(single)
    for y in single:
        coll.insert_many(y)

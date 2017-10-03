

# mongodb

import pymongo


_connect = 'kindle'

_host = 'localhost'

_port = 27017



_client = pymongo.MongoClient(_host,_port)
_db = _client[_connect]

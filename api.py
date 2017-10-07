from flask import Flask,jsonify,request
from datetime import datetime

# 静态文件的放置路径，可根据实际情况设置，这里设置为默认路径：'./static/'
api = Flask(__name__, static_url_path='')


from apps.kindle import kindle
from utils.domain import allow_cross_domain

from settings.db import _db
import random


@api.route('/kindle', methods=['GET'])
def rrr():
    f = _db['k2'].find({},{'_id':0})
    fl = f.count()
    nu = random.randint(0,fl)
    last = f[nu]
    return jsonify(last)


@api.route('/zhihu', methods=['GET'])
def zhihu():
    f = _db['zhihu_collection'].find({},{'_id':0})
    fl = f.count()
    nu = random.randint(0,fl)
    last = f[nu]
    return jsonify(last)




# 获取某个指定的单词
@api.route('/create', methods=['POST','OPTIONS'])
@allow_cross_domain
def create():
    print(request.json)
    data = {}
    # if request.json!=None and request.json['secret']=='sj':
    if request.json!=None:
        data['read_time'] = datetime.now()
        data['tag'] = request.json['tag']
        data['content'] = request.json['content']
        # data['find_url'] = request.json['url']
        _db['k2'].insert(data)
        print(data)
    return jsonify({'status': 200})



api.register_blueprint(kindle,url_prefix='/kindle')


if __name__ == '__main__':
    # api.run(debug=True,host='0.0.0.0',)
    api.run(host='0.0.0.0',port=8333)

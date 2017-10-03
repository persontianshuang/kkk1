from flask import Blueprint,jsonify


kindle = Blueprint('videos',__name__)



# 标记   笔记  TODO：评论
@kindle.route('/', methods=['GET'])
def all_videos():
    all = MgFlow().all_videos()
    return jsonify(all)




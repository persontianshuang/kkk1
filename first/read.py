import re


file = open('/Users/user/pynew/project/kindle/My Clippings.txt','rt',encoding='utf8')
clip = file.read()
clip_list = clip.split('==========')

# my_clip = tool.pymg('kindle','my_clip_lao')
for clip_any in clip_list:
    data = {}
    try:
        # print(clip_any)
        mes = [x for x in clip_any.split('\n') if x != '']
        # print(mes)
        name = re.sub('\ufeff','',mes[0])
        readDate = re.compile(r'(\d{4}年\d{1,2}月\d{1,2})').findall(mes[1])[0]
        findPage = re.compile(r'(\d+[-]\d+)').findall(mes[1])[0]
        content = mes[2]
        data = {
            'book_raw_name': name,
            'book_simple_name': name,
            'read_time': readDate,
            'findPage': findPage,
            'content': content,
        }
        print(data)
    except:
        print('_______')
        print(clip_any)
        print('_______')
    # try:
    #     my_clip.insert_one(data)
    # except:
    #     print('传入数据库失败')


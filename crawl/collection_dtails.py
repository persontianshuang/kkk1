import re

import requests
from lxml import html

def make_req(url):
    header = {}
    header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

    the_html = requests.get(url,headers=header).text
    response = html.fromstring(the_html)
    return response

# 具体的收藏夹
class CollectionDtails(object):

    def __init__(self,url):
        self.url = url
        self.collection_id = re.compile(r'collection/(\d+)').findall(self.url)[0].strip()

    # 获取页数，
    def get_page(self):
        req = make_req(self.url)
        xpa = '/html/body//div[@class="border-pager"]/div[@class="zm-invite-pager"]/span[last()-1]/a/text()'
        pages = req.xpath(xpa)
        if list(pages)==[]:
            return None
        else:
            return pages[0]

    # 生成待爬取的url
    def make_page_urls(self):
        page = self.get_page()
        if page:
            page_urls = [self.url+'?page={}'.format(str(x)) for x in range(1,int(page)+1)]
            return page_urls
        else:
            return [self.url]

    # 爬取收藏的文章或回答的id
    def get_artcle_or_answer_id(self,url):
        req = make_req(url)

        xpa = '//*[@id="zh-list-collection-wrap"]/div//a[@class="toggle-expand"]/@href'
        coll_xpa = '//*[@id="zh-fav-head-title"]/text()'
        coll_name = req.xpath(coll_xpa)[0].strip()
        results = req.xpath(xpa)
        info_list = []
        for x in results:
            data = {}
            if 'question' in x:
                qu = re.compile(r'/question/(\d+)/').findall(x)[0].strip()
                anw =re.compile(r'answer/(\d+)').findall(x)[0].strip()
                data['tag'] = 'answer'
                data['question'] = qu
                data['answer'] = anw
                data['collection_id'] = self.collection_id
                data['collection_name'] = coll_name
                info_list.append(data)

            else:
                article= x.strip('https://zhuanlan.zhihu.com/p/').strip()
                data['tag'] = 'article'
                data['article'] = article
                data['collection_id'] = self.collection_id
                data['collection_name'] = coll_name
                info_list.append(data)
        return info_list

    def start(self):
        info_list = []
        for x in self.make_page_urls():
            page = self.get_artcle_or_answer_id(x)
            if page!=[]:
               info_list.append(page)
        return info_list

# pg = Pag('https://www.zhihu.com//collection/186968788').start()
raw_data = ['https://www.zhihu.com//collection/186968788', 'https://www.zhihu.com//collection/159397945', 'https://www.zhihu.com//collection/172559256', 'https://www.zhihu.com//collection/162516977', 'https://www.zhihu.com//collection/145686016', 'https://www.zhihu.com//collection/68829553', 'https://www.zhihu.com//collection/132331007', 'https://www.zhihu.com//collection/132613823', 'https://www.zhihu.com//collection/42377980', 'https://www.zhihu.com//collection/132624063', 'https://www.zhihu.com//collection/77237800', 'https://www.zhihu.com//collection/69665894', 'https://www.zhihu.com//collection/101739722', 'https://www.zhihu.com//collection/69274065', 'https://www.zhihu.com//collection/115723985', 'https://www.zhihu.com//collection/101585908', 'https://www.zhihu.com//collection/114358622', 'https://www.zhihu.com//collection/42143968', 'https://www.zhihu.com//collection/69273856', 'https://www.zhihu.com//collection/69277606', 'https://www.zhihu.com//collection/104258476', 'https://www.zhihu.com//collection/104258873', 'https://www.zhihu.com//collection/115648482', 'https://www.zhihu.com//collection/109456313', 'https://www.zhihu.com//collection/68822833', 'https://www.zhihu.com//collection/71811940', 'https://www.zhihu.com//collection/113049070', 'https://www.zhihu.com//collection/68648939', 'https://www.zhihu.com//collection/97706444', 'https://www.zhihu.com//collection/115503591', 'https://www.zhihu.com//collection/113996896', 'https://www.zhihu.com//collection/113219224', 'https://www.zhihu.com//collection/108913631', 'https://www.zhihu.com//collection/100299513', 'https://www.zhihu.com//collection/98424582', 'https://www.zhihu.com//collection/97945846', 'https://www.zhihu.com//collection/90031041', 'https://www.zhihu.com//collection/86355671', 'https://www.zhihu.com//collection/82929346', 'https://www.zhihu.com//collection/77388932', 'https://www.zhihu.com//collection/69717048', 'https://www.zhihu.com//collection/71362204', 'https://www.zhihu.com//collection/42141948', 'https://www.zhihu.com//collection/69275298', 'https://www.zhihu.com//collection/71559354', 'https://www.zhihu.com//collection/69652768', 'https://www.zhihu.com//collection/69274503']

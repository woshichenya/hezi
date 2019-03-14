# -*- coding: utf-8 -*-

import sys
from Cookie import SimpleCookie

from plusSpider.db.tables.db_ims_plus_hot_gzh import VdImsPlusHotGzh

reload(sys)
sys.setdefaultencoding("utf-8")
import datetime
import json
import urllib
import requests

import scrapy
from plusSpider.items import PlusspiderItem, PlusspiderlineItem, PlusspiderPieItem, PlusspiderPieUpdateItem, \
    PlusspiderGzhUpdateItem, PlusspiderGzhItem, PlusspiderGzhInfoItem, PlusspiderGzhInfoUpdateItem
from plusSpider.db.utils import date_utils


class PlusSpiderSpider(scrapy.Spider):
    name = 'plus_spider'
    allowed_domains = ['data.xiaodianpu.com']
    # start_urls = ['http://data.xiaodianpu.com/']
    cookie = 'Hm_lvt_abe7a1f4564f3de2b0defe0b5c722991=1542077367,1542159695,1542162314,1542174523; Hm_lpvt_abe7a1f4564f3de2b0defe0b5c722991=1542181320; SESSION_SEE_DATA=02d29e3a-0b39-461b-bd4a-a8c453b8bf35; '
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            "Host": "data.xiaodianpu.com",
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
            # "Referer": "https://data.xiaodianpu.com/result.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            # "X-Requested-With": "XMLHttpRequest",
        },
        # "ITEM_PIPELINES": {},
        "LOG_FILE": "plus_see.log",
        "LOG_ENABLED": "True",
        "LOG_LEVEL": 'DEBUG',
        # "DOWNLOAD_DELAY": "2",
    }

    def start_requests(self):
        url = "https://portal.xiaodianpu.com/api/auth/login"
        yield scrapy.FormRequest(
            url=url,
            formdata={"username": "18610538450", "password": "tyc123456",
                      "see_api_time": datetime.datetime.now().strftime('%Y%m%d%H%M%S')},
            callback=self.parse
        )

    def parse(self, response):
        set_cookie = response.headers.getlist('Set-Cookie')
        if len(set_cookie[0]) > len(set_cookie[1]):
            self.cookie += set_cookie[0].split(' ')[0]
        else:
            self.cookie += set_cookie[1].split(' ')[0]
        self.cookie = {i.key: i.value for i in SimpleCookie(self.cookie).values()}
        url = 'https://data.xiaodianpu.com/api/hotword-service/home/v1/wordList?'
        param_data = {'showType': 0, 'categoryId': -1, 'page': 1, 'pageSize': 10}
        data = urllib.urlencode(param_data)
        # for i in range(1, 11):
        #     param_data['page'] = i
        #     yield scrapy.Request( url + data , callback=self.parse_item)
        yield scrapy.Request(url + data, cookies=self.cookie, callback=self.parse_word_List)

    def parse_word_List(self, response):
        word_List = json.loads(response.body)
        # url_hot = 'https://data.xiaodianpu.com/result.html#/hot?'
        url_head_base = 'https://data.xiaodianpu.com/api/hotword-service/hotword/detail/v1/headBase?'
        url_article = 'https://data.xiaodianpu.com/api/hotword-service/hotword/detail/v1/articleList?'
        url_line = 'https://data.xiaodianpu.com/api/hotword-service/hotword/detail/v1/lineChart?'
        url_cr_pie = 'https://data.xiaodianpu.com/api/hotword-service/hotword/detail/v1/crPieChart?'
        # print word_List['items']
        for it in word_List['items']:
            param_data_article = {'keyword': it['keyword'], 'showType': 0, 'page': 1, 'pageSize': 8, 'total': 0}
            data_article = urllib.urlencode(param_data_article)
            param_data_line = {'keyword': it['keyword'], 'showType': 1, 'dateType': 7}
            data_line = urllib.urlencode(param_data_line)
            param_data_keyword = {'keyword': it['keyword']}
            data_keyword = urllib.urlencode(param_data_keyword)
            yield scrapy.Request(url_article + data_article, cookies=self.cookie, meta={'keyword': it['keyword']}, callback=self.parse_article)
            yield scrapy.Request(url_line + data_line, cookies=self.cookie, meta={'keyword': it['keyword']}, callback=self.parse_line)
            yield scrapy.Request(url_cr_pie + data_keyword, cookies=self.cookie, meta={'keyword': it['keyword']}, callback=self.parse_cr_pie)
            yield scrapy.Request(url_head_base + data_keyword, cookies=self.cookie, callback=self.parse_head_base)
            # print url_hot + data_hot
            # yield SplashRequest(url_hot + data_hot, cookies=self.cookie, callback=self.parse_hot,args={'wait': 3})
            break

    def parse_article(self, response):
        print response
        print '---------parse_article---------'
        item = PlusspiderItem()
        item_list = json.loads(response.body)['items']  # 将获取到的数据转为json格式
        print item_list
        url_base = 'https://data.xiaodianpu.com/api/wechat-kol-service/kol/detail/v1/base?'
        for data in item_list:
            item['title'] = data['title']
            item['url'] = data['url']
            item['gzh_biz'] = data['biz']
            item['gzh_title'] = data['wechat_name']
            item['read_sum'] = data['read_num']
            item['agree_sum'] = data['like_num']
            item['hot_word_title'] = response.meta['keyword']
            item['article_class'] = data['category_name']
            item['create_time'] = data['push_time']
            param_data_biz = {'biz': data['biz']}
            data_biz = urllib.urlencode(param_data_biz)
            yield scrapy.Request(url_base + data_biz, cookies=self.cookie, callback=self.parse_base)
            yield item


    def parse_line(self, response):
        print '--------parse_line----------'
        item = PlusspiderlineItem()
        item_list = json.loads(response.body)  # 将获取到的数据转为json格式
        for data in item_list:
            item['hot_word_title'] = response.meta['keyword']
            item['read_sum'] = data['read_num']
            item['agree_sum'] = data['like_num']
            item['article_sum'] = data['article_num']
            item['create_date'] = date_utils.system_time()
            yield item

    def parse_cr_pie(self, response):
        print '------- parse_cr_pie-----------'
        item = PlusspiderPieItem()
        item_list = json.loads(response.body)  # 将获取到的数据转为json格式
        item['title'] = response.meta['keyword']
        item['gzh_class'] = item_list['category']
        item['gzh_article_read'] = item_list['read_mag']
        item['create_time'] = date_utils.system_time()
        yield item


    def parse_head_base(self, response):
        # 返回值{"keyword":"酒店","hot_score":94.93,"hot_rank":1,"latent_score":90.09,"latent_rank":1,"update_time":"2018-11-16 09:20:02","expo_flag":1}
        print '-------------parse_head_base-------------------'
        item = PlusspiderPieUpdateItem()
        item_json = json.loads(response.body)
        item['title'] = item_json['keyword']
        item['hot_rank'] = item_json['hot_rank']
        yield item


    def parse_base(self, response):
        # {"biz":"MjM5MjAxNDM4MA==","wechat_id":"rmrbwx","wechat_name":"人民日报","wechat_desc":"参与、沟通、记录时代。","head_img_url":"http://wx.qlogo.cn/mmhead/Q3auHgzwzM5Dlw4H8vWoicXPXccEVkWYgFE1pNUvX7uaHmafPODGIEA/132","qr_code_url":"https://mp.weixin.qq.com/mp/qrcode?scene=10000001&size=102&__biz=MjM5MjAxNDM4MA==&mid=2666224601&idx=3&sn=f46d9e17bd41a30028d710cd9e796818","kqi":"100.0","company":"人民日报","relative_kol_num":11,"is_100k_plus":true,"is_original":false,"category_id":25,"category_name":"时事","has_voice":true,"has_video":true,"migration":1,"has_music":false,"has_mini_prog":false,"original_rate":0.0,"buying_price_min":73.54,"buying_price_max":241.86,"buying_desire":27.863295,"interactive_score":99.79,"head_read_num":100001.0,"head_like_num":15785.0,"other_read_num":100001.0,"other_like_num":4609.0,"publish_times_2week":133,"article_num_2week":317,"update_time":"2018-11-16 03:24:57","push_time":1542284875}
        print '-------------parse_base-------------------'
        item = PlusspiderGzhItem()
        item_json = json.loads(response.body)
        item['biz'] = item_json['biz']
        item['uin_hao'] = item_json['wechat_id']
        item['logo'] = item_json['head_img_url']
        item['title'] = item_json['wechat_name']
        if item_json['company'] is None:
            item['auth'] = '个人'
        else:
            item['auth'] = item_json['company']
        item['qr_code_url'] = item_json['qr_code_url']
        item['new_send_time'] = date_utils.str_time_stamp(str(item_json['update_time']), 0)
        item['create_time'] = date_utils.system_time()
        yield item


class PlusSpiderSpiderWxb(scrapy.Spider):
    name = 'plus_spider_wxb'
    allowed_domains = ['data.wxb.com','account.wxb.com']
    start_urls = ["http://account.wxb.com/"]
    cookie = 'Hm_lvt_5859c7e2fd49a1739a0b0f5a28532d91=1542104566; visit-wxb-id=cb47ec8679332ee4be0b634f1ab14609; wxb_fp_id=4153882519; aliyungf_tc=AQAAAAxoDVa26QIAOhxFecKf9Jfcfpnd; PHPSESSID=44c9c16c18c5ad9ca530f36a7f5fe1c3; '
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            # "Host": "data.wxb.com",
            "Connection": "keep-alive",
            "Accept": "application/json, text/plain, */*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36",
            # "Referer": "https://data.xiaodianpu.com/result.html",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8",
            "X-Requested-With": "XMLHttpRequest",
        },
        # "ITEM_PIPELINES": {},
        "LOG_FILE": "plus_wxb.log",
        "LOG_ENABLED": "True",
        "LOG_LEVEL": 'DEBUG',
        # "DOWNLOAD_DELAY": "2",
    }
    def parse(self, response):
        set_cookie = response.headers.getlist('Set-Cookie')
        self.cookie += set_cookie[0].split(' ')[0] + ' '
        self.cookie += set_cookie[1].split(' ')[1]
        self.cookie = {i.key: i.value for i in SimpleCookie(self.cookie).values()}
        return scrapy.FormRequest(
            url='https://account.wxb.com/login',
            formdata={"email": "18811084140", "password": "090911",
                      "captcha": ""},
            cookies=self.cookie,
            callback=self.parse_search_vipcn
        )

    def parse_search_vipcn(self, response):
        # TODO 数据库查询公众号名称
        for gzh in VdImsPlusHotGzh({}).select_gzh_all():
            vipcn = PlusSpiderSpiderWxb.get_search(gzh.uin_hao)['data'][0]['wx_origin_id']
            url = 'https://data.wxb.com/details/postRead?id=%s' % vipcn
            yield scrapy.Request(url, meta={'vipcn_id': vipcn, 'biz': gzh.biz, 'gzh_title': gzh.title}, callback=self.parse_vipcn)
        # vipcn = PlusSpiderSpiderWxb.get_search('rmrbwx')['data'][0]['wx_origin_id']
        # url = 'https://data.wxb.com/details/postRead?id=%s' % vipcn
        # yield scrapy.Request(url, meta={'vipcn_id': vipcn, 'biz': 'MjM5MjAxNDM4MA==', 'gzh_title': '人民日报'}, callback=self.parse_vipcn)

    def parse_vipcn(self, response):
        print '-------------- parse_vipcn ------------------'
        item = PlusspiderGzhUpdateItem()
        vipcn = response.xpath('//div[@class="detail-overview"]/div')
        # 账号主体
        # vipcn.xpath('./div[@class="content company"]/text()').extract()[0]
        # 分类
        # vipcn.xpath('./div[@class="content category"]/text()').extract()[0]
        total = vipcn.xpath('./div[@class="inform-wrap"]/div[@class="inform-item"]')
        # 微信名称
        # total.xpath('./span/text()').extract()[0]
        # 二维码
        # vipcn.xpath('//div[@class="wxb-avatar-img"]/img/@src/text()').extract()[0]
        # 发文情况
        dispatch = response.xpath('//div[@class="card-number"]/text()').extract()
        # 阅读量
        pv_views = response.xpath('//div[@class="ant-card-body"]/div[@class="item"]/div/text()').extract()
        # 最高点赞数
        # pv_views[4]
        model = '10万+'  # 表示10万+
        model1 = '100001'  # 将10万+替换成整型100001
        # 功能介绍：参与、沟通、记录时代。
        item['remark'] = total.xpath('./div[@class="content"]/text()').extract()[1]
        # 发文次数
        item['send_article_sum'] = int(dispatch[0])
        # 每次平均发文篇数
        item['average_send_article'] = float(dispatch[1])
        # 头条平均阅读量
        item['average_top_read'] = model1 if model == pv_views[0] else pv_views[0]
        # 非头条平均阅读量
        item['average_nottop_read'] = model1 if model == pv_views[2] else pv_views[2]
        # 最高阅读量
        item['max_read_sum'] = model1 if model == pv_views[4] else pv_views[4]
        # 头条平均点赞数
        item['average_top_agree'] = model1 if model == pv_views[6] else pv_views[6]
        # 微信号：rmrbwx
        item['uin_hao'] = total.xpath('./div[@class="content"]/text()').extract()[0]
        print item
        url_chart = 'https://data.wxb.com/account/statChart/%s?period=7&start_date=&end_date=' % response.meta['vipcn_id']
        yield scrapy.Request(url_chart,cookies=self.cookie, meta={'biz': response.meta['biz'], 'gzh_title': response.meta['gzh_title']}, callback=self.parse_stat_chart)
        url_rank = 'https://data.wxb.com/account/rank/%s?period=7&start_date=&end_date=' % response.meta['vipcn_id']
        yield scrapy.Request(url_rank, cookies=self.cookie, meta={'biz': response.meta['biz'], 'gzh_title': response.meta['gzh_title']}, callback=self.parse_stat_rank)

        yield item

    def parse_stat_chart(self, response):
        print '--------parse_stat_chart---------'
        item = PlusspiderGzhInfoItem()
        item_list = json.loads(response.body, encoding='utf-8')['data']
        for key, values in item_list.items():
            item['gzh_title'] = response.meta['gzh_title']
            item['gzh_biz'] = response.meta['biz']
            item['read_sum'] = values['read_num_total']
            item['top_read_sum'] = values['top_read_num_total']
            item['agree_sum'] = values['like_num_total']
            item['top_agree_sum'] = values['top_like_num_total']
            item['send_read_sum'] = values['articles_total']
            item['create_time'] = date_utils.str_time_stamp(str(key), 1)
            yield item

    def parse_stat_rank(self, response):
        print '--------parse_stat_rank---------'
        item = PlusspiderGzhInfoUpdateItem()
        item_list = json.loads(response.body, encoding='utf-8')['history_rank']
        for key, values in item_list.items():
            item['gzh_biz'] = response.meta['biz']
            item['ranking'] = values['rank']
            item['create_time'] = date_utils.str_time_stamp(str(key), 1)
            yield item


    @staticmethod
    def get_search(kw):
        url = "https://data.wxb.com/search"
        querystring = {"page": "1", "page_size": "10", "kw": kw, "category_id": "", "start_rank": "*",
                       "end_rank": "*",
                       "fans_min": "", "fans_max": "", "is_verify": "0", "is_original": "0", "is_continuous": "0"}
        headers = {
            'accept': "application/json, text/plain, */*",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
            'connection': "keep-alive",
            'cookie': "aliyungf_tc=AQAAANTM9F5nqw4AxpNuJDUMUROMlLBI; visit-wxb-id=23d1de18465acdf97efb030c699b72a6; wxb_fp_id=635308960; Hm_lvt_5859c7e2fd49a1739a0b0f5a28532d91=1542160082; Hm_lpvt_5859c7e2fd49a1739a0b0f5a28532d91=1542160082; PHPSESSID=ae5c7be5c117db7feccd03e4bf1301fa",
            'host': "data.wxb.com",
            'referer': "https://data.wxb.com/searchResult?kw=%E4%BA%BA%E6%B0%91%E6%97%A5%E6%8A%A5&page=1",
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
            'x-requested-with': "XMLHttpRequest",
            'cache-control': "no-cache",
            'postman-token': "3be6ce3e-5d0f-0f6f-b9f4-794a3a5fd625"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        # print json.loads(response.text)
        return json.loads(response.text)

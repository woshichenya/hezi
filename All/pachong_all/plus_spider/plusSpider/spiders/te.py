# # -*- coding: utf-8 -*-
#
#
# import sys
#
# reload(sys)
# sys.setdefaultencoding("utf-8")
# import json
# from Cookie import SimpleCookie
#
# import scrapy
# import requests
#
# class PlusSpiderSpiderWxb(scrapy.Spider):
#     name = 'plus_spider_wxb'
#     allowed_domains = ['data.wxb.com','account.wxb.com']
#
#     start_urls = ["http://account.wxb.com/"]
#     cookie = 'Hm_lvt_5859c7e2fd49a1739a0b0f5a28532d91=1542104566; visit-wxb-id=cb47ec8679332ee4be0b634f1ab14609; wxb_fp_id=4153882519; aliyungf_tc=AQAAAAxoDVa26QIAOhxFecKf9Jfcfpnd; PHPSESSID=44c9c16c18c5ad9ca530f36a7f5fe1c3; '
#     vipcn = ''
#     def parse(self, response):
#         set_cookie = response.headers.getlist('Set-Cookie')
#         self.cookie += set_cookie[0].split(' ')[0] + ' '
#         self.cookie += set_cookie[1].split(' ')[1]
#         self.cookie = {i.key: i.value for i in SimpleCookie(self.cookie).values()}
#         return scrapy.FormRequest(
#                     url='https://account.wxb.com/login',
#                     formdata={"email": "18811084140", "password": "090911",
#                               "captcha": ""},
#                     cookies=self.cookie,
#                     callback=self.parse_search_vipcn
#                 )
#
#     def parse_search_vipcn(self, response):
#         # TODO 数据库查询公众号名称
#         self.vipcn = PlusSpiderSpiderWxb.get_search('rmrbwx')['data'][0]['wx_origin_id']
#         url = 'https://data.wxb.com/details/postRead?id=%s' %self.vipcn
#         yield scrapy.Request(url, callback=self.parse_vipcn)
#
#     def parse_vipcn(self, response):
#         vipcn =  response.xpath('//div[@class="detail-overview"]/div')
#         # 账号主体
#         vipcn.xpath('./div[@class="content company"]/text()').extract()[0]
#         # 分类
#         vipcn.xpath('./div[@class="content category"]/text()').extract()[0]
#         total = vipcn.xpath('//div[@class="inform-wrap"]/div[@class="inform-item"]/text()').extract()
#         # 人民日报认证
#         total[0]
#         # 微信号：rmrbwx
#         total[1]
#         # 功能介绍：参与、沟通、记录时代。
#         total[2]
#         # 二维码
#         vipcn.xpath('//div[@class="wxb-avatar-img"]/img/@src/text()').extract()[0]
#         # 发文情况
#         dispatch = response.xpath('//div[@class="card-number"]/text()').extract()
#         # 发文次数
#         dispatch[0]
#         # 每次平均发文篇数
#         dispatch[1]
#         # 阅读量
#         pv_views = response.xpath('//div[@class="ant-card-body"]/div[@class="item"]/text()').extract()
#         # 头条平均阅读量
#         pv_views[0]
#         # 非头条平均阅读量
#         pv_views[1]
#         # 最高阅读量
#         pv_views[2]
#         # 头条平均点赞数
#         pv_views[3]
#         # 最高点赞数
#         pv_views[4]
#
#
#         # url = 'https://data.wxb.com/account/statChart/%s?period=7&start_date=&end_date=' %self.vipcn
#         # yield scrapy.Request(url, callback=self.parse_stat_chart)
#         # url = 'https://data.wxb.com/account/rank/%s?period=7&start_date=&end_date=' % self.vipcn
#         # yield scrapy.Request(url, callback=self.parse_stat_rank)
#
#     def parse_stat_chart(self, response):
#         print '--------parse_stat_chart---------'
#         print response.body
#
#     def parse_stat_rank(self, response):
#         print '--------parse_stat_rank---------'
#         print response.body
#
#     @staticmethod
#     def get_search(kw):
#         url = "https://data.wxb.com/search"
#         querystring = {"page": "1", "page_size": "10", "kw": kw, "category_id": "", "start_rank": "*",
#                        "end_rank": "*",
#                        "fans_min": "", "fans_max": "", "is_verify": "0", "is_original": "0", "is_continuous": "0"}
#         headers = {
#             'accept': "application/json, text/plain, */*",
#             'accept-encoding': "gzip, deflate, br",
#             'accept-language': "zh-CN,zh;q=0.9,en;q=0.8",
#             'connection': "keep-alive",
#             'cookie': "aliyungf_tc=AQAAANTM9F5nqw4AxpNuJDUMUROMlLBI; visit-wxb-id=23d1de18465acdf97efb030c699b72a6; wxb_fp_id=635308960; Hm_lvt_5859c7e2fd49a1739a0b0f5a28532d91=1542160082; Hm_lpvt_5859c7e2fd49a1739a0b0f5a28532d91=1542160082; PHPSESSID=ae5c7be5c117db7feccd03e4bf1301fa",
#             'host': "data.wxb.com",
#             'referer': "https://data.wxb.com/searchResult?kw=%E4%BA%BA%E6%B0%91%E6%97%A5%E6%8A%A5&page=1",
#             'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
#             'x-requested-with': "XMLHttpRequest",
#             'cache-control': "no-cache",
#             'postman-token': "3be6ce3e-5d0f-0f6f-b9f4-794a3a5fd625"
#         }
#         response = requests.request("GET", url, headers=headers, params=querystring)
#         # print json.loads(response.text)
#         return json.loads(response.text)
#

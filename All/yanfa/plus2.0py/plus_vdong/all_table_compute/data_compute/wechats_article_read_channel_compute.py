# -*- coding: UTF-8 -*-
from plus_vdong.all_table_compute.data_source.wx_source.wechats_api import WechatsApi
class DbPlusWechatsArticleReadChannelCompute:

    def __init__(self, uniacid,date,key,sercet):
        self.read_channel_data = []
        self.uniacid = uniacid
        self.begin_date = date
        self.end_date = date
        self.key = key
        self.sercet = sercet
        self._wechats_api = WechatsApi(key, sercet,self.begin_date,self.end_date)
        pass

    def get_data(self):
        self.set_data()
        return self.read_channel_data

    def set_data(self):
        data = self.__gat_api_article_share_read(self.begin_date, self.end_date)
        self.__set_read_channel_data(data)

    # 写入渠道数据到数据流
    def __set_read_channel_data(self, data):
        for item in data:

            item = {
                "uniacid": self.uniacid,
                "int_page_read_user": item["int_page_read_user"],
                "int_page_read_count": item["int_page_read_count"],
                "ori_page_read_user": item["ori_page_read_user"],
                "ori_page_read_count": item["ori_page_read_count"],
                "user_source": item["user_source"],
                "create_date": item["ref_date"]
            }
            self.read_channel_data.append(item)

    # 获取图文阅读、转发等信息
    def __gat_api_article_share_read(self, begin_date, end_date):
        res = self._wechats_api.get_user_read(begin_date, end_date)

        return res
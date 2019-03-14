# -*- coding: UTF-8 -*-
from data_stats.common.wechat.wechat import Wechat
from data_stats.common.wechat.api.vipcn.datacube import DataCube
class WechatsApi(object):
    def __init__(self,key=None, sercet=None,begin_date=None,end_date=None):

        self.key = key
        self.sercet = sercet
        self.begin_date = begin_date
        self.end_date = end_date
        self.i_data = {}
        wechat_obj = Wechat(key,sercet)
        self.api =  DataCube(wechat_obj)


    # 获取关注取消信息
    def get_user_summary(self,begin_date,end_date):
        res = self.api.get_user_summary(begin_date,end_date)

        if res == False:
            raise RuntimeError('接口调用异常')
        return res

    # 获取用户总关注人数
    def get_user_cumulate(self, begin_date, end_date):
        res = self.api.get_user_cumulate(begin_date, end_date)
        return res

    # 获取图文阅读、转发等信息
    def get_user_read(self, begin_date, end_date):
        res = self.api.get_user_read(begin_date, end_date)
        return res

    # 每日发送文章数量
    def get_article_total(self, begin_date, end_date):
        res = self.api.get_article_total(begin_date, end_date)
        return len(res)




# -*- coding: UTF-8 -*-
# 只能查一天的数据
from plus_vdong.all_table_compute.data_source.wx_source.wechats_api import WechatsApi
import json
class DbPlusWechatsArticleReadCountCompute:

    def __init__(self, uniacid,date,key,sercet):
        self.read_count_data = { \
            "int_page_read_user": 0, "int_page_read_count": 0, "ori_page_read_user": 0, "ori_page_read_count": 0, \
            "share_user": 0, "share_count": 0, "add_to_fav_user": 0, "add_to_fav_count": 0 \
            }
        self.uniacid = uniacid
        self.begin_date = date
        self.end_date = date
        self.key = key
        self.sercet = sercet
        self._wechats_api = WechatsApi(key, sercet,self.begin_date,self.end_date)
        pass

    def get_data(self):
        self.set_data()
        return self.read_count_data

    def set_data(self):
        data = self.__gat_api_article_share_read(self.begin_date, self.end_date)
        self.__set_read_count_data(data)

        self.read_count_data["send_article_count"] = self.__get_api_article_total(self.begin_date, self.end_date)
        self.read_count_data["uniacid"] = self.uniacid
        # 计算昨日周同比、日环比
        compare_obj = Compare(self.uniacid, self.end_date)
        compare = compare_obj.set_data(self.read_count_data, 'int_page_read_count').compare()
        compare.update(compare_obj.set_data(self.read_count_data, 'ori_page_read_count').compare())
        compare.update(compare_obj.set_data(self.read_count_data, 'share_count').compare())
        compare.update(compare_obj.set_data(self.read_count_data, 'add_to_fav_count').compare())
        self.read_count_data["compare"] = json.dumps(compare)

        # 写入阅读数据到数据流
    def __set_read_count_data(self, data):
        for item in data:
            self.read_count_data["add_to_fav_count"] += item["add_to_fav_count"]
            self.read_count_data["add_to_fav_user"] += item["add_to_fav_user"]
            self.read_count_data["int_page_read_user"] += item["int_page_read_user"]
            self.read_count_data["int_page_read_count"] += item["int_page_read_count"]
            self.read_count_data["ori_page_read_user"] += item["ori_page_read_user"]
            self.read_count_data["ori_page_read_count"] += item["ori_page_read_count"]
            self.read_count_data["share_count"] += item["share_count"]
            self.read_count_data["share_user"] += item["share_user"]
            self.read_count_data["create_date"] = item["ref_date"]  # 给日期赋值，多条记录里面的值都相同


    # 获取图文阅读、转发等信息
    def __gat_api_article_share_read(self, begin_date, end_date):
        res = self._wechats_api.get_user_read(begin_date, end_date)
        return res

        # 每日发送文章数量
    def __get_api_article_total(self, begin_date, end_date):
        res = self._wechats_api.get_article_total(begin_date, end_date)
        return res


from plus_vdong.common.api.compare_ratio import CompareRatio
from plus_vdong.all_table_compute.data_source.db_source.plus_wechats_article_read_count import PlusWechatsArticleReadCount
from plus_vdong.utils.date_utils import *
#累计关注人数比
class Compare(CompareRatio):
    def __init__(self,uniacid,create_date):
        self.create_date = create_date
        self.uniacid = uniacid
        self.seven_days_ago = param_day_yesterday(str(create_date),days=-7)
        self.yesterday = param_day_yesterday(str(create_date))

    # 本期
    def set_data(self,data,field):
        self.field = field
        self.data = data
        return self
    def current_period_data(self):
        return self.data.get(self.field,0)


    def week_the_corresponding_period_data(self):
        # 同期数：从昨日起往前推算的第7日的关注用户总数
        return PlusWechatsArticleReadCount().get_data(self.seven_days_ago,self.uniacid,self.field)

    def day_the_corresponding_period_data(self):
        # 同期数：从昨日起往前推算前一天的图文阅读总次数
        return PlusWechatsArticleReadCount().get_data(self.yesterday, self.uniacid,self.field)

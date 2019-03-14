# -*- coding: UTF-8 -*-


import json
from plus_vdong.all_table_compute.data_source.wx_source.wechats_api import WechatsApi
class DbPlusWechatsMemberAnalysisCompute(object):

    def __init__(self, uniacid,date,key,sercet):
        self.data = {}
        self.uniacid = uniacid
        self.begin_date = date
        self.end_date = date
        self.key = key
        self.sercet = sercet
        self._wechats_api = WechatsApi(key, sercet,self.begin_date,self.end_date)
        pass


    #返回昨日累计关注总数、昨日新增、取消、净增用户数
    def get_data(self):
        compare = {}
        self.get_yesterday_user_data()
        self.get_user_count_data()
        # 计算昨日周同比、日环比
        compare_obj = Compare(self.uniacid, self.end_date)
        compare = compare_obj.set_data(self.data,'cumulate_user').compare()
        compare.update(compare_obj.set_data(self.data, 'new_user').compare())
        compare.update(compare_obj.set_data(self.data, 'cancel_user').compare())
        compare.update(compare_obj.set_data(self.data, 'incr_user').compare())
        self.data["compare"] = json.dumps(compare)
        return self.data

    # 获取昨天的用户关注取消信息
    def get_yesterday_user_data(self):
        res = self.__gat_api_user_concern_data(self.begin_date,self.end_date)
        data = {"new_user": 0, "cancel_user": 0, "ref_date": "","incr_user":0,"uniacid":self.uniacid}
        for item in res:
            data['new_user'] += item['new_user']
            data['cancel_user'] += item['cancel_user']
            data['ref_date'] = item['ref_date']
            # 计算净增用户
            data['incr_user'] = data['new_user'] - data['cancel_user']
        # 把数据写入数据流
        self.data["new_user"] = data["new_user"]
        self.data["cancel_user"] = data["cancel_user"]
        self.data["incr_user"] = data["incr_user"]
        self.data["create_date"] = data["ref_date"]
        self.data["uniacid"] = data["uniacid"]


    def get_user_count_data(self):
        res  = self.__gat_api_user_count_data(self.begin_date,self.end_date)
        data = {"cumulate_user":0}
        for item in res:
            data['cumulate_user'] += item['cumulate_user']

        #把总关注信息写入数据流中
        self.data["cumulate_user"] = data['cumulate_user']


    # 获取关注取消信息
    def __gat_api_user_concern_data(self,begin_date,end_date):

        res = self._wechats_api.get_user_summary(begin_date,end_date)
        return res

    # 获取用户总关注人数
    def __gat_api_user_count_data(self, begin_date, end_date):
        res = self._wechats_api.get_user_cumulate(begin_date, end_date)
        return res


from plus_vdong.common.api.compare_ratio import CompareRatio
from plus_vdong.all_table_compute.data_source.db_source.plus_wechats_member_analysis import PlusWechatsMemberAnalysis
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
        return PlusWechatsMemberAnalysis().get_data(self.seven_days_ago,self.uniacid,self.field)

    def day_the_corresponding_period_data(self):
        # 同期数：从昨日起往前推算前一天的图文阅读总次数
        return PlusWechatsMemberAnalysis().get_data(self.yesterday, self.uniacid,self.field)

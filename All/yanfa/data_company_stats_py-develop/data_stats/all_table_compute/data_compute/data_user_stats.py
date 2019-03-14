# -*- coding: UTF-8 -*-
from data_stats.all_table_compute.data_source.db_source.middle_expire_user import DataMiddleExpireUser,DataMiddleExpireUserSource
from data_stats.all_table_compute.data_source.db_source.middle_user import DataMiddleUserSource
from data_stats.all_table_compute.data_source.db_source.weichen_version import DataWeichenVersionSource
from data_stats.utils.date_utils import get_date_by_date
from data_stats.utils.db_util import insert

class DataUserStatsCompute(object):

    def __init__(self,query_date):
        self.query_date = query_date

    def total_user(self):
        return DataMiddleUserSource().count_total_user()

    def weichen_user(self):
        return DataMiddleUserSource().count_user_for_form('weichen')

    def plus_user(self):
        return DataMiddleUserSource().count_user_for_form('plus')

    def weichen_pay_user(self):
        count = 0
        list = DataWeichenVersionSource().select_version_list(0)
        for item in list:
            count += DataMiddleUserSource().count_group_user_with_weichen(item.group,item.weichen_version)
        return count

    def weichen_keep_user(self):
        #对比用户信息 如果今日的到期时间大于昨日的到期时间 说明用户进行了续费
        return DataMiddleExpireUserSource().count_keep_user()
        #把用户写入到到期用户表 便于与下一天更新的用户信息对比到期时间
        '''exprie_list = []
        list = DataMiddleUserSource().select_total_user()
        for item in list:
            field = {'user_id': item.user_id, 'weichen_version': item.weichen_version, 'create_date': self.query_date,
                     'from': item.from_}
            exprie_list.append(field)
        insert(DataMiddleExpireUser,exprie_list)'''

    def weichen_lose_user(self):
        return DataMiddleUserSource().count_weichen_lose_user(get_date_by_date(self.query_date,-15))

    def active_user(self):
        return DataMiddleUserSource().count_user_from_active_date(self.query_date)

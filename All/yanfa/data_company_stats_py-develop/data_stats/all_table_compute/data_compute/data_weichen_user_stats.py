# -*- coding: UTF-8 -*-
from data_stats.all_table_compute.data_source.db_source.middle_user import DataMiddleUserSource
from data_stats.all_table_compute.data_source.db_source.weichen_version import DataWeichenVersionSource
from data_stats.all_table_compute.data_source.db_source.middle_expire_user import DataMiddleExpireUser,DataMiddleExpireUserSource

import time, datetime
from data_stats.utils.date_utils import get_date_by_date

class DataWeichenUserStatsCompute(object):

    def __init__(self,query_date):
        self.query_date = query_date

    def pay_user(self):
        count = 0
        list = DataWeichenVersionSource().select_version_list(0)
        for item in list:
            count += DataMiddleUserSource().count_group_user_with_weichen(item.group,item.weichen_version)
        return count

    def keep_user(self):
        return DataMiddleExpireUserSource().count_keep_user()

    def lose_user(self):
        return DataMiddleUserSource().count_weichen_lose_user(get_date_by_date(self.query_date,-15))

    def try_user(self):
        count = 0
        list = DataWeichenVersionSource().select_version_list(1)
        for item in list:
            count += DataMiddleUserSource().count_group_user_with_weichen(item.group,item.weichen_version)
        return count
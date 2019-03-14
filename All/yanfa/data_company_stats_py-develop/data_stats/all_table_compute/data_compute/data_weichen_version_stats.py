# -*- coding: UTF-8 -*-
from data_stats.all_table_compute.data_source.db_source.middle_user import DataMiddleUserSource
from data_stats.all_table_compute.data_source.db_source.weichen_version_stats import DataWeichenVersionStatsSource
from data_stats.utils.date_utils import get_date_by_date

class DataWeichenVersionStatsCompute(object):

    def __init__(self,query_date,weichen_version,group_id):
        self.query_date = query_date
        self.weichen_version = weichen_version
        self.group_id = group_id

    def total_user(self):
        return DataMiddleUserSource().count_group_user_with_weichen(self.group_id,self.weichen_version)

    def last_user(self):
        count = 0
        res = DataWeichenVersionStatsSource().get_info_someday(get_date_by_date(self.query_date),self.weichen_version,self.group_id)
        if res is not None:
            count = res['total_user']
        return  count
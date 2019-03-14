# -*- coding: UTF-8 -*-

from data_stats.all_table_compute.data_compute.data_weichen_user_stats import DataWeichenUserStatsCompute
from data_stats.all_table_compute.data_source.db_source.weichen_user_stats import DataWeichenUserStatsSource
from data_stats.utils.date_utils import get_date_by_date

class DataWeichenUserStats(object):
    _data = []
    def __init__(self,query_date):
        self.query_date = query_date

    def set_data(self):
        last_info = DataWeichenUserStatsSource().get_info_someday(get_date_by_date(self.query_date))
        compute = DataWeichenUserStatsCompute(self.query_date)
        field = {
            'pay_user' : compute.pay_user(),
            'keep_user' : compute.keep_user(),
            'lose_user' : compute.lose_user(),
            'try_user' : compute.try_user(),
            'create_date' : self.query_date,
            'new_pay_user' : 0,
            'new_keep_user' : 0,
            'new_lose_user' : 0,
            'new_try_user': 0
        }
        if last_info is not None:
            diff_user = field['pay_user'] - last_info['pay_user']
            field['new_pay_user'] = diff_user if diff_user>1 else 0

            diff_user = field['keep_user'] - last_info['keep_user']
            field['new_keep_user'] = diff_user if diff_user>1 else 0

            diff_user = field['lose_user'] - last_info['lose_user']
            field['new_lose_user'] = diff_user if diff_user>1 else 0

            diff_user = field['try_user'] - last_info['try_user']
            field['new_try_user'] = diff_user if diff_user>1 else 0

        self._data.append(field)

    def get_data(self):
        self.set_data()
        return self._data

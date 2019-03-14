# -*- coding: UTF-8 -*-

from data_stats.all_table_compute.data_compute.data_user_stats import DataUserStatsCompute

class DataUserStats(object):
    _data = []
    def __init__(self,query_date):
        self.query_date = query_date

    def set_data(self):
        compute = DataUserStatsCompute(self.query_date)
        field = {
            'total_user' : compute.total_user(),
            'weichen_user' : compute.weichen_user(),
            'plus_user' : compute.plus_user(),
            'weichen_pay_user' : compute.weichen_pay_user(),
            'weichen_keep_user' : compute.weichen_keep_user(),
            'weichen_lose_user' : compute.weichen_lose_user(),
            'active_user' : compute.active_user(),
            'create_date' : self.query_date,
        }
        self._data.append(field)

    def get_data(self):
        self.set_data()
        return self._data
